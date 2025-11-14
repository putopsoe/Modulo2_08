# Ejercicio 1 - Manejo de excepción específica (ZeroDivisionError)
# Enunciado original: "numero = 7/0" (división por cero)
# Objetivo: identificar la excepción concreta y manejarla mostrando un mensaje
# explicativo para el usuario en lugar de dejar que el programa se bloquee.

def safe_divide(numerator, denominator):
    """Divide numerator entre denominator manejando errores concretos.

    Devuelve None si hay un error y muestra un mensaje explicativo.
    """
    try:
        resultado = numerator / denominator
    except ZeroDivisionError:
        print("Error: división por cero. No se puede dividir entre 0. Por favor, proporciona un divisor distinto de 0.")
        return None
    except TypeError:
        print("Error: tipos inválidos para la división. Asegúrate de pasar números (int o float).")
        return None
    else:
        return resultado


if __name__ == "__main__":
    # Caso problemático del enunciado
    print("Caso enunciado: 7 / 0")
    r = safe_divide(7, 0)
    print("Resultado devuelto:", r)
    print()

    # Caso correcto para verificar comportamiento
    print("Caso válido: 10 / 2")
    r2 = safe_divide(10, 2)
    print("Resultado devuelto:", r2)
    print()

    # Caso de tipo inválido
    print("Caso tipo inválido: '2' + 10 (intento de dividir con tipo incorrecto)")
    r3 = safe_divide("2", 10)
    print("Resultado devuelto:", r3)
