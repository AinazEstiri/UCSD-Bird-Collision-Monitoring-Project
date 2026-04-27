import time
import math
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
acc = adafruit_adxl34x.ADXL345(i2c)

THRESHOLD = 2.0

last_mag = None

while True:
    x, y, z = acc.acceleration

    mag = math.sqrt(x*x + y*y + z*z)

    if last_mag is not None:
        diff = abs(mag - last_mag)

        if diff > THRESHOLD:
            print(f"Viberation Detected!\t{diff:.2f}  x={x:.2f}, y={y:.2f}, z={z:.2f}")
        else:
            print(f"Viberation Listening...\t{diff:.2f}")

    last_mag = mag
    time.sleep(0.05)
