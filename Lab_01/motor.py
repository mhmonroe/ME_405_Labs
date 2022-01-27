'''!    @file       motor.py
        @brief      A driver for working with a DC motor.
        @details    The motor driver encapsulates all of the functionality
                    that will be useful for interacting with the DC motor
                    from Lab 0x03 and subsequent lab assignments.

        @author     Juan Luna
        @author     Marcus Monroe
        @author     Cade Liberty

        @date       January 26, 2022
'''

import pyb
import utime

class motorDriver:
    ''' @brief      A motor driver class for the DRV8847 from TI...
        @details    Objects of this class can be used to configure the
                    motor driver and to create one or more objects of the
                    Motor class which can be used to perform motor control.
    '''

    def __init__ (self, en_pin, in1_pin, in2_pin, timer):
        ''' @brief             Initializes new objects of the motorDriver class.
            @param  en_pin
            @param  in1_pin
            @param  in2_pin
            @param  timer      Timer ID associated with the board.
        '''
        ## enable pin
        self.en_pin = en_pin
        self.en_pin.high()

        ## define motor pins
        self.in1_pin = in1_pin
        self.in2_pin = in2_pin

        ## Timer object for motor with 20-kHz frequency.
        self.timer = timer
        
        ## Motor timer channels configured in PWM mode (active high).
        self.tim_ch1 = self.timer.channel(1, mode = pyb.Timer.PWM, 
                                               pin = self.in1_pin)
        self.tim_ch2 = self.timer.channel(2, mode = pyb.Timer.PWM, 
                                               pin = self.in2_pin)

    def set_duty_cycle (self, duty):
        ''' @brief      Set duty cycle as a pulse width percent for the motors.
            @details    Positive values represent rotation of the motor in one
                        direction (clockwise) and negative values in the
                        opposite direction (counterclockwise).

            @param  duty    Signed value representing duty cycle of
                            PWM signal to be sent to the motor pins.            
        '''

        print("Setting duty cycle to " + str(duty))
        
        ## Positive duty cycle
        if (duty >= 0):
            self.tim_ch1.pulse_width_percent(abs(duty))
            self.tim_ch2.pulse_width_percent(0)
        ## Negative duty cycle
        elif (duty < 0):
            self.tim_ch1.pulse_width_percent(0)
            self.tim_ch2.pulse_width_percent(abs(duty))

if __name__ == '__main__':

    ## Enable pins
    ENA = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
    ENB = pyb.Pin(pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)

    ## Pin objects associated with first motor.
    IN1A_pin = pyb.Pin.cpu.B4
    IN2A_pin = pyb.Pin.cpu.B5

    ## Pin objects associated with first motor.
    IN1B_pin        = pyb.Pin.cpu.A0
    IN2B_pin        = pyb.Pin.cpu.A1

    ## Timer objects for motors with 20-kHz frequency.
    tim_MOT_A = pyb.Timer(3, freq = 20000)
    tim_MOT_B = pyb.Timer(5, freq = 20000)

    ## Motor objects
    motor_A = motorDriver(ENA, IN1A_pin, IN2A_pin, tim_MOT_A)
    motor_B = motorDriver(ENB, IN1B_pin, IN2B_pin, tim_MOT_B)
    
    # Test the motors to see if they work
    while(True):
        motor_A.set_duty_cycle(int(input('Please Enter motor duty cycle for Motor A: ')))
        motor_B.set_duty_cycle(int(input('Please Enter motor duty cycle for Motor B: ')))