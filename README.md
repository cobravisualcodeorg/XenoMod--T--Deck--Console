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
- **Firmware MicroPython** compatible.
- **Bibliotecas necesarias:** `st7789`, `machine`, `os`, `_thread`, `gc`, `time`.

## Instalación

1. **Sube el código** a la T-Deck con un entorno compatible con MicroPython.
2. **Asegúrate** de que las bibliotecas necesarias están disponibles en el sistema de archivos.Si decargaste el este repsitorio no deberia tener problemas con las librerias. siempre y cuando instales el firmware que se encuentra en este repositorio.

## Uso

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

🐰 Proyecto en fase **Beta**.

---
"Xenomod FT CSP version v.1" - 2025

