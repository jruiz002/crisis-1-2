# Data Center Resource Management: Crisis 2

Este proyecto contiene la solución algorítmica para la **Crisis 2 (Asignación de Memoria para Máquinas Virtuales)** descrita en el Caso de Estudio de *Análisis y Diseño de Algoritmos*. 

Implementa una solución basada en **Programación Dinámica (0/1 Knapsack problem)** para determinar la asignación óptima de memoria de un servidor físico sin exceder su capacidad estricta, maximizando al mismo tiempo el valor computacional o rentabilidad de las Máquinas Virtuales (VMs).

## Estructura del Proyecto

El código está estructurado modularmente siguiendo buenas prácticas de Ingeniería de Software:
- `models.py`: Define el modelo inmutable de datos `VirtualMachine` empleando `dataclasses`.
- `allocator.py`: Contiene el algoritmo voraz / programación dinámica (`VMMemoryAllocator`) utilizando un enfoque *bottom-up* con tabulación y reconstrucción (backtracking).
- `main.py`: Archivo principal que ejecuta y demuestra la funcionalidad del algoritmo utilizando el caso real del enunciado.

## Requisitos Previos

- Python 3.8 o superior.
- No se requieren dependencias de terceros (solo librerías de la Standard Library de Python).

## ¿Cómo ejecutar el proyecto?

1. Abre tu terminal.
2. Navega al directorio donde se extrajo este proyecto (`crisis-2/`).
3. Ejecuta el archivo principal mediante el siguiente comando:

```bash
python3 main.py
```

Al final de la ejecución, el programa imprimirá:
1. El tamaño total de memoria del servidor ($W$).
2. Las VMs disponibles junto con sus pesos y valores.
3. El resultado máximo de valor computacional posible.
4. La selección óptima estricta de cuáles VMs garantizan dicho máximo sin desbordar el recurso físico.
