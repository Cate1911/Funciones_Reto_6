#Declarar la función
def valor_prestamo(c:float, i:float, n:float) -> float:
    valor_final_prestamo = c * (1 + (i/100))**n
    return valor_final_prestamo
#Definir la función main
if __name__ == "__main__":
    c = float(input("Ingrese el valor del préstamo socilitado: "))
    i = float(input("Ingrese el porcentaje de interés anual: "))
    n = float(input("Ingrese el tiempo que dura la inversión (en meses): "))
    valor_final_prestamo = valor_prestamo(c, i, n)
    print("El valor final del préstamo es de " + str(valor_final_prestamo))