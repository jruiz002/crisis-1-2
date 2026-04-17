# Data Center Resource Management: Crisis 1 & Crisis 2

Este proyecto contiene las soluciones algorítmicas para las **Crisis 1 y 2** descritas en el Caso de Estudio de *Análisis y Diseño de Algoritmos* sobre la gestión de recursos en un Centro de Datos.

## Soluciones Implementadas

### Crisis 1: Programación de Tareas de Alto Riesgo
Implementa una solución basada en un enfoque **Greedy (Voraz)** apoyado en un **Matroide Ponderado** y la estructura de datos *Conjuntos Disjuntos* (Union-Find). Minimiza la penalidad financiera total al agendar tareas críticas de tiempo unitario en su respectivo límite de tiempo (deadline).

### Crisis 2: Asignación de Memoria para Máquinas Virtuales
Implementa una solución basada en **Programación Dinámica (0/1 Knapsack problem)** para determinar la asignación óptima de memoria de un servidor físico sin exceder su capacidad estricta, maximizando al mismo tiempo el valor computacional o rentabilidad de las Máquinas Virtuales (VMs).

## Estructura del Proyecto

El código está estructurado modularmente siguiendo buenas prácticas de Ingeniería de Software:
- `crisis-1/task_scheduler.py`: Contiene la implementación óptima del algoritmo Greedy para la planeación de tareas usando Conjuntos Disjuntos.
- `models.py`: Define el modelo inmutable de datos `VirtualMachine` empleando `dataclasses` (Crisis 2).
- `allocator.py`: Contiene el algoritmo de programación dinámica (`VMMemoryAllocator`) utilizando un enfoque *bottom-up* con tabulación y reconstrucción (Crisis 2).
- `main.py`: Archivo principal que ejecuta y demuestra la funcionalidad del algoritmo de asignación de memoria (Crisis 2).

## Requisitos Previos

- Python 3.8 o superior.
- No se requieren dependencias de terceros (solo librerías de la Standard Library de Python).

## ¿Cómo ejecutar el proyecto?

1. Abre tu terminal.
2. Navega al directorio raíz del proyecto.

### Ejecución de la Crisis 1
Para ver la planificación óptima de las tareas de alta prioridad sujeto a vencimientos:

```bash
python crisis-1/task_scheduler.py
```

### Ejecución de la Crisis 2
Para ejecutar el algoritmo de Programación Dinámica evaluando la asignación de VMs:

```bash
python crisis-2/main.py
```

Al final de la ejecución de la Crisis 2, el programa imprimirá:
1. El tamaño total de memoria del servidor ($W$).
2. Las VMs disponibles junto con sus pesos y valores.
3. El resultado máximo de valor computacional posible.
4. La selección óptima estricta de cuáles VMs garantizan dicho máximo sin desbordar el recurso físico.
