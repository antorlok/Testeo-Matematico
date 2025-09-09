import numpy as np
import random
from Common.Repositories.FileManager import FileManager



def ExtraxtContent():
    try:
        path= "./Apps/DataProcessor/DataExtractor/Data/"
        fileManager = FileManager(path)
        archivo = fileManager.openFile("datos_generados.txt")
        numbers = np.zeros(250000, dtype=np.int32)
        i = 0
        for registro in archivo:
            campos = registro.strip().split("#")
            if not campos:
                continue
            if i < 250000:
                rand = random.random()
                if rand < 0.5:
                    if campos:
                        numbers[i] = str(random.choice(campos))
                        i += 1
            else:
                break 
        return numbers
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nom}'")
        return []


def dividir_arreglo_aleatorio(arr):
    mascara = np.random.rand(arr.size) < 0.5
    arreglo1 = arr[mascara]
    arreglo2 = arr[~mascara]
    
    max_len = max(arreglo1.size, arreglo2.size)
    if arreglo1.size < max_len:
        arreglo1 = np.pad(arreglo1, (0, max_len - arreglo1.size), constant_values=0)
    if arreglo2.size < max_len:
        arreglo2 = np.pad(arreglo2, (0, max_len - arreglo2.size), constant_values=0)
    return arreglo1, arreglo2

arreglo1, arreglo2 = dividir_arreglo_aleatorio(arreglo)
print(f"Arreglo 1 tiene {arreglo1.size} elementos")
print(f"Arreglo 2 tiene {arreglo2.size} elementos")


for i in range(len(arreglo1)):
    print(arreglo1[i],arreglo2[i])