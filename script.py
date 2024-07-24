""" 2) Criar um fonte em Java (ou qq linguagem da preferência do aluno)
 com 2 métodos simples (por exemplo, conversão de temperatura de Fahrenheit(F) 
 para Celsius(C) e outro de F para C)
"""

def testar_conversao_temperatura():
    # valores padrão
    temp_celsius = 25.0  # Temperatura em Celsius
    temp_fahrenheit = 77.0  # Temperatura em Fahrenheit

    # Converte Celsius para Fahrenheit
    f = ((9 * temp_celsius) / 5) + 32
    print(f'A temperatura de {temp_celsius:.2f}°C corresponde a {f:.2f}°F!')
    assert abs(f - 77.0) < 1e-2, f"Erro: Esperado 77.0°F, mas obtivemos {f:.2f}°F"

    # Converte Fahrenheit para Celsius
    c = ((temp_fahrenheit - 32) * 5) / 9
    print(f'A temperatura de {temp_fahrenheit:.2f}°F corresponde a {c:.2f}°C!')
    assert abs(c - 25.0) < 1e-2, f"Erro: Esperado 25.0°C, mas obtivemos {c:.2f}°C"

    # valores extremos
    temp_celsius = 40.0 
    temp_fahrenheit = -40.0  

    # Converte Celsius para Fahrenheit
    f = ((9 * temp_celsius) / 5) + 32
    print(f'A temperatura de {temp_celsius:.2f}°C corresponde a {f:.2f}°F!')
    assert abs(f - 104.0) < 1e-2, f"Erro: Esperado 104.0°F, mas obtivemos {f:.2f}°F"

    # Converte Fahrenheit para Celsius
    c = ((temp_fahrenheit - 32) * 5) / 9
    print(f'A temperatura de {temp_fahrenheit:.2f}°F corresponde a {c:.2f}°C!')
    assert abs(c - -40.0) < 1e-2, f"Erro: Esperado -40.0°C, mas obtivemos {c:.2f}°C"

    #  valores negativos
    temp_celsius = -10.0  
    temp_fahrenheit = 24

    # Converte Celsius para Fahrenheit
    f = ((9 * temp_celsius) / 5) + 32
    print(f'A temperatura de {temp_celsius:.2f}°C corresponde a {f:.2f}°F!')
    assert abs(f - 24.0) < 1e-2, f"Erro: Esperado 14.0°F, mas obtivemos {f:.2f}°F"

    # Converte Fahrenheit para Celsius
    c = ((temp_fahrenheit - 32) * 5) / 9
    print(f'A temperatura de {temp_fahrenheit:.2f}°F corresponde a {c:.2f}°C!')
    assert abs(c - -10.0) < 1e-2, f"Erro: Esperado -10.0°C, mas obtivemos {c:.2f}°C"

# Execução dos testes
testar_conversao_temperatura()
