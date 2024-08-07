      //*------------------------------------------------------------------------------*
        //* setCliente
        //* API para modificar atributos de baja, activo y registrado del cliente
        //*
        //* Dr. Pedro E. Colla
        //* UADER - Ingeniería de Software I
        //* (c) 2023 Dr. Pedro E. Colla
        //*-----------------------------------------------------------------------------*
        
    import { DynamoDBClient, GetItemCommand, ScanCommand, PutItemCommand, UpdateItemCommand } from "@aws-sdk/client-dynamodb";
	import { randomUUID } from "crypto";
	import {marshall,unmarshall}  from "@aws-sdk/util-dynamodb";

	const ddbClient = new DynamoDBClient(new DynamoDBClient({}));
	export const handler = async (event, context) => {
	    try {
	        const cliente = JSON.parse(event.body);
	        

//*---- Arma clave de búsqueda

        const input = { 
            ExpressionAttributeNames: { 
                 "#a": "activo", 
                 "#r": "registrado"
            }, 
            ExpressionAttributeValues: { 
                ":a": { 
                   BOOL: cliente.activo 
                }, 
               ":r": { 
                   BOOL: cliente.registrado 
                },
           }, 
           Key: { 
               "id": { 
                   S: cliente.id 
           }}, 
           ReturnValues: "ALL_NEW", 
           TableName: "cliente", 
           UpdateExpression: "SET #a = :a, #r = :r" 
};



//*---- Realiza la busqueda y actualización
            
            const command = new UpdateItemCommand(input);
            const response = await ddbClient.send(command);

//*---- Hace el unmarshalling de los datos pues NO es un objeto DynamoDBDocumentClient y por lo tanto el resultado es un JSON que

            const uresponse=unmarshall(response.Attributes);

            return {
                  statusCode: 200,
     	            body: JSON.stringify({"data" : uresponse , "response" : "OK"}),
     	      };


//*----- Si algo anda mal retorna el error
                                                     
           } catch (error) {
                console.error(error);
                return {
                    statusCode: 500,
     	            body: JSON.stringify({ message: error.message , "response" : "Error" }),
                };
            }

};


