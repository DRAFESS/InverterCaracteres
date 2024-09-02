def inverter_string(s):
    s_invertida = ""
    for caractere in s:
        s_invertida = caractere + s_invertida
    return s_invertida

entrada = input("Digite a string a ser invertida: ")

resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")


def inverter_string(s):
    s_invertida = ""
    for caractere in s:
        s_invertida = caractere + s_invertida
    return s_invertida

entrada = "Exemplo de string"

resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
