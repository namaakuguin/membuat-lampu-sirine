from machine import Pin, PWM
from time import sleep

led = PWM(Pin(13))
led.freq(1000)


while True:
  #perulangan led untuk menyala terang
  for brightness in range (0,1023,10):
    led.duty(brightness)
    sleep (0.01)
  #perulangan led untuk redup kembali
  for brightness in range (1023,-1,-10):
    led.duty(brightness)
    sleep(0.01)

