import math


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(math.sqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True


def primos_hasta(limite_superior: int) -> list[int]:
    return [num for num in range(2, limite_superior + 1) if es_primo(num)]


# Ejemplo de uso
numero = 234
print(f"¿{numero} es primo?: {es_primo(numero)}")
print(f"Primos hasta 30: {primos_hasta(30)}")
