import board
import busio
from adafruit_bno08x.i2c import BNO08X_I2C
from adafruit_bno08x.uart import BNO08X_UART
from adafruit_bno08x import BNO_REPORT_ACCELEROMETER

# i2c = board.I2C()
# 3Mkb/s
# uart = busio.UART(board.TX, board.RX, baudrate=3000000)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

i2c = busio.I2C(board.SCL, board.SDA, 100000)
# bno = BNO08X_UART(uart, debug=True)
bno = BNO08X_I2C(i2c,debug=True)
bno.enable_feature(BNO_REPORT_ACCELEROMETER)

while True:
    accel_x, accel_y, accel_z = bno.acceleration  # pylint:disable=no-member
    print("X: %0.6f  Y: %0.6f Z: %0.6f  m/s^2" % (accel_x, accel_y, accel_z))