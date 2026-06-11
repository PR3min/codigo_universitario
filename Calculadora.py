def sumar(v1,v2):
    resultado=v1+v2
    return resultado
def resta(v1,v2):
    resultado=v1-v2
    return resultado
valor1=int(input("Ingrese valor: "))
valor2=int(input("Ingrese valor: "))
print(f"El resultado de suma es: {sumar(valor1,valor2)}")
print(f"El resultado de resta es: {resta(valor1,valor2)}")