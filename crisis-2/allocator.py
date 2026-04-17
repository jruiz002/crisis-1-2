from typing import List, Tuple
from models import VirtualMachine

class VMMemoryAllocator:
    """
    Clase encargada de la asignación de memoria para Máquinas Virtuales (VMs)
    utilizando Programación Dinámica (Enfoque bottom-up para el problema 0/1 Knapsack).
    """

    @staticmethod
    def allocate(vms: List[VirtualMachine], max_memory: int) -> Tuple[float, List[VirtualMachine]]:
        """
        Calcula la asignación óptima de memoria maximizando el valor computacional total
        sin exceder la capacidad estricta de memoria (max_memory).
        
        Args:
            vms (List[VirtualMachine]): Lista de las máquinas virtuales disponibles.
            max_memory (int): Capacidad máxima de memoria del servidor (W).
            
        Returns:
            Tuple[float, List[VirtualMachine]]: Una tupla que contiene:
                - El valor computacional máximo obtenible.
                - La lista de Máquinas Virtuales seleccionadas para lograr dicho valor.
        """
        n = len(vms)
        # Crear la tabla DP V[i][w] inicializada en 0.
        # Dimensiones: (n + 1) x (max_memory + 1)
        dp = [[0.0] * (max_memory + 1) for _ in range(n + 1)]
        
        # Construir la tabla DP de forma bottom-up
        for i in range(1, n + 1):
            vm = vms[i - 1]
            w_i = vm.memory
            v_i = vm.value
            
            for w in range(1, max_memory + 1):
                if w_i > w:
                    # El peso de la VM excede la capacidad residual w
                    # Recurrencia: V[i, w] = V[i-1, w]
                    dp[i][w] = dp[i - 1][w]
                else:
                    # Se evalúa la inclusión vs exclusión
                    # Recurrencia: max(V[i-1, w], V[i-1, w-wi] + vi)
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_i] + v_i)
                    
        # Recuperación de los elementos seleccionados (Backtracking sobre la tabla)
        selected_vms = []
        w = max_memory
        
        for i in range(n, 0, -1):
            # Si el valor difiere del anterior inmediato sin el elemento i, significa que el elemento i fue incluido
            if dp[i][w] != dp[i - 1][w]:
                vm = vms[i - 1]
                selected_vms.append(vm)
                w -= vm.memory  # Reducir la capacidad restante
                
        # Invertir la lista para conservar el orden de entrada (opcional)
        selected_vms.reverse()
        
        max_value = dp[n][max_memory]
        return max_value, selected_vms
