#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)

def beep():
    ev3.speaker.beep()

def andar(dist_cm, velocity=200):
    CIRC = 17.6
    graus = (dist_cm / CIRC) * 360
    left_motor.run_angle(velocity, graus, Stop.HOLD, False)
    right_motor.run_angle(velocity, graus, Stop.HOLD, True)

def girar(ang_graus, velocity=100):
    fator = 2.2
    left_motor.run_angle(velocity, ang_graus * fator, Stop.HOLD, False)
    right_motor.run_angle(velocity, ang_graus * fator, Stop.HOLD, True)

def teste():
    ev3.speaker.say("TESTE TESTE TESTE ALO ALO ALO")
    wait(2000)

    #Letra L de LULA LIVRE
    andar(10)
    girar(90)
    andar(6)

    ev3.speaker.say("LULA LIVRE FAZ O ÉLI")


beep()
teste()