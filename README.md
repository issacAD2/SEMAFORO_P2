# P2_SemaforoLeds

# Práctica P2: Implementación de un Semáforo mediante GPIO

## Introducción

En esta actividad se desarrolló una representación sencilla de un semáforo utilizando una Raspberry Pi y tres LEDs de diferentes colores. Cada LED representa una de las señales tradicionales de un semáforo: rojo, amarillo y verde.

El control de los componentes se realizó mediante Python, utilizando la librería `RPi.GPIO` para enviar señales digitales a los pines de la Raspberry Pi.

El trabajo se realizó de manera remota. Para acceder al dispositivo se utilizó una conexión SSH desde una máquina virtual con Fedora ejecutada mediante VirtualBox.

---

## Propósito

El objetivo principal de esta práctica fue aplicar el funcionamiento de las salidas digitales de la Raspberry Pi para controlar varios dispositivos de manera secuencial.

Con esta actividad se practicó:

* Configuración de pines GPIO.
* Numeración BCM.
* Programación de secuencias mediante Python.
* Uso de tiempos de espera.
* Manejo de ciclos infinitos.
* Interrupción de programas mediante `Ctrl+C`.
* Liberación de los GPIO al terminar la ejecución.
* Conexión remota mediante SSH.

---

## Material y herramientas

Para realizar el montaje y la programación se utilizaron:

* Raspberry Pi.
* 1 LED rojo.
* 1 LED amarillo.
* 1 LED verde.
* Resistencias.
* Protoboard.
* Cables de conexión.
* Computadora.
* Fedora Linux.
* VirtualBox.
* Python 3.
* Librería `RPi.GPIO`.
* Conexión de red.

---

## Distribución de los GPIO

Los LEDs fueron conectados a tres GPIO diferentes utilizando la numeración BCM.

| Luz      | GPIO BCM | Pin físico | Tipo   |
| -------- | -------: | ---------: | ------ |
| Rojo     |       18 |         12 | Salida |
| Amarillo |       24 |         18 | Salida |
| Verde    |       23 |         16 | Salida |

La configuración BCM permite utilizar directamente los números correspondientes a los GPIO en el programa.

---

## Acceso remoto

Antes de ejecutar el programa fue necesario establecer comunicación con la Raspberry Pi.

Desde Fedora se utilizó el siguiente comando:

```bash
ssh mar@192.168.50.83
```

Una vez establecida la conexión, se pudo trabajar desde la terminal directamente sobre la Raspberry Pi.

---

## Configuración del entorno

Para trabajar con las dependencias de Python se activó el entorno virtual utilizado durante la práctica:

```bash
source 8S11/bin/activate
```

Cuando el entorno se encuentra activo, su nombre aparece al inicio de la línea de comandos.

Posteriormente se creó el archivo correspondiente al programa:

```bash
sudo nano semaforoLeds.py
```

---

## Ejecución

Después de guardar el código, se inició el programa mediante:

```bash
python semaforoLeds.py
```

El programa permanece funcionando continuamente hasta que se presiona `Ctrl+C`.

---

## Funcionamiento del sistema

El programa comienza configurando los tres GPIO como salidas digitales.

Inicialmente todas las luces permanecen apagadas. Después comienza la secuencia del semáforo.

### Primera etapa: luz verde

El GPIO correspondiente al LED verde se activa y permanece encendido durante:

**10 segundos**

Después de ese tiempo se apaga para continuar con la siguiente etapa.

### Segunda etapa: luz amarilla

A continuación se activa el LED amarillo.

Su tiempo de funcionamiento es de:

**3 segundos**

Una vez transcurrido el tiempo establecido, vuelve a apagarse.

### Tercera etapa: luz roja

Finalmente se activa el LED rojo durante:

**10 segundos**

Después de apagarse, el programa vuelve a comenzar desde la luz verde.

La secuencia completa es:

```text
VERDE
  ↓
10 segundos
  ↓
AMARILLO
  ↓
3 segundos
  ↓
ROJO
  ↓
10 segundos
  ↓
REPETIR
```

---

## Control de la ejecución

Para mantener la secuencia activa se utiliza un ciclo `while True`.

Esto hace que el programa continúe ejecutándose hasta recibir una interrupción por parte del usuario.

Cuando se presiona:

```text
Ctrl + C
```

se activa el manejo de `KeyboardInterrupt`, permitiendo detener el programa de manera controlada.

---

## Liberación de los pines

Al finalizar la ejecución se realiza una limpieza de los GPIO mediante:

```python
GPIO.cleanup()
```

Esta instrucción permite liberar los pines que fueron utilizados por el programa y devolverlos a un estado seguro.

---

## Evidencias

Durante el desarrollo de la práctica se obtuvieron diferentes evidencias del proceso realizado.

### 1. Conexión y trabajo desde la terminal

Se realizó la conexión mediante SSH y se preparó el entorno de trabajo.

![Captura de pantalla](images/terminal.jpeg)

### 2. Edición del programa

Se utilizó el editor `nano` para crear y modificar el archivo `semaforoLeds.py`.

![Captura de pantalla](images/nano.jpeg)

### 3. Funcionamiento de la luz verde

Se comprobó el encendido del LED verde durante la primera etapa de la secuencia.

![Captura de pantalla](images/1.jpeg)

### 4. Funcionamiento de la luz amarilla

Posteriormente se verificó el encendido del LED amarillo.

![Captura de pantalla](images/2.jpeg)

### 5. Funcionamiento de la luz roja

Finalmente se comprobó la activación del LED rojo.

![Captura de pantalla](images/3.jpeg)

---

## Resultado

La práctica permitió comprobar que los tres LEDs pueden ser controlados de forma independiente mediante los GPIO de la Raspberry Pi.

La secuencia implementada funcionó de manera continua siguiendo el orden:

**Verde → Amarillo → Rojo → Verde → Amarillo → Rojo**

Los tiempos configurados fueron de 10 segundos para las luces verde y roja, y 3 segundos para la luz amarilla.

---

## Conclusión

Con la realización de esta práctica se logró implementar una simulación funcional de un semáforo utilizando una Raspberry Pi.

El ejercicio permitió reforzar el conocimiento sobre el manejo de GPIO mediante Python, además de practicar estructuras de repetición, temporizadores y control de interrupciones.

También se comprobó la utilidad de la conexión SSH para desarrollar y ejecutar programas en la Raspberry Pi desde otro equipo.

Finalmente, el proyecto permitió observar de forma práctica cómo una secuencia programada puede controlar diferentes componentes electrónicos conectados a una computadora de propósito general como la Raspberry Pi.
