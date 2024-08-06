Algoritmo sin_titulo
	Escribir "Instrucciones para escuchar su cancion favorita en Spotify"
	Escribir "Elija en que condicion se encuentra"
	Escribir "1.Tengo descargado, instalado y ejecutado Spotify"
	Escribir "2.No tengo descargado Spotyfy"
	Escribir "3.Tengo descargado Spotify pero no instalado"
	Escribir "4.Tengo descargado e instalado Spotify"
	Leer option
	P1 = "Primeramente debe descargar el instalador de Spotify desde su pagina oficial"
	P2 = "Instalar el programa hacinedo doble click sobre el instalador"
	P3 = "Aceptar los terminos y condiciones"
	P4 = "Elegir la direccion donde se instalara el programa"
	P5 = "Esperar a que finalice la instalacion"
	P6 = "Ejecutar el programa"
	P7 = "Vincular su cuenta de Spotify o crearla su es un usuario nuevo"
	P8 = "Acceder al buscador en la parte superior derecha y hacer click en buscar"
	P9 = "Escribir en el buscador el nombre la cancion que desea escuchar y teclear enter"
	P10 = "Para finalizar reproducir la cancion"
	Segun option Hacer
		2:
			Escribir P1
			Escribir P2
			Escribir P3
			Escribir P4
			Escribir P5
			Escribir P6
			Escribir P7
			Escribir P8
			Escribir P9
			Escribir P10
		1:
			Escribir P7
			Escribir P8
			Escribir P9
			Escribir P10
		3:
			Escribir P2
			Escribir P3
			Escribir P4
			Escribir P5
			Escribir P6
			Escribir P7
			Escribir P8
			Escribir P9
			Escribir P10
		4:
			Escribir P6
			Escribir P7
			Escribir P8
			Escribir P9
			Escribir P10
		De Otro Modo:
			Escribir "La opcion ingresada es incorrecta"
	Fin Segun
FinAlgoritmo
