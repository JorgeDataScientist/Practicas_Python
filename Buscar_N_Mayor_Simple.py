def custom_max(n1: int, n2: int, n3: int):
    """
        Dado dos numeros de entrada, retorna el mayor de ambos
        :param n1: Primer numero a comparar
        :param n2: Segundo numero a comparar
        :return: el mayor de n1 y n2
    """
    if n1 > n2 > n3:
        return n1
    elif n2 > n3:
        return n2
    elif n1 < n3:
        return n3
    else:
        return 'Los numeros son iguales'

print(custom_max(12, 7, 0))
print(custom_max(2, 9, 6))
print(custom_max(6, 7, 4))