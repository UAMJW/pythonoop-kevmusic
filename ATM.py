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