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
right_motor = Motor(Port.D)
pince_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=32, axle_track=145)

# Go forward and backwards for one meter.
#left_motor.run_time(speed=10, time=5, then=Stop.HOLD, wait=False)
#left_motor.run_time(speed=10, time=5, then=Stop.HOLD, wait=True)
#robot.straight(100)
ev3.speaker.beep()

pince_motor.run_time(
            speed=-1000,
            time=1000,
            then=Stop.COAST,
            wait=True)       

#robot.straight(-1500)
ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
#robot.turn(180)
#ev3.speaker.beep()

#robot.turn(-180)
#ev3.speaker.beep()
