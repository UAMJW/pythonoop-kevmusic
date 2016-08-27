#Clases en Python
<hr><hr>

##Creando una clase
Se utiliza la palabra reservada `class` seguido del nombre de la clase y `:` seguido de las definiones de sus funciones

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
Existen ocasiones en las que las clases deben tener propiedades con valores por defecto. Esto se logra a través del constructor `def __init__(self, arg1, argN):`.

```python
class ATM:
	noTransacciones = 0
	fechaHoraActual = ''
	
	def __init__(self, fHA):
		self.fechaHoraActual = fHA
	
	def saludo(self):
		return 'Buenos dias. Ingrese su tarjeta por favor'
		
>>> x = ATM('Agosto 26 2016, 22:00')
>>> x.fechaHoraActual
(Agosto 26 2016, 22:00)

```

#Ejemplo final ATM.py
Código:

```python
import datetime

# Obteniendo la hora actual
now = datetime.datetime.now()

class ATM:
    noTransacciones = 0
    fechaHoraActual = ''
    
    def __init__(self, fHA):
        self.fechaHoraActual = fHA
    
    def saludo(self):
        return 'Buenos dias. Ingrese su tarjeta por favor'
        
x = ATM(now.strftime("%Y-%m-%d %H:%M"))
x.fechaHoraActual
```
![alt text][logo]
[logo]: Resources/ATMpy.png "ATM.py"










.