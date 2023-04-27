def impares(n):
    return range(1, 2*n, 2)

def verificar_curiosidad(n):
    suma_impares = sum(impares(n))
    cuadrado_n = n ** 2
    
    if cuadrado_n == suma_impares:
        return True
    else:
        return False

n = int(input("Ingrese el número al que desea comprobar la curiosidad matemática: "))
if verificar_curiosidad(n):
    print(f"La curiosidad matemática se cumple para n = {n}")
else:
    print(f"La curiosidad matemática NO se cumple para n = {n}")

