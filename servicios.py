from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod
    def descripcion(self):
        pass