from machine import Pin,PWM
from time import sleep

led1 = PWM(Pin(13), freq = 1000)
led2 = PWM(Pin(14), freq = 1000)
buzzer = PWM(Pin(12), freq=1000)
buzzer.duty (0)

#fungsi utama untuk mengaktifkan semua komponen
def jalankan_sistem(brightness):
# atur kecerahan lampu led
    led1.duty(brightness)
    led2.duty(brightness)

# hitung jeda berdasarkan kecerahan 
    jeda = 0.15 - ( brightness / 1023 * 0.11)

# bunyikan buzzer
    buzzer.duty(512)
    sleep(jeda)
    buzzer.duty(0)
    sleep(jeda)

while True:
# loop naik
  for brightness in range (0,1023,100):

    jalankan_sistem(brightness)

#loop turun
  for brightness in range (1023,-1,-100):

    jalankan_sistem(brightness)
