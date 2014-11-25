import xmlrpclib
try:
	#Leemos por pantalla
	n = int(raw_input("Digite la cantidad de dolares a convertir: "))
	#Conectamos con el servidor
	proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
	print "Cantidad de dolares en pesos (USD): %s" % str(proxy.funcion1(n))
	raw_input("Presione una tecla para terminar")

except ValueError:
	#Si el digito ingresado no es un numero
	print "Ha ingreso un digito incorrecto"