import pyb
import time
# Motors
pinA10 = pyb.Pin(pyb.Pin.cpu.A10, pyb.Pin.OUT_PP)
pinA10.high()
pinB5 = pyb.Pin.cpu.B5
tim1 = pyb.Timer(3, freq = 20000)
t1ch1 = tim1.channel(1, pyb.Timer.PWM, pin=pinB5)
pinB4 = pyb.Pin.cpu.B4
t1ch2 = tim1.channel(2, pyb.Timer.PWM, pin=pinB4)
t1ch1.pulse_width_percent(75)
t1ch2.pulse_width_percent(0)

# Encoders
pinA = pyb.Pin.cpu.B6
pinB = pyb.Pin.cpu.B7
tim4 = pyb.Timer(4, prescaler=0, period=65535)
t4ch1 = tim4.channel(1,pyb.Timer.ENC_AB, pin=pinA)
t4ch2 = tim4.channel(1,pyb.Timer.ENC_AB, pin=pinB)
while True:
    print(tim4.counter())
    time.sleep_ms(10)

