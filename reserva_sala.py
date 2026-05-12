from clases.servicio import Servicio
from clases.excepciones import ServicioError


class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, capacidad):

        super().__init__(nombre, costo_base)

        if capacidad <= 0:
            raise ServicioError(
                "La capacidad debe ser mayor a cero"
            )

        self.capacidad = capacidad

    def calcular_costo(self, horas=1, impuesto=0):

        if horas <= 0:
            raise ServicioError(
                "Las horas deben ser mayores a cero"
            )
        subtotal= self.costo_base * horas

        total = subtotal + (subtotal * impuesto)

        return total

    def descripcion(self):

        return (
            f"Reserva de sala para "
            f"{self.capacidad} personas"
        )