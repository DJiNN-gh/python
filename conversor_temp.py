"""Conversor de temperaturas em Python
O programa deve obter um valor qualquer, presumir que ele representa todos as três unidades de medida de temperatura e retornar o equivalente para cada uma das outras duas unidades.
Ex.: o valor 20 é passado, o programa supõe o caso 1, Celsius, e retorna o equivalente ao valor passado em Farenheit e Kelvin.
Após, o programa faz o mesmo supondo o caso 2, Farenheit, e retorn o equivalente ao valor passado em Celsius e Kelvin.Após, o programa faz o mesmo supondo o caso 3, Kelvin, e retorna o equivalente ao valor passado em Celsius e Farenheit.
Então, o programa encerra."""

def convCelsiusParaFarenheit(tempEntrada_f):
    return ((tempEntrada_f * 1.8) + 32.0)

def convCelsiusParaKelvin(tempEntrada_f):
    return (tempEntrada_f + 273.15)

def convFarenheitParaCelsius(tempEntrada_f):
    return ((tempEntrada_f - 32) / 1.8)

def convFarenheitParaKelvin(tempEntrada_f):
    return ((tempEntrada_f + 459.67) / 1.8)

def convKelvinParaCelsius(tempEntrada_f):
    return (tempEntrada_f - 273.15)

def convKelvinParaFarenheit(tempEntrada_f):
    return ((tempEntrada_f * 1.8) - 459.67)

temp_f = float(input("Insira o valor da temperatura: " ))

print("\n")

print("Sua temperatura em Celsius: ", round(temp_f, 2))
print("Em Farenheit: ", round(convCelsiusParaFarenheit(temp_f), 2))
print("Em Kelvin: ", round(convCelsiusParaKelvin(temp_f), 2))

print("\n")

print("Sua temperatura em Farenheit: ", round(temp_f, 2))
print("Em Celsius: ", round(convFarenheitParaCelsius(temp_f), 2))
print("Em Kelvin: ", round(convFarenheitParaKelvin(temp_f), 2))

print("\n")

print("Sua temperatura em Kelvin: ", round(temp_f, 2))
print("Em Celsius: ", round(convKelvinParaCelsius(temp_f), 2))
print("Em Farenheit: ", round(convKelvinParaFarenheit(temp_f), 2))

print("\n")