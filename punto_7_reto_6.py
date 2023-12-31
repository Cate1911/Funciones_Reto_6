#Declarar funciones
def calcular_promedio_numeros(a:float, b:float, c:float, d:float, e:float) -> float:
    promedio = (a + b + c + d + e) / 5
    return promedio

def calcular_mediana_numeros(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_numeros = [a, b, c, d, e]
    lista_numeros_ordenados = sorted(lista_numeros)
    longitud_lista = len(lista_numeros)
    mediana = lista_numeros_ordenados[longitud_lista // 2]
    return mediana

def calcular_promedio_multiplicativo(a:float, b:float, c:float, d:float, e:float) -> float:
    el_promedio_multiplicativo = ((a*b*c*d*e)**(1/5))
    return el_promedio_multiplicativo

def ordenar_numeros_ascendente(a:float, b:float, c:float, d:float, e:float) -> float:
    lista = [a, b, c, d, e]
    lista_ascendente = sorted(lista)
    return lista_ascendente

def ordenar_numeros_descendente(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_1 = [a, b, c, d, e]
    lista_descendente = sorted(lista_1, reverse = True)
    return lista_descendente

def calcular_potencia_mayor_numero_elevado_al_menor(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_2 = [a, b, c, d, e]
    mayor : float = max(lista_2)
    menor : float = min(lista_2)
    potencia = mayor ** menor
    return potencia

def calcular_raiz_cubica_menor_numero(a:float, b:float, c:float, d:float, e:float) -> float:
    lista_3 = [a, b, c, d, e]
    menor_1 : float = min(lista_3)
    raiz = menor_1 ** 1/3
    return raiz
if __name__ == "__main__":
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    d = float(input("Ingrese el cuarto número: "))
    e = float(input("Ingrese el quinto número: "))
    promedio = calcular_promedio_numeros(a, b, c, d, e)
    mediana = calcular_mediana_numeros(a, b, c, d, e)
    el_promedio_multiplicativo = calcular_promedio_multiplicativo(a, b, c, d, e)
    lista_ascendente = ordenar_numeros_ascendente(a, b, c, d, e)
    lista_descendente = ordenar_numeros_descendente(a, b, c, d, e)
    potencia = calcular_potencia_mayor_numero_elevado_al_menor(a, b, c, d, e)
    raiz = calcular_raiz_cubica_menor_numero(a, b, c, d, e)
    
    print("El promedio de los números ingresados es " + (str)(promedio))
    print("La mediana es "+ str(mediana))
    print("El promedio multiplicativo de los números es " + str(el_promedio_multiplicativo))
    print("La lista ordenada de manera ascendente: " + str(lista_ascendente))
    print("La lista ordenada de manera descendente: " + str(lista_descendente))
    print("La potencia del número mayor elevado al menor es " + str(potencia))
    print("La raíz cúbica del menor número es " + str(raiz))