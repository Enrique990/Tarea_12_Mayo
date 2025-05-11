import random
from collections import Counter

numeros = [random.randint(1, 100) for _ in range(100)]

numeros_ordenados = sorted(numeros)

frecuencia_numeros = Counter(numeros_ordenados)

print("Matriz ordenada:")
print(numeros_ordenados)
print("\n" + "="*50 + "\n")

print("Tabla de Frecuencias:")
print("--------------------")
print("| Número | Cantidad |")
print("|--------|----------|")
for numero, cantidad in sorted(frecuencia_numeros.items()):
    print(f"| {numero:<6} | {cantidad:<8} |")
print("--------------------")