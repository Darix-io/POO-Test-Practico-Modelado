from modelo.persona import Persona
from modelo.caja_atencion import CajaAtencion


def main():
    caja = CajaAtencion()

    p1 = Persona("Brito", "9548848878")
    p2 = Persona("Julia", "1125878788")
    p3 = Persona("Mateo", "1366598548")
    p4 = Persona("Ximena", "1029449484")

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

