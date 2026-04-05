from abc import ABC, abstractmethod

class Gestion_vehiculos(ABC):
    def __init__(self, nombre_sucursal):
        self.vehiculos = []
        self.nombre_sucursal = nombre_sucursal

    @abstractmethod
    def agregar_vehiculo(self, vehiculo):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def mostrar_info_sistema(self):
        pass

class RegistroMantenimiento:
    def __init__(self, ultima_fecha):
        self.ultima_fecha = ultima_fecha
    
    def obtener_mantenimiento(self):
        return f"Revision: {self.ultima_fecha}"

class ControlSeguro:
    def __init__(self, numero_poliza):
        self.numero_poliza = numero_poliza
    
    def verificar_seguro(self):
        return f"Seguro ID: {self.numero_poliza}"

class VehiculoFinal(Gestion_vehiculos, RegistroMantenimiento, ControlSeguro):
    def __init__(self, sucursal, fecha, poliza, placa, kilometraje):
        Gestion_vehiculos.__init__(self, sucursal)
        RegistroMantenimiento.__init__(self, fecha)
        ControlSeguro.__init__(self, poliza)
        
        self.placa = placa
        self.kilometraje = kilometraje

    @property
    def kilometraje(self):
        return self.kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if valor >= self.kilometraje:
            self.kilometraje = valor
        else:
            print("Error: Valor de kilometraje invalido")

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        return f"Unidad {vehiculo} registrada"

    def __str__(self):
        return f"Vehiculo: {self.__placa} | Sucursal: {self.nombre_sucursal}"

    def mostrar_info_sistema(self):
        return f"Status: {self.obtener_mantenimiento()} | {self.verificar_seguro()}"

if __name__ == "__main__":
    v1 = VehiculoFinal("Sede Norte", "2026-04-01", "POL-882", "GUJ-123", 4500)
    v2 = VehiculoFinal("Sede Sur", "2026-03-15", "POL-991", "MAI-456", 12800)
    v3 = VehiculoFinal("Sede Riohacha", "2026-04-02", "POL-102", "UNU-789", 0)

    print(v1.agregar_vehiculo("Bus Intermunicipal"))
    print(v1)
    print(v1.mostrar_info_sistema())

    print(f"Lectura protegida: {v1.kilometraje}")
    v1.kilometraje = 4600
    print(f"Cambio aplicado: {v1.kilometraje}")
    
    v1.kilometraje = 2000