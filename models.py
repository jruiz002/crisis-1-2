from dataclasses import dataclass

@dataclass
class VirtualMachine:
    """
    Representa una Máquina Virtual (VM) en el centro de datos.
    
    Atributos:
        id (str): Identificador único de la VM.
        memory (int): Capacidad de memoria requerida (peso, w_i).
        value (float): Valor computacional o rentabilidad (v_i).
    """
    id: str
    memory: int
    value: float
