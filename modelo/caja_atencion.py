from modelo.persona import Persona
from modelo.turno import Turno


class CajaAtencion:

    def __init__(self):
        self.__turnos_pendientes: list[Turno] = []
        self.__contador_turnos: int = 0

    def agregar_persona(self, persona: Persona) -> Turno:
        self.__contador_turnos += 1
        turno = Turno(self.__contador_turnos, persona)
        self.__turnos_pendientes.append(turno)
        return turno

    def esta_vacia(self) -> bool:
        return len(self.__turnos_pendientes) == 0

    def atender_siguiente(self) -> Turno:
        if self.esta_vacia():
            raise IndexError("No hay turnos pendientes para atender.")
        return self.__turnos_pendientes.pop(0)

    def proximo_turno(self) -> Turno | None:
        if self.esta_vacia():
            return None
        return self.__turnos_pendientes[0]

