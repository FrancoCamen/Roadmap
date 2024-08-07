# Pila de cartas
from pila import Pila
from random import randint

cartas = Pila();
cartas_aux = Pila();

# Carga aleatoria de las cartas en la pila
for i in range (0, 48):
    validacion = False;
    while validacion == False:
        # Genera el codigo de la carta
        numero_carta = str(randint(1, 12));
        palo_carta = str(randint(1,4));
        if palo_carta == "1":
            palo_carta = "oro";
        elif palo_carta == "2":
            palo_carta = "basto";
        elif palo_carta == "3":
                palo_carta = "espada";
        elif palo_carta == "4":
            palo_carta = "copa";
        carta = numero_carta + palo_carta;
         
        # Compara si el codigo de la carta ya existe en la pila
        if cartas.size() == 0:
            cartas.push(carta);
            validacion = True;
        else:
            no_es_igual = True;
            while cartas.size() > 0:
                carta_comp = cartas.pop();
                cartas_aux.push(carta_comp);
                if carta_comp == carta:
                    no_es_igual = False;
                    break
            while cartas_aux.size() > 0:
                cartas.push(cartas_aux.pop());
            if no_es_igual == True:
                cartas.push(carta);
                validacion = True;

# Funcion que reparte las cartas del maso de forma aleatoria
def repartir(cartas):
    print("Repartiendo maso de cartas...");
    maso = Pila();
    while cartas.size() > 0:
        i = randint(0, cartas.size());
        for x in range(0, i):
            carta = cartas.pop();
            maso.push(carta);
        if maso.size() != 0:
                carta_seleccionada = maso.pop();
                print(carta_seleccionada);
        while maso.size() > 0:
            cartas.push(maso.pop());
            
# Funcion que separa las cartas en 4 pilas por palo
def separar(cartas):
    oros = Pila()
    bastos = Pila()
    espadas = Pila()
    copas = Pila()
    oros_aux = Pila()
    bastos_aux = Pila()
    espadas_aux = Pila()
    copas_aux = Pila()

    while cartas.size() > 0:
        carta = cartas.pop();
        palo1_carta = carta[0];
        nueva1_carta = carta.replace(palo1_carta, "");
        palo2_carta = carta[0] + carta[1];
        nueva2_carta = carta.replace(palo2_carta, "");

        if nueva1_carta == "oro" or nueva2_carta == "oro":
            oros.push(carta);
        elif nueva1_carta == "basto" or nueva2_carta == "basto":
            bastos.push(carta);
        elif nueva1_carta == "espada" or nueva2_carta == "espada":
            espadas.push(carta);
        elif nueva1_carta == "copa" or nueva2_carta == "copa":
            copas.push(carta);
        else:
            print("Hubo un error");

    # Mostando pilas 
    print("Pila de cartas de Oro");
    while oros.size() > 0:
        cart = oros.pop()
        print(cart);
        oros_aux.push(cart);
    print("Pila de cartas de Basto");
    while bastos.size() > 0:
        print(bastos.pop());
    print("Pila de cartas de Espada");
    while espadas.size() > 0:
        print(espadas.pop());
    print("Pila de cartas de Copa");
    while copas.size() > 0:
        print(copas.pop());

    # Mostrando pila Oro ordenada
    print("Pila de Oro ordenada")
    while oros.size() > 0 or oros_aux.size() > 0:
        for x in range(1,13):
            while oros.size() > 0:
                carta = oros.pop()
                carta_nueva = int(carta[0:(len(carta)-3)])
                if carta_nueva == x:
                    print(carta)
                else:
                    oros_aux.push(carta)
            while oros_aux.size() > 0:
                carta = oros_aux.pop()
                carta_nueva = int(carta[0:(len(carta)-3)])
                if carta_nueva == x:
                    print(carta)
                else:
                    oros.push(carta)

separar(cartas);

        



    
