class Task:
    def __init__(self, task_id, deadline, penalty):
        self.task_id = task_id
        self.deadline = deadline
        self.penalty = penalty

    def __repr__(self):
        return f"Task(id={self.task_id}, d={self.deadline}, w={self.penalty})"

class DisjointSet:
    """
    Estructura de datos de Conjuntos Disjuntos (Union-Find) para encontrar 
    el último tiempo disponible eficientemente en tiempo casi constante O(α(n)).
    """
    def __init__(self, size):
        self.parent = list(range(size + 1))

    def find(self, i):
        # Path compression
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        self.parent[root_i] = root_j

def schedule_tasks(tasks):
    """
    Implementación del algoritmo Greedy propuesto en la Crisis 1 utilizando
    un Matroide Ponderado. 
    
    1. Ordenar por penalidad descendente: O(n log n)
    2. Encontrar el slot disponible (Disjoint Set) y asignarlo: O(n α(n))
    
    Tiempo de Ejecución Total: O(n log n)
    """
    # 1. Criterio elegido: f(a_i) = w_i
    # Ordenar tareas iterativamente de mayor a menor penalidad
    tasks.sort(key=lambda x: x.penalty, reverse=True)
    
    if not tasks:
        return [], [], 0

    # 2. Encontrar el plazo máximo para fijar la ventana de tiempo.
    max_deadline = max(task.deadline for task in tasks)
    # No necesitamos más espacios de tiempo que la cantidad de tareas o el deadline máximo
    max_time_slot = min(max_deadline, len(tasks))

    ds = DisjointSet(max_time_slot)
    
    scheduled = []
    missed = []
    total_penalty = 0
    schedule = [None] * (max_time_slot + 1)
    
    for task in tasks:
        # El espacio de tiempo t no debe superar su deadline ni el slot máximo del sistema
        target_slot = min(task.deadline, max_time_slot)
        
        # Buscar el espacio de tiempo disponible más cercano hacia la izquierda
        available_slot = ds.find(target_slot)
        
        if available_slot > 0:
            # Se puede completar la tarea, asignar al slot
            schedule[available_slot] = task
            scheduled.append(task)
            # Unir con el espacio de su izquierda para indicar que este slot fue ocupado
            ds.union(available_slot, available_slot - 1)
        else:
            # 0 indica que todos los espacios temporales antes de t (inclusive) están ocupados
            # Se incumple el plazo y cursa la masiva penalidad financiera
            missed.append(task)
            total_penalty += task.penalty
            
    # Remover campos vacíos en el horario para devolver el cronograma ordenado temporalmente
    final_schedule = [t for t in schedule if t is not None]
            
    return final_schedule, missed, total_penalty

if __name__ == "__main__":
    # Ejemplo de la alternativa descartada 1 
    # S = {a1, a2, a3}, (d1=1, w1=10), (d2=2, w2=100), (d3=2, w3=100)
    tasks = [
        Task("a1", 1, 10),
        Task("a2", 2, 100),
        Task("a3", 2, 100)
    ]
    
    scheduled, missed, total_penalty = schedule_tasks(tasks)
    
    print("Tareas Programadas:", scheduled)
    print("Tareas Fallidas (Penalizadas):", missed)
    print("Penalidad Total Incurrida:", total_penalty)
