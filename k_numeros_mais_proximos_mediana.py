import random

def particiona(arr, p, r):
    x = arr[r]  # pivo
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def particionaAleatorio(arr, p, r):
    j = random.randint(p, r)
    arr[j], arr[r] = arr[r], arr[j]
    return particiona(arr, p, r)

def mediana(arr, p, r, i):
    if p == r:
        return arr[p]
    
    q = particionaAleatorio(arr, p, r)
    m = q - p + 1  # posicao do pivo 

    if i == m:
        return arr[q]
    elif i < m:
        return mediana(arr, p, q - 1, i)
    else:
        return mediana(arr, q + 1, r, i - m)

def k_mais_proximos_mediana(arr, k):
    n = len(arr)
    i = n // 2 + 1  # posicaoo da mediana
    med = mediana(arr[:], 0, n - 1, i)

    dist_val = [(abs(x - med), x) for x in arr if x != med]

    distancias = [d for d, v in dist_val]
    limite = mediana(distancias[:], 0, len(distancias) - 1, k)  # mediana baseada no quick select com particionamento aleatorio

    resultado = []

    for d, v in dist_val:
        if d < limite or (d == limite and len(resultado) < k):
            resultado.append(v)

    return resultado

if __name__ == "__main__":

    # Teste 1
    arr = [1, 2, 3, 4, 5]
    k = 2
    i = len(arr) // 2 + 1  # i = 3, mediana = 3
    print(f"Resultado Teste 1 : {k_mais_proximos_mediana(arr,k)}")
    # Resultado esperado: [2, 4]

    # Teste 2
    arr = [10, 20, 30, 40, 50, 60, 70]
    k = 3
    i = len(arr) // 2 + 1  # i = 4, mediana = 40
    print(f"Resultado Teste 2 : {k_mais_proximos_mediana(arr,k)}")
    # Resultado esperado: [30, 50, 20] ou [30, 50, 60]

    # Teste 3
    arr = [7, 13, 26, 31, 42, 59, 77, 84, 91]
    k = 4
    i = len(arr) // 2 + 1  # i = 5, mediana = 42
    print(f"Resultado Teste 3 : {k_mais_proximos_mediana(arr,k)}")
    # Resultado esperado: [31, 26, 59, 13]

    # Teste 4
    arr = [5, 9, 14, 20, 27, 33, 38]
    k = 2
    i = len(arr) // 2 + 1  # i = 4, mediana = 20
    print(f"Resultado Teste 4 : {k_mais_proximos_mediana(arr,k)}")
    # Resultado esperado: [14, 27]

    # Teste 5
    arr = [100, 150, 200, 250, 300, 350, 400]
    k = 3
    i = len(arr) // 2 + 1  # i = 4, mediana = 250
    print(f"Resultado Teste 5 : {k_mais_proximos_mediana(arr,k)}")
    # Resultado esperado: [200, 300, 150]