import pytest
from conversores_temp import converter_temperatura
# from conversores_temp import converter_temperatura 



# # HAPPY PATH
# def test_celsius_para_fahrenheit():
#     resultado = converter_temperatura(0, "celsius", "fahrenheit")
#     assert resultado == 32.0

# def test_fahrenheit_para_celsius():
#     resultado = converter_temperatura(32, "fahrenheit", "celsius")
#     assert resultado == 0.0

# def test_celsius_para_kelvin():
#     resultado = converter_temperatura(0, "celsius", "kelvin")
#     assert resultado == 273.15

# def test_kelvin_para_celsius():
#     resultado = converter_temperatura(273.15, "kelvin", "celsius")
#     assert resultado == 0.00

# def test_fahrenheit_para_kelvin():
#     resultado = converter_temperatura(32, "fahrenheit", "kelvin")
#     assert resultado == 273.15

# def test_kelvin_para_fahrenheit():
#     resultado = converter_temperatura(273.15, "kelvin", "fahrenheit")
#     assert resultado == 32.0

# # TESTES PARA TESTAR O PROGRAMA
# def test_kelvin_negativo():
#     with pytest.raises(ValueError, match="Temperatura em Kelvin não pode ser negativa"):
#         converter_temperatura(-1, "kelvin", "celsius")

# def test_escala_invalida():
#     with pytest.raises(ValueError, match="Escala de temperatura inválida"):
#         converter_temperatura(100, "abc", "celsius")

# def test_escala_invalida_para():
#     with pytest.raises(ValueError, match="Escala de temperatura inválida"):
#         converter_temperatura(100, "celsius", "xyz")

# def test_valor_invalido():
#     with pytest.raises(ValueError):
#         converter_temperatura("abc", "celsius", "fahrenheit")


# -----Mesma coisa só que com parametrize()-----#
 

# HAPPY PATH

@pytest.mark.parametrize("valor, de_escala, para_escala, esperado",
                         [
                             (32, "KELVIN", "CELSIUS", -241.15),
                             (32, "KELVIN", "FAHRENHEIT", -402.07),
                             (32, "KELVIN", "KELVIN", 32),
                             (32, "kelvin", "celsius", -241.15),
                             (32, "CelsiuS", "FahRENhEiT", 89.6),
                             (32, "CELSIUS", "KELVIN", 305.15),
                             (32, "CELSIUS", "FAHRENHEIT", 89.6),
                             (32, "CELSIUS", "CELSIUS", 32),
                             (32, "FAHRENHEIT", "KELVIN", 273.15),
                             (32, "FAHRENHEIT", "CELSIUS", 0),
                             (32, "FAHRENHEIT", "FAHRENHEIT", 32)
                         ], 
                         ids = ["KELVIN PARA CELSIUS", "KELVIN PARA FAHRENHEIT", "KELVIN PARA KELVIN", "ESCALA MINÚSCULA",
                                "ESCALA EM MAIÚSCULA", "CELSIUS PARA KELVIN", "CELSIUS PARA FAHRENHEIT", "CELSIUS PARA CELSIUS",
                                "FAHRENHEIT PARA KELVIN", "FAHRENHEIT PARA CELSIUS", "FAHRENHEIT PARA FAHRENHEIT"]
                         )

def test_converter_temperatura_happpath(valor, de_escala, para_escala, esperado):
    resultado = converter_temperatura(valor, de_escala, para_escala)
    assert round(resultado, 2) == pytest.approx(esperado,0.1)