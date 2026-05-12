from clases.servicio import Servicio
from clases.excepciones import ServicioError


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, tipo_equipo):

        super().__init__(nombre, costo_base)

        if not tipo_equipo:
            raise ServicioError(
                "Tipo de equipo inválido"
            )

        self.tipo_equipo = tipo_equipo
    def calcular_costo(self, dias=1, descuento=0):

        if dias <= 0:
            raise ServicioError(
                "Los días deben ser mayores a cero"
            )

        subtotal = self.costo_base * dias

        total = subtotal - (subtotal * descuento)

        return total
    def descripcion(self):

        return (
            f"Alquiler de equipos tipo "
            f"{self.tipo_equipo}"
        )