from clases.servicio import Servicio
from clases.excepciones import ServicioError


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, costo_base, especialidad):

        super().__init__(nombre, costo_base)

        if not especialidad:
            raise ServicioError(
                "Especialidad inválida"
            )

        self.especialidad = especialidad
    def calcular_costo(self, sesiones=1, recargo=0):

        if sesiones <= 0:
            raise ServicioError(
                "Las sesiones deben ser mayores a cero"
            )

        subtotal = self.costo_base * sesiones

        total = subtotal + recargo

        return total
    def descripcion(self):

        return (
            f"Asesoría especializada en "
            f"{self.especialidad}"
        )