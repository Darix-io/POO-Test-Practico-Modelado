from modelo.persona import Persona


class Turno:

    def __init__(self, numero_turno: int, persona: Persona):
        self.__numero_turno = numero_turno
        self.__persona = persona

    @property
    def numero_turno(self) -> int:
        return self.__numero_turno

    @property
    def persona(self) -> Persona:
        return self.__persona

    def __str__(self) -> str:
        return f"Turno #{self.__numero_turno} - {self.__persona}"
