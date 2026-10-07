import RPi.GPIO as GPIO # type: ignore
from time import sleep

# GPIO correspondientes a cada luz
ROJO = 18
AMARILLO = 24
VERDE = 23

LUCES = [ROJO, AMARILLO, VERDE]

def configurar():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for pin in LUCES:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


def apagar_todas():
    for pin in LUCES:
        GPIO.output(pin, GPIO.LOW)


def activar(pin, nombre, segundos):
    apagar_todas()
    GPIO.output(pin, GPIO.HIGH)
    print(f"[SEMAFORO] {nombre} activo")
    sleep(segundos)
    GPIO.output(pin, GPIO.LOW)


try:
    configurar()

    print("--------------------------------")
    print("     CONTROL DE SEMAFORO")
    print("--------------------------------")
    print("Modo de trabajo: BCM")
    print("GPIO:", LUCES)
    print("Presiona Ctrl+C para finalizar\n")

    while True:
        activar(VERDE, "LUZ VERDE", 10)
        activar(AMARILLO, "LUZ AMARILLA", 3)
        activar(ROJO, "LUZ ROJA", 10)

except KeyboardInterrupt:
    print("\nSecuencia detenida por el usuario.")

finally:
    apagar_todas()
    GPIO.cleanup()
    print("GPIO liberados correctamente.")