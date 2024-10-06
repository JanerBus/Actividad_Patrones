from abc import ABC, abstractmethod

class Documento(ABC):
    @abstractmethod
    def clonar(self):
        pass

    @abstractmethod
    def editar_contenido(self, nuevo_contenido):
        pass

class CurriculumVitae(Documento):
    def __init__(self, nombre, experiencia):
        self.nombre = nombre
        self.experiencia = experiencia

    def clonar(self):
        return CurriculumVitae(self.nombre, self.experiencia.copy())

    def editar_contenido(self, nuevo_contenido):
        # Lógica para actualizar el contenido del currículum
        pass

# Similarmente, se definirían las clases CartaPresentacion e Informe

class EditorDocumentos:
    def __init__(self):
        self.plantillas = {
            "curriculum": CurriculumVitae("John Doe", []),
            "carta": CartaPresentacion(),
            # ...
        }

    def crear_nuevo_documento(self, tipo_plantilla):
        plantilla = self.plantillas.get(tipo_plantilla)
        if plantilla:
            return plantilla.clonar()
        else:
            raise ValueError("Plantilla no encontrada")
