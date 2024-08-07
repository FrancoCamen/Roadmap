import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:
	def scan(self):
		
		self.pos[1] += 1
		if self.pos[1] == len(self.stations):
			self.pos[1] = 0
			self.pos[0] +=1
			if self.pos[0] == len(self.frecuencias):
				self.pos[0] = 0
		
		print("Sintonizando... Estación {} {} {}".format(self.frecuencias[self.pos[0]], self.stations[self.pos[1]], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		
		self.radio = radio
		self.frecuencias = ["M1", "M2", "M3", "M4"]
		self.stations = ["1250", "1380", "1510"]
		self.pos = [0,0]
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
"""Separate class for FM state"""
class FmState(State):

	def __init__(self, radio):

		self.radio = radio
		self.frecuencias = ["M1", "M2", "M3", "M4"]
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = [0,0]
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

	def __init__(self):
		
		self.fmstate = FmState(self)
		self.amstate = AmState(self)
		#*--- Inicialmente en FM
		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

#*---------------------

if __name__ == "__main__":
	#os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 12 + [radio.toggle_amfm] + [radio.scan] * 12
	#actions *= 2

#*---- Recorre las acciones ejecutando la acción

	print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
	for action in actions:
		action()

