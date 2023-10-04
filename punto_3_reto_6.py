#Declarar la función para calcular la cantidad de carne de aves en kilos
def cantidad_carne_aves(N:int, M:int, K:int) -> int:
  carne_aves = 6 * N + 7 * M + K
  return carne_aves
#Definir la función main con las variables y con el resultado que quiero que muestre
if __name__ == "__main__":
  N = int(input("Ingrese la cantidad de gallinas:"))
  M = int(input("Ingrese la cantidad de gallos:"))
  K = int(input("Ingrese la cantidad de pollitos: "))
  carne_aves = cantidad_carne_aves(N, M, K)
  print("La cantidad de carne de aves que tiene es de " + str(carne_aves))