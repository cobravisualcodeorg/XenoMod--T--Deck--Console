# Xenomod T Deck Console



Xenomod T Deck Console es una interfaz de línea de comandos (CLI) para la **LilyGO T-Deck** con ESP32-S3, desarrollada por **CobraVisualCode.org**. Proporciona una experiencia de consola interactiva con soporte para comandos básicos, ejecución de scripts en Python y navegación de archivos.

## Características

- Interfaz de consola con entrada y salida de texto.
- Explorador de archivos integrado con desplazamiento.
- Posibilidad de ejecutar scripts `.py` desde la consola.
- Indicador visual de memoria libre.
- Reinicio del sistema desde la interfaz.
- Control con el teclado de la T-Deck y el trackball.


## Requisitos

- **LilyGO T-Deck** con ESP32-S3.
- **Firmware MicroPython** compatible. 👉https://github.com/cobravisualcodeorg/LilyGO-T-Deck-micropython-ES/tree/main/Firmware%2Cs


## Instalación
1. **descarga este repositorio**
2. **Sube el código** con un entorno compatible con MicroPython. si no tienes uno te recomiendo thonny 👉https://thonny.org/
 ![thonny](https://github.com/user-attachments/assets/28818597-4949-4aa0-bd81-3f39c429e08e)

5. **Asegúrate** de que las bibliotecas necesarias están disponibles en el sistema de archivos.Si decargaste el este repositorio no deberia tener problemas con las librerias. siempre y cuando instales el firmware que se encuentra en este repositorio.

## Uso (Beta)

### Comandos Disponibles

| Comando         | Descripción |
|----------------|------------|
| `ls`          | Lista los archivos en el sistema. |
| `run`         | Ejecuta un script `.py` existente. | # Escribe Run en la consola y luego presona enter y coloca el nombre del archivo.py y preciona enter>>
| `mem`         | Muestra la memoria disponible en la T-Deck. |
| `reboot`      | Reinicia el sistema. |
| `exit`        | Sale de la consola. |
| `wifi`        | (No disponible en versión beta). |
| `help`        | Muestra la lista de comandos disponibles. |
| `about_me`    | Información sobre el sistema y el desarrollador. |

### Uso del Trackball

- **Arriba / Abajo**: Navegar entre archivos.


## Créditos

Desarrollado por **Kevin Nazario** para **CobraVisualCode.org**.
______________________________
🐰 Proyecto en fase **Beta**.
______________________________


