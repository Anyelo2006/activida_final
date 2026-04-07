from abc import ABC, abstractmethod
class ProcesadorRender(ABC):
    def __init__(self, nombre_proyec):
        
        self.__nombre_proyec = nombre_proyec 
        self.__estado = "Esperando"

    @abstractmethod
    def ejecutar_proceso(self):
        
        pass

    def obtener_nombre(self):
        return self.__nombre_proyec


class MejorarCalidadMixin:
    def aplicar_filtro(self):
        return "Aplicando filtros de alta resolucion a los frames..."

class AlertaCloudMixin:
    def enviar_aviso(self):
        return "Enviando correo: El video ya esta listo!"


class RenderFinal(ProcesadorRender, MejorarCalidadMixin, AlertaCloudMixin):
    def __init__(self, nombre_proyec, frames_totales):
        super().__init__(nombre_proyec)
        
        self.__frames = frames_totales 

    def ejecutar_proceso(self):
        return f"Procesando {self.__frames} imagenes del proyecto {self.obtener_nombre()}"

    
    @property
    def cantidad_frames(self):
        return self.__frames

    @cantidad_frames.setter
    def cantidad_frames(self, nuevo_valor):
        if nuevo_valor > 0:
            self.__frames = nuevo_valor
        else:
            print("ERROR TECNICO: Cantidad de frames no valida para el motor")
    def __str__(self):
        return f"Render: {self.obtener_nombre()} | Frames: {self.__frames}"

if __name__ == "__main__":
    mi_trabajo = RenderFinal("Video_Final_Uniguajira", 120)

    print(mi_trabajo.ejecutar_proceso())
    print(mi_trabajo.aplicar_filtro()) 
    

    mi_trabajo.cantidad_frames = 250 
    mi_trabajo.cantidad_frames = -5 
    
    print(mi_trabajo)