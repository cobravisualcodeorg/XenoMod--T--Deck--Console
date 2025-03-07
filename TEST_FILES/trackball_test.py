from machine import Pin, SPI
import utime
import st7789

spi = SPI(1, baudrate=8000000, sck=Pin(40), mosi=Pin(41), miso=Pin(38))
DC = Pin(11, Pin.OUT)
CS = Pin(12, Pin.OUT)
BL = Pin(42, Pin.OUT)
tft = st7789.ST7789(spi, 240, 320, dc=DC, cs=CS, backlight=BL, rotation=1)
tft.init()
tft.on()

kbd_pwr = Pin(10, Pin.OUT)

# Trackball pins
tb_up = Pin(3, mode=Pin.IN, pull=Pin.PULL_UP)
tb_down = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)
tb_left = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)
tb_right = Pin(2, mode=Pin.IN, pull=Pin.PULL_UP)
tb_click = Pin(0, mode=Pin.IN, pull=Pin.PULL_UP)

x = 160  # Posición inicial centrada
y = 120

TRACK_SPEED = 4

tb_int = False
tb_up_count = 0
tb_down_count = 0
tb_left_count = 0
tb_right_count = 0
tb_click_count = 0

kbd_pwr.on()
utime.sleep(0.5)

def cursor(prev, new):
    tft.fill_circle(prev[0], prev[1], 6, st7789.BLACK)
    tft.fill_circle(new[0], new[1], 6, st7789.WHITE)

def explode(new):
    for r in range(6, 15):
        tft.fill_circle(new[0], new[1], r, st7789.WHITE)
    for r in reversed(range(6, 15)):
        tft.fill_circle(new[0], new[1], r, st7789.BLACK)

def button_isr(pin):
    global tb_int, tb_left_count, tb_right_count, tb_up_count, tb_down_count, tb_click_count
    tb_int = True

    if pin == tb_up:
        tb_up_count = TRACK_SPEED
    elif pin == tb_down:
        tb_down_count = TRACK_SPEED
    elif pin == tb_left:
        tb_left_count = TRACK_SPEED
    elif pin == tb_right:
        tb_right_count = TRACK_SPEED
    elif pin == tb_click:
        tb_click_count = 1

tb_up.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)
tb_down.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)
tb_left.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)
tb_right.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)
tb_click.irq(trigger=Pin.IRQ_FALLING, handler=button_isr)

def handle_tb():
    global tb_int, x, y, tb_left_count, tb_right_count, tb_up_count, tb_down_count, tb_click_count
    prev = (x, y)

    if tb_int:
        x -= tb_left_count
        x += tb_right_count
        y += tb_down_count  # Se sumaba en la dirección equivocada
        y -= tb_up_count

        print(f"Posición: x={x}, y={y}, tb_down_count={tb_down_count}")

        # Limitar el movimiento dentro de la pantalla
        x = max(0, min(x, 320))
        y = max(0, min(y, 240))

        if tb_click_count:
            explode((x, y))

        cursor(prev, (x, y))

        tb_int = False
        tb_up_count = 0
        tb_down_count = 0
        tb_left_count = 0
        tb_right_count = 0
        tb_click_count = 0

while True:
    handle_tb()

