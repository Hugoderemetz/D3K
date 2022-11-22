#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the sound volume
ev3.speaker.set_volume(100, which='_all_')

# Initialize the language
ev3.speaker.set_speech_options("fr", "m3", 1, 1)

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
pince_motor = Motor(Port.A)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=32, axle_track=145)

count = 2
distance = 455
batery = ev3.battery.current()

ev3.screen.draw_text(0, 0, str(batery), Color.RED, Color.GREEN)
wait(2000)
ev3.screen.load_image("dizzy.png")  

for i in range(1, count + 1):
    ev3.speaker.play_file("boing.wav")
    robot.straight(distance * i)                    # Avance          
    ev3.speaker.play_file("boing.wav")
    pince_motor.run_until_stalled(                  # Ouvre la pince
                speed=-500,
                then=Stop.COAST,
                duty_limit=100)
    robot.straight(40)                              # Avance
    pince_motor.run_until_stalled(                  # Ferme la pince
                speed=500,
                then=Stop.HOLD,
                duty_limit=100)   
    ev3.speaker.play_file("boing.wav")
    robot.turn(180)                                 # Demi-tour
    ev3.speaker.play_file("boing.wav")
    robot.straight(distance * i + 60)               # Avance
    pince_motor.run_until_stalled(                  # Ouvre la pince
                speed=-500,
                then=Stop.COAST,
                duty_limit=100)  
    robot.straight(-50)                             # Recule
    pince_motor.run_until_stalled(                  # Ferme la pince
                speed=500,
                then=Stop.HOLD,
                duty_limit=100)
    robot.turn(180)                                # Demi-tour
    ev3.speaker.say("Travail terminé")
