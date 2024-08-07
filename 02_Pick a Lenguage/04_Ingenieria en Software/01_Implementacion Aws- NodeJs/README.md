# Mesa de Ayuda

Taller y práctico para la materia Ingeniería de Software I

Implementación (parcial) de arquitectura, componente y maquetado para aplicación mockup de mesa de ayuda.
Se utilizaron herramientas de Aws: Lambda, API Gateway y Dynamo DB
Tambien se utilizo el software Insomnia para realizar pruebas y test.

Implementación Full Stack Node.JS en AWS.

## Problema

Se resuelve la suigiente problematica: Dado el planteo de la aplicación para soporte de Mesa de Ayuda se desea hacer un diseño detallado e implementación (parcial) del componente clientes en una arquitectura de tipo “Serverless” utilizando los servicios de AWS Full Stack basado en Node.JS.

## API ticket
```
	/crearTicket	Crea un nuevo ticket
	/listarTicket	Lista todos los tickets de un cliente
```

## API cliente

```

	/addCliente	Agrega un nuevo cliente
	/getCliente	Recupera el registro de un cliente
	/setCliente	Actualiza banderas baja, activo, registrado
	/updateCliente	Actualiza datos del cliente
	/listCliente	Lista clientes
	/resetCliente	Hace reset de password y actualiza fecha
	/loginCliente	Revisa login y actualiza fecha
	/deleteCliente	Borra fisicamente un cliente
``