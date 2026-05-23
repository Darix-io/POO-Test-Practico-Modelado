from modelo.persona import Persona
from modelo.caja_atencion import CajaAtencion


def main():
    caja = CajaAtencion()

    p1 = Persona("Ana", "30123456")
    p2 = Persona("Bruno", "30234567")
    p3 = Persona("Carla", "30345678")
    p4 = Persona("Diego", "30456789")

    caja.agregar_persona(p1)
    caja.agregar_persona(p2)
    caja.agregar_persona(p3)
    caja.agregar_persona(p4)

    atendido_1 = caja.atender_siguiente()
    print(f"Atendido: {atendido_1}")

    atendido_2 = caja.atender_siguiente()
    print(f"Atendido: {atendido_2}")

    proximo = caja.proximo_turno()
    if proximo is None:
        print("No hay turnos esperando.")
    else:
        print(f"Siguiente en espera: {proximo}")


if __name__ == "__main__":
    main()

