from models import VirtualMachine
from allocator import VMMemoryAllocator

def main():
    print("=== Crisis 2: Asignación de Memoria para Máquinas Virtuales ===")
    
    # Capacidad máxima de memoria del servidor físico (W)
    max_memory = 50
    print(f"Capacidad máxima de memoria del servidor (W): {max_memory} GB")
    
    # Definición de las Máquinas Virtuales disponibles
    vms = [
        VirtualMachine(id="VM-001", memory=10, value=60),
        VirtualMachine(id="VM-002", memory=20, value=100),
        VirtualMachine(id="VM-003", memory=30, value=120),
        VirtualMachine(id="VM-004", memory=15, value=75),
        VirtualMachine(id="VM-005", memory=5,  value=40)
    ]
    
    print("\nMáquinas Virtuales Disponibles:")
    for vm in vms:
        print(f" - {vm.id}: {vm.memory} GB de RAM | Valor: {vm.value}")
        
    print("\nEjecutando algoritmo de Programación Dinámica (0/1 Knapsack)...")
    
    # Llamamos al allocator para maximizar el valor
    max_value, selected_vms = VMMemoryAllocator.allocate(vms, max_memory)
    
    # Mostramos los resultados
    print("\n=== Resultados de la Asignación ===")
    print(f"Valor computacional total (Máximo): {max_value}")
    
    print("Máquinas Virtuales seleccionadas para el servidor:")
    total_memory_used = 0
    for vm in selected_vms:
        print(f" -> {vm.id} (Memoria: {vm.memory} GB, Valor: {vm.value})")
        total_memory_used += vm.memory
        
    print(f"\nMemoria total utilizada: {total_memory_used} GB / {max_memory} GB")
    print(f"Memoria residual disponible: {max_memory - total_memory_used} GB")

if __name__ == '__main__':
    main()
