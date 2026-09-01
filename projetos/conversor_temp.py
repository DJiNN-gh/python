"""Conversor de temperaturas em Python
O programa deve obter um valor qualquer, presumir que ele representa todos as três unidades de medida de temperatura e retornar o equivalente para cada uma das outras duas unidades.
Ex.: o valor 20 é passado, o programa supõe o caso 1, Celsius, e retorna o equivalente ao valor passado em Farenheit e Kelvin.
Após, o programa faz o mesmo supondo o caso 2, Farenheit, e retorn o equivalente ao valor passado em Celsius e Kelvin.Após, o programa faz o mesmo supondo o caso 3, Kelvin, e retorna o equivalente ao valor passado em Celsius e Farenheit.
Então, o programa encerra."""

def conv_celsius_para_farenheit(tempEntrada_f):
    return ((tempEntrada_f * 1.8) + 32.0)

def conv_celsius_para_kelvin(tempEntrada_f):
    return (tempEntrada_f + 273.15)

def conv_farenheit_para_celsius(tempEntrada_f):
    return ((tempEntrada_f - 32) / 1.8)

def conv_farenheit_para_kelvin(tempEntrada_f):
    return ((tempEntrada_f + 459.67) / 1.8)

def conv_kelvin_para_celsius(tempEntrada_f):
    return (tempEntrada_f - 273.15)

def conv_kelvin_para_farenheit(tempEntrada_f):
    return ((tempEntrada_f * 1.8) - 459.67)

temp_f = float(input("Insira o valor da temperatura: \n"))

print(f"Sua temperatura em Celsius: {(temp_f):.2f}")
print(f"Em Farenheit: {conv_celsius_para_farenheit(temp_f):.2f}")
print(f"Em Kelvin: {conv_celsius_para_kelvin(temp_f):.2f}")

print(f"Sua temperatura em Farenheit: {temp_f:.2f}")
print(f"Em Celsius: {conv_farenheit_para_celsius(temp_f):.2f}")
print(f"Em Kelvin: {conv_farenheit_para_kelvin(temp_f):.2f}")

print(f"Sua temperatura em Kelvin: {temp_f:.2f}")
print(f"Em Celsius: {conv_kelvin_para_celsius(temp_f):.2f}")
print(f"Em Farenheit: {conv_kelvin_para_farenheit(temp_f):.2f}")