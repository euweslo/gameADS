def dividir(valor, divisor):
    try:
        resultado = valor / divisor
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida")
        return None
    except TypeError:
        print("Erro: Os valores devem ser números")
        return None