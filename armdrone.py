from pymavlink import mavutil
from dronekit import *
import cv2
import numpy as np
from simple_pid import PID




def connect_drone(port, wait_ready=True, baud_rate=57600):
    vehicle = connect(port, wait_ready, baud_rate)
    print('Connection succesful')
    return vehicle

def arm_drone():
    print("Basic pre-arm checks")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
    print("Arming motors")
    vehicle.armed = True


vehicle = connect_drone()
arm_drone()