from curses import baudrate
from pickletools import bytes8
import serial
import keyboard
import time

class Com_Connection:
    def __init__(self, com, baudrate, timeout):
        self.com=com
        self.baudrate=baudrate
        self.timeout=timeout
    
    def serial_inputs(self):

        ser = serial.Serial(port=str(self.com),
                            baudrate=self.baudrate,
                            timeout=self.timeout) 
        ser.open()
        with open('test.txt', 'a') as f:
            while True:
                receive = ser.readline()
                f.write(receive+'\n')
                
                time.sleep(1)
                if keyboard.is_pressed('q'):
                    print("User need to quit the application")
                    break
        ser.close()
        