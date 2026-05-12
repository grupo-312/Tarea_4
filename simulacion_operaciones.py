import utils.logger_config

from clases.cliente import Cliente
from clases.reserva_sala import ReservaSala
from clases.alquiler_equipo import AlquilerEquipo
from clases.asesoria_especializada import AsesoriaEspecializada
from clases.reserva import Reserva

from clases.excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)


clientes = []
servicios = []
reservas = []


def simular_operaciones():

    print("\n========= SOFTWARE FJ =========\n")

    # --------------------------------------------------
    # OPERACIÓN 1
    # CLIENTE VÁLIDO
    # --------------------------------------------------

    try:

        cliente1 = Cliente(
            "Daniel parra",
            "12345",
            "daniel@gmail.com"
        )

        clientes.append(cliente1)

        print("Cliente registrado correctamente")

    except ClienteError as e:

        print(f"ERROR CLIENTE: {e}")

    # --------------------------------------------------
    # OPERACIÓN 2
    # CLIENTE VÁLIDO
    # --------------------------------------------------

    try:

        cliente2 = Cliente(
            "Lorena Salazar",
            "67890",
            "lorena@gmail.com"
        )

        clientes.append(cliente2)

        print("Cliente registrado correctamente")

    except ClienteError as e:

        print(f"ERROR CLIENTE: {e}")

    # --------------------------------------------------
    # OPERACIÓN 3
    # CLIENTE INVÁLIDO
    # --------------------------------------------------

    try:

        cliente_error = Cliente(
            "",
            "abc",
            "correo_malo"
        )

    except ClienteError as e:

        print(f"ERROR CLIENTE: {e}")

    # --------------------------------------------------
    # OPERACIÓN 4
    # SERVICIO VÁLIDO
    # --------------------------------------------------

    try:

        sala1 = ReservaSala(
            "Sala Premium",
            50000,
            20
        )

        servicios.append(sala1)

        print("Servicio registrado")

    except ServicioError as e:

        print(f"ERROR SERVICIO: {e}")

    # --------------------------------------------------
    # OPERACIÓN 5
    # SERVICIO VÁLIDO
    # --------------------------------------------------

    try:

        equipo1 = AlquilerEquipo(
            "Alquiler Laptop",
            80000,
            "Laptop"
        )

        servicios.append(equipo1)

        print("Servicio registrado")

    except ServicioError as e:

        print(f"ERROR SERVICIO: {e}")

    # --------------------------------------------------
    # OPERACIÓN 6
    # SERVICIO VÁLIDO
    # --------------------------------------------------

    try:

        asesoria1 = AsesoriaEspecializada(
            "Asesoría IA",
            120000,
            "Inteligencia Artificial"
        )

        servicios.append(asesoria1)

        print("Servicio registrado")

    except ServicioError as e:

        print(f"ERROR SERVICIO: {e}")

    # --------------------------------------------------
    # OPERACIÓN 7
    # SERVICIO INVÁLIDO
    # --------------------------------------------------

    try:

        servicio_error = ReservaSala(
            "Sala Incorrecta",
            10000,
            -5
        )

    except ServicioError as e:

        print(f"ERROR SERVICIO: {e}")

    # --------------------------------------------------
    # OPERACIÓN 8
    # RESERVA EXITOSA
    # --------------------------------------------------

    try:

        reserva1 = Reserva(
            cliente1,
            sala1,
            3
        )

        reservas.append(reserva1)

        reserva1.confirmar()

        valor = reserva1.procesar_pago()

        print(
            reserva1.mostrar_reserva()
        )

        print(f"Valor pagado: ${valor}")

    except ReservaError as e:

        print(f"ERROR RESERVA: {e}")

    # --------------------------------------------------
    # OPERACIÓN 9
    # RESERVA INVÁLIDA
    # --------------------------------------------------

    try:

        reserva_error = Reserva(
            cliente1,
            sala1,
            -1
        )

    except ReservaError as e:

        print(f"ERROR RESERVA: {e}")

    # --------------------------------------------------
    # OPERACIÓN 10
    # EXCEPCIÓN CONTROLADA
    # --------------------------------------------------

    try:

        reserva2 = Reserva(
            cliente1,
            sala1,
            1
        )

        reserva2.cancelar()

        reserva2.confirmar()

    except ReservaError as e:

        print(f"ERROR CONTROLADO: {e}")

    # --------------------------------------------------
    # MOSTRAR RESULTADOS
    # --------------------------------------------------

    print("\n========= CLIENTES =========\n")

    for cliente in clientes:

        print(
            cliente.mostrar_informacion()
        )

    print("\n========= SERVICIOS =========\n")

    for servicio in servicios:

        print(
            servicio.descripcion()
        )

    print("\n========= RESERVAS =========\n")

    for reserva in reservas:

        print(
            reserva.mostrar_reserva()
        )


simular_operaciones()
