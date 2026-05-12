from datetime import datetime
import logging

from clases.cliente import Cliente
from clases.servicio import Servicio
from clases.excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if not isinstance(cliente, Cliente):
            raise ReservaError("Cliente inválido")

        if not isinstance(servicio, Servicio):
            raise ReservaError("Servicio inválido")

        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.fecha = datetime.now()

    def confirmar(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "No se puede confirmar una reserva cancelada"
                )

            self.estado = "Confirmada"

            logging.info(
                f"Reserva confirmada para {self.cliente.nombre}"
            )

        except ReservaError as e:

            logging.error(str(e))
            raise

    def cancelar(self):

        try:

            if self.estado == "Confirmada":
                raise ReservaError(
                    "No se puede cancelar una reserva confirmada"
                )

            self.estado = "Cancelada"

            logging.info(
                f"Reserva cancelada para {self.cliente.nombre}"
            )

        except ReservaError as e:

            logging.error(str(e))
            raise

    def procesar_pago(self):

        try:

            costo = self.servicio.calcular_costo(
                self.duracion
            )

        except Exception as e:

            logging.error(
                "Error procesando pago"
            )

            raise ReservaError(
                "No fue posible procesar el pago"
            ) from e

        else:

            logging.info(
                f"Pago procesado correctamente: ${costo}"
            )

            return costo

        finally:

            logging.info(
                "Finalizó proceso de pago"
            )

    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} | "
            f"Estado: {self.estado}"
        )
