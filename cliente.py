from clases.entidad import Entidad
from clases.excepciones import ClienteError
class Cliente(Entidad):
    def _init_(self, nombre, documento, correo):
        self._nombre=None
        self._documento=None
        self._correo=None
        self.nombre=nombre
        self.documento=documento
        self.correo=correo
        @property
        def nombre(self):
            return self._nombre
        @nombre.setter
        def nombre(self, valor):
            if not valor or len(valor.strip()) <3:
                raise ClienteError("Nombre invalido")
            self._nombre=valor
        @property
        def documento(self):
            return self._documento
        @documento.setter
        def documento(self, valor):
            if not str(valor).isdigit():
                raise ClienteError("Documento invalido")
            self._documento=valor
        @property
        def correo (self):
            return self._correo
        @correo.setter
        def correo(self, valor):
            if "@" not in valor:
                raise ClienteError("Correo invalido")  
            self._correo=valor
        def mostrar_informacion(self):
            return (
            f"Cliente: {self.nombre} | "
            f"Documento: {self.documento} | "
            f"Correo: {self.correo}"
        )      
