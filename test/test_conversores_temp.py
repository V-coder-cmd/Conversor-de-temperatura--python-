import pytest
from conversores_temp import converter_temperatura 



# HAPPY PATH
def test_celsius_para_fahrenheit():
    resultado = converter_temperatura(0, "celsius", "fahrenheit")
    assert resultado == 32.0

def test_fahrenheit_para_celsius():
    resultado = converter_temperatura(32, "fahrenheit", "celsius")
    assert resultado == 0.0

def test_celsius_para_kelvin():
    resultado = converter_temperatura(0, "celsius", "kelvin")
    assert resultado == 273.15

def test_kelvin_para_celsius():
    resultado = converter_temperatura(273.15, "kelvin", "celsius")
    assert resultado == 0.00

def test_fahrenheit_para_kelvin():
    resultado = converter_temperatura(32, "fahrenheit", "kelvin")
    assert resultado == 273.15

def test_kelvin_para_fahrenheit():
    resultado = converter_temperatura(273.15, "kelvin", "fahrenheit")
    assert resultado == 32.0

# TESTES PARA TESTAR O PROGRAMA

def test_kelvin_negativo():
    with pytest.raises(ValueError, match="Temperatura em Kelvin não pode ser negativa"):
        converter_temperatura(-1, "kelvin", "celsius")

def test_escala_invalida():
    with pytest.raises(ValueError, match="Escala de temperatura inválida"):
        converter_temperatura(100, "abc", "celsius")

def test_escala_invalida_para():
    with pytest.raises(ValueError, match="Escala de temperatura inválida"):
        converter_temperatura(100, "celsius", "xyz")

def test_valor_invalido():
    with pytest.raises(ValueError):
        converter_temperatura("abc", "celsius", "fahrenheit")
