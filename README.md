#Clases en Python
<hr><hr>

##Creando una clase
Se utiliza la palabra reservada _class_ seguido del nombre de la clase y dos puntos (_:_) seguido de las definiones de sus funciones

```python
class ATM:
	<declaración-1>
	.
	.
	<declaración-n>
```

##Variables de clase
Se declaran a continuación de declarar el nombre de la clase

```python
class ATM:
	noTransacciones = 0
```

##Objetos de clase
Soportan dos operaciones:

1. Referencias a atributos
2. Instanciación

###Referencias a atributos
```python
class ATM:
	noTransacciones = 0
	
	def saludo(self):
		return 'Buenos días. Ingrese su tarjeta por favor'
```

Tanto `ATM.noTransacciones ` como `ATM.saludo` son referencias a atributos válidos

###Instanciación

Se le asigna el valor a la variable con en nombre de la clase seguido de abre y cierre de paréntesis

`x = ATM()`

##Inicialización
Existen ocasiones en las que las clases deben tener propiedades con valores por defecto. Esto se logra a través del constructor.

```python
class ATM:
	noTransacciones = 0
	fechaHoraActual = ''
	
	def __init__(self, fHA):
		self.fechaHoraActual = fHA
	
	def saludo(self):
		return 'Buenos días. Ingrese su tarjeta por favor'
		
>>> x = ATM('Agosto 26 2016, 22:00')
>>> x.fechaHoraActual
(Agosto 26 2016, 22:00)

```

#Ejemplo final ATM.py

![alt text][logo]
[logo]: Resources/ATMpy.png "ATM.py"










.