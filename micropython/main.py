# ---------------------------
# Código EV3 MicroPython — Escrita de Letras
# ---------------------------
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
import math

# ---------------------------
# CONFIGURAÇÃO
# ---------------------------
ev3 = EV3Brick()

# Motores (ajuste conforme solicitado)
motor_esq = Motor(Port.A)   # roda esquerda -> Porta 1
motor_dir = Motor(Port.D)   # roda direita -> Porta 4

# Geometria do robô (em cm)
L = 19.0          # distância entre rodas (cm)
circ_roda = 15.7  # circunferência da roda (cm)

# Posição da caneta (em cm)
p_caneta_x = 2.0
p_caneta_y = -7.0

# ---------------------------
# FUNÇÕES BÁSICAS
# ---------------------------
def cm_para_graus_roda(dist_cm):
    """Converte distância (cm) em graus da roda."""
    return (dist_cm / circ_roda) * 360.0

def enviar_comando(dist_esq_cm, dist_dir_cm, velocidade=200):
    """Movimenta as rodas com distâncias em cm."""
    deg_esq = cm_para_graus_roda(dist_esq_cm)
    deg_dir = cm_para_graus_roda(dist_dir_cm)
    motor_esq.run_angle(velocidade, deg_esq, Stop.BRAKE, False)
    motor_dir.run_angle(velocidade, deg_dir, Stop.BRAKE, True)

def mover_frente(dist_cm, velocidade=200):
    enviar_comando(dist_cm, dist_cm, velocidade)

def mover_tras(dist_cm, velocidade=200):
    enviar_comando(-dist_cm, -dist_cm, velocidade)

def girar_com_compensacao(angulo_graus, passos=40, velocidade=180):
    """
    Gira o robô de 'angulo_graus' mantendo o ponto da caneta aproximadamente fixo.
    """
    total_theta = math.radians(angulo_graus)
    sinal = 1.0 if total_theta >= 0 else -1.0
    total_theta = abs(total_theta)
    dtheta = total_theta / passos
    L_m = L

    for _ in range(passos):
        delta_s = dtheta * p_caneta_y
        dl = delta_s - (L_m / 2.0) * dtheta
        dr = delta_s + (L_m / 2.0) * dtheta
        if sinal < 0:
            dl, dr = -dl, -dr
        enviar_comando(dl, dr, velocidade)

# ---------------------------
# LETRAS
# ---------------------------
def letra_A():
    mover_frente(8)
    girar_com_compensacao(135)
    mover_frente(5.6)
    mover_tras(5.6)
    girar_com_compensacao(-270)
    mover_frente(5.6)
    girar_com_compensacao(135)
    mover_frente(8)
    girar_com_compensacao(90)
    mover_frente(4)
    girar_com_compensacao(90)
    mover_frente(3)
    girar_com_compensacao(180)
    mover_frente(3)
    girar_com_compensacao(90)
    mover_frente(4)
    girar_com_compensacao(-90)

def letra_B():
    mover_frente(8)
    girar_com_compensacao(90)
    mover_frente(3)
    girar_com_compensacao(90)
    mover_frente(4)
    girar_com_compensacao(90)
    mover_frente(3)
    girar_com_compensacao(-180)
    mover_frente(3)
    girar_com_compensacao(90)
    mover_frente(4)
    girar_com_compensacao(90)
    mover_frente(3)
    girar_com_compensacao(90)

def letra_C():
    girar_com_compensacao(180)
    mover_frente(8)
    girar_com_compensacao(-90)
    mover_frente(5)
    girar_com_compensacao(-90)
    mover_frente(8)
    girar_com_compensacao(180)

def letra_L():
    mover_frente(8)
    girar_com_compensacao(90)
    mover_frente(5)
    girar_com_compensacao(90)

def letra_O():
    for _ in range(4):
        mover_frente(6)
        girar_com_compensacao(90)

# ---------------------------
# EXEMPLO DE USO
# ---------------------------
def escrever_nome():
    """Exemplo: desenhar L, O, B"""
    letra_L()
    mover_frente(2)
    letra_O()
    mover_frente(2)
    letra_B()

# ---------------------------
# EXECUÇÃO
# ---------------------------
escrever_nome()