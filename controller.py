from funciones import sumar, restar, multiplicar, dividir

class ControladorCalculadora:
    def operar(self, operacion, a, b):
        if operacion == 'Suma':
            return sumar(a, b)
        elif operacion == 'Resta':
            return restar(a, b)
        elif operacion == 'Multiplicación':
            return multiplicar(a, b)
        elif operacion == 'División':
            return dividir(a, b)
        else:
            raise ValueError("Operación no válida")
