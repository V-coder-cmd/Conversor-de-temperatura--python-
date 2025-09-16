def converter_temperatura(valor, de_escala, para_escala):

    try:
        valor = float(valor)
    
    except:
        raise ValueError("O valor da temperatura deve ser numérico")


    de = de_escala.upper()
    para = para_escala.upper()

    escalas_validas = {"CELSIUS", "KELVIN", "FAHRENHEIT"}

    if de not in escalas_validas or para not in escalas_validas:
        raise ValueError("Escala de temperatura inválida")
    
    if de == "KELVIN" and valor < 0:
        raise ValueError("Temperatura em Kelvin não pode ser negativa")
    
    if de == para:
        return float(valor)
    
    if de == "KELVIN":
        celsius = valor - 273.15
    
    elif de == "FAHRENHEIT":
        celsius = (valor - 32) / 1.8

    else:
        celsius = valor
    
    if para == "KELVIN":
        resultado = celsius + 273.15
    
    elif para == "FAHRENHEIT":
        resultado = celsius * 1.8 + 32

    else:
        resultado = celsius

    return round(resultado, 2)


print(converter_temperatura(32, "fahrenheit", "kelvin"))
print(converter_temperatura(32, "kelvin", "fahrenheit"))
print(converter_temperatura(32, "celsius", "kelvin"))
print(converter_temperatura(32, "kelvin", "celsius"))