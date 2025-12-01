#!/usr/bin/env pybricks-micropython
"""
main.py - Teste simples do Binho
Para pybricks-micropython
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
import math

# =============================================================================
# CONFIGURAÇÕES - AJUSTE AQUI
# =============================================================================

# Medidas físicas (meça com régua!)
WHEEL_DIAMETER_MM = 30      # Diâmetro da roda em milímetros
WHEELBASE_MM = 142          # Distância entre as rodas em milímetros

# Fatores de correção (ajuste testando)
LINEAR_CORRECTION = 0.54     # Aumente se andar menos que o esperado
ROTATION_CORRECTION = 0.585   # Aumente se girar menos que o esperado

# Velocidade (graus por segundo)
SPEED = 100                 # 100 = devagar, 500 = rápido

# =============================================================================
# INICIALIZAÇÃO
# =============================================================================

# Inicializa o brick
ev3 = EV3Brick()

# Inicializa motores
motor_left = Motor(Port.D)
motor_right = Motor(Port.A)

ev3.speaker.beep()
print("Binho pronto!")

# =============================================================================
# FUNÇÕES BÁSICAS
# =============================================================================

def andar_mm(distancia):
    """Anda X milímetros para frente (ou para trás se negativo)"""
    circunferencia = math.pi * WHEEL_DIAMETER_MM
    graus_motor = (distancia / circunferencia) * 360 * LINEAR_CORRECTION

    motor_left.run_angle(SPEED, graus_motor, wait=False)
    motor_right.run_angle(SPEED, graus_motor, wait=True)

def andar_cm(distancia):
    """Anda X centímetros para frente"""
    andar_mm(distancia * 10)

def girar_graus(angulo):
    """Gira X graus (positivo = direita, negativo = esquerda)"""
    arco = (WHEELBASE_MM * math.pi * abs(angulo)) / 360
    circunferencia = math.pi * WHEEL_DIAMETER_MM
    graus_motor = (arco / circunferencia) * 360 * ROTATION_CORRECTION

    if angulo > 0:  # Direita
        motor_left.run_angle(SPEED, graus_motor, wait=False)
        motor_right.run_angle(SPEED, -graus_motor, wait=True)
    else:  # Esquerda
        motor_left.run_angle(SPEED, -graus_motor, wait=False)
        motor_right.run_angle(SPEED, graus_motor, wait=True)

def esperar(segundos):
    """Pausa em segundos"""
    wait(int(segundos * 1000))

# =============================================================================
# TESTES 
# =============================================================================

def teste_linha():
    """Desenha linha reta de 20cm - meça depois!"""
    print("Teste: linha de 20cm")
    ev3.speaker.beep()
    esperar(2)

    andar_cm(20)

    ev3.speaker.beep()
    print("Pronto! Meça a linha com régua")

def teste_quadrado():
    """Desenha quadrado de 10x10cm"""
    print("Teste: quadrado 10x10cm")
    ev3.speaker.beep()
    esperar(2)

    for i in range(4):
        print("Lado " + str(i+1))
        andar_cm(10)
        girar_graus(90)

    ev3.speaker.beep()
    print("Pronto! Veja se fechou certinho")

def teste_triangulo():
    """Desenha triângulo"""
    print("Teste: triângulo")
    ev3.speaker.beep()
    esperar(2)

    for i in range(3):
        andar_cm(10)
        girar_graus(120)

    ev3.speaker.beep()
    print("Triângulo feito!")

def teste_letra_L():
    """Desenha um L"""
    print("Teste: letra L")
    ev3.speaker.beep()
    esperar(2)

    andar_cm(10)      # Linha vertical
    girar_graus(-90)  # Vira para esquerda
    andar_cm(8)       # Linha horizontal

    ev3.speaker.beep()
    print("L desenhado!")

def teste_letra_O():
    """Desenha um O (círculo em segmentos)"""
    print("Teste: letra O")
    ev3.speaker.beep()
    esperar(2)

    # Círculo = 36 passos pequenos de 10 graus cada
    for i in range(36):
        andar_mm(8.7) 
        girar_graus(10) # Gira 10 graus

    ev3.speaker.beep()
    print("O desenhado!")

def teste_letra_I():
    """Desenha um I"""
    print("Teste: letra I")
    ev3.speaker.beep()
    esperar(2)

    # Barra superior
    andar_cm(3)
    andar_cm(-1.5)

    # Barra vertical
    girar_graus(-90)
    andar_cm(10)

    # Barra inferior
    girar_graus(90)
    andar_cm(-1.5)
    andar_cm(3)

    ev3.speaker.beep()
    print("I desenhado!")

def teste_zigue_zague():
    """Desenha zigue-zague"""
    print("Teste: zigue-zague")
    ev3.speaker.beep()
    esperar(2)

    for i in range(4):
        andar_cm(5)
        girar_graus(60)
        andar_cm(5)
        girar_graus(-60)

    ev3.speaker.beep()
    print("Zigue-zague feito!")

def teste_estrela():
    """Desenha uma estrela de 5 pontas"""
    print("Teste: estrela")
    ev3.speaker.beep()
    esperar(2)

    for i in range(5):
        andar_cm(10)
        girar_graus(144)  # 144 graus para estrela de 5 pontas

    ev3.speaker.beep()
    print("Estrela feita!")

# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================

esperar(1)

#teste_linha() 
#teste_quadrado()
#teste_triangulo()
#teste_letra_L()
#teste_letra_O()
#teste_letra_I()
#teste_zigue_zague()
teste_estrela()

# Finaliza
print("Fim!")
ev3.speaker.beep()
wait(300)
ev3.speaker.beep()