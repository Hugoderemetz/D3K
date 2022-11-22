#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
pince_motor = Motor(Port.A)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=32, axle_track=145)

# Go forward and backwards for one meter.

robot.straight(100)
ev3.speaker.beep()

pince_motor.run_until_stalled(
            speed=1000,
            then=Stop.COAST,
            duty_limit=100)  

ev3.speaker.beep()
ev3.speaker.beep()

pince_motor.run_until_stalled(
            speed=1000,
            then=Stop.HOLD,
            duty_limit=100)   

robot.straight(-100)
ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
#robot.turn(180)
#ev3.speaker.beep()

#robot.turn(-180)
#ev3.speaker.beep()
