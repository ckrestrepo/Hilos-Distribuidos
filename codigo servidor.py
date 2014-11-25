import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

#Definimos la funcion
def dolar_a_peso(dolar):
	return dolar * 2142

#Abrimos el servidor para que acepte las peticiones
server = SimpleXMLRPCServer(("localhost", 8000))
print "Servidor abierto en el puerto 8000..."

#Registramos la funcion que hemos definido
server.register_function(dolar_a_peso, "funcion1")
server.serve_forever()