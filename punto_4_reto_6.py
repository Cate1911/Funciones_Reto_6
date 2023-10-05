#Declarar la función
def vueltas_billete_b(P:int, M:int, H:int, B:int) -> int:
  costo_total = P * 300 + M * 3300 + H * 350
  vueltas = B - costo_total
  return vueltas
#Definir la función main
if __name__ == "__main__":
  P = int(input("Ingrese la cantidad de panes que compró:"))
  M = int(input("Ingrese la cantidad de bolsas de leche que compró:"))
  H = int(input("Ingrese la cantidad de huevos que compró: "))
  B = int(input("Ingrese el valor del billete con el que pagó: "))
  vueltas = vueltas_billete_b(P, M, H, B)
  valor_absoluto_vueltas = abs(vueltas)
#Definir condiones para que se ejecute la instrucción según la condición que se cumpla
  if vueltas >= 0:
    print("Su cambio es " + str(vueltas))
  else:
    print("Quedó debiendo " + str(valor_absoluto_vueltas))