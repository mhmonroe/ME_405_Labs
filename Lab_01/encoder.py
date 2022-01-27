'''!    @file       motorDriver.py
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

class EncoderDriver:
    
    def __init__ (self, enc1_pin, enc2_pin, timer):
        ''' @brief             Initializes new objects of the encoderDriver class.
            @param  enc1_pin
            @param  enc2_pin
            @param  timer      Timer ID associated with the board.
        '''
        # encoder objects
        self.enc1_pin = enc1_pin
        self.enc2_pin = enc2_pin

        # timer
        self.timer = timer

        # channels
        self.tim_ch1 = timer.channel(1, mode = pyb.Timer.ENC_AB,
                                         pin = self.enc1_pin)
        self.tim_ch2 = timer.channel(2, mode = pyb.Timer.ENC_AB,
                                         pin = self.enc2_pin)

        self.period = 2**16 - 1

        ##  To be used by the methods:
        self.delta_val = 0
        self.last_tick = 0
        self.new_tick = 0
        self.true_position = 0
        
    def read(self):
        ''' @brief                   Records values from encoders in ticks.
            @return  true_position   Position value  
        '''
        self.last_tick = self.new_tick
        self.new_tick = self.timer.counter()
        self.delta_val = self.new_tick - self.last_tick
        
        # Accounting for overflow or underflow
        if (self.delta_val > 0.5*self.period):
            self.delta_val -= self.period
        elif (self.delta_val < -0.5*self.period):
            self.delta_val += self.period

        self.true_position += self.delta_val
        return(self.true_position)

    def zero(self):
        ''' @brief  Sets encoder value to zero  
        '''
        self.true_position = 0

if __name__ == '__main__':

    ## Pin objects for encoder 1
    ENC1A_pin = pyb.Pin.cpu.B6
    ENC1B_pin = pyb.Pin.cpu.B7

    ## Pin objects for encoder 2
    ENC2A_pin = pyb.Pin.cpu.C6
    ENC2B_pin = pyb.Pin.cpu.C7

    ## Timer objects
    tim_ENC_A = pyb.Timer(4, prescaler = 0, period = 2**16 - 1)
    tim_ENC_B = pyb.Timer(8, prescaler = 0, period = 2**16 - 1)

    # Create encoder objects
    enc_A = EncoderDriver(ENC1A_pin, ENC1B_pin, tim_ENC_A)
    enc_B = EncoderDriver(ENC2A_pin, ENC2B_pin, tim_ENC_B)
    
    #test encoder to see if they work
    while(True):
        print(enc_A.read())
        enc_B.read()
        utime.sleep_ms(25)
    