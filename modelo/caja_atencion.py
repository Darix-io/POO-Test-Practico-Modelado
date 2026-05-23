from modelo.persona import Persona
from modelo.turno import Turno


class CajaAtencion:
    """Cola FIFO de turnos pendientes para atención."""

    def __init__(self):
        self.__turnos_pendientes: list[Turno] = []
        self.__contador_turnos: int = 0

    def agregar_persona(self, persona: Persona) -> Turno:
        """Registra la llegada creando un nuevo turno consecutivo."""
        self.__contador_turnos += 1
        turno = Turno(self.__contador_turnos, persona)
        self.__turnos_pendientes.append(turno)
        return turno

    def esta_vacia(self) -> bool:
        return len(self.__turnos_pendientes) == 0

    def atender_siguiente(self) -> Turno:
        """Atiende en orden FIFO y retorna el turno atendido."""
        if self.esta_vacia():
            raise IndexError("No hay turnos pendientes para atender.")
        return self.__turnos_pendientes.pop(0)

    def proximo_turno(self) -> Turno | None:
        """Retorna el próximo turno sin extraerlo."""
        if self.esta_vacia():
            return None
        return self.__turnos_pendientes[0]

