# Proyecto Django - Instrucciones para Clonar y Ejecutar

Este repositorio contiene un proyecto desarrollado en **Django**. Si deseas clonar el repositorio y verlo funcionando en tu máquina local, sigue los siguientes pasos.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Python**: Asegúrate de tener instalada la versión adecuada de Python. Puedes verificar la versión con el siguiente comando:
  ```bash
  python3 --version

  
- **Pip**: Asegúrate de tener pip instalado para poder gestionar las dependencias. Para verificar si está instalado, ejecuta:
  ```bash
   pip3 --version
  
## (Recomendado) Instalacion del VENV
- **Viertualenv**:: Te recomiendo usar un entorno virtual para evitar conflictos de dependencias. Si no tienes virtualenv instalado, puedes instalarlo con:
    ```bash
    python3 -m venv env

**Activacion de Venv**

- Si estas en Linux:
   ```bash
    source env/bin/activate

- Si estas en Windows:
   ```bash
    .\env\Scripts\activate

**AInstalacion de requisitos**
- Puedes instalar los requisitos necesario del requirements.txt con el iguiente comando:
  ```bash
    pip install -r requirements.txt

## Configuracion de la base de datos
- Ejecuta el siguiente comando para aplicar las migraciones y configurar la base de datos:
  ```bash
    python manage.py makemigrations
    python manage.py migrate

- Crear un superUsuario para poder acceder a la aplicacion:
  ```bash
    python manage.py createsuperuser

**Arrancan el programa**
- Una vez que todo esté configurado, ejecuta el siguiente comando para iniciar el servidor local:
  ```bash
    python manage.py runserver







  
