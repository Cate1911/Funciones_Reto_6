from funciones_7 import calcular_promedio_numeros
from funciones_7 import calcular_mediana_numeros
from funciones_7 import calcular_promedio_multiplicativo
from funciones_7 import ordenar_numeros_ascendente
from funciones_7 import ordenar_numeros_descendente
from funciones_7 import calcular_potencia_mayor_numero_elevado_al_menor
from funciones_7 import calcular_raiz_cubica_menor_numero

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