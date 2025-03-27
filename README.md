
# Proyecto Django - Instrucciones para Clonar y Ejecutar

Este repositorio contiene un proyecto desarrollado en **Django**. Si deseas clonar el repositorio y verlo funcionando en tu máquina local, sigue los siguientes pasos.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Python**: Asegúrate de tener instalada la versión adecuada de Python. Puedes verificar la versión con el siguiente comando:
  ```bash
  python3 --version
  ```

- **Pip**: Asegúrate de tener `pip` instalado para poder gestionar las dependencias. Para verificar si está instalado, ejecuta:
  ```bash
  pip3 --version
  ```

## Clonando el Repositorio

1. **Clonar el repositorio a tu máquina local**:

   Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/usuario/mi-proyecto-django.git
   cd mi-proyecto-django
   ```

   Asegúrate de reemplazar `https://github.com/usuario/mi-proyecto-django.git` con la URL de tu repositorio.

## (Recomendado) Instalación del VENV

- **Virtualenv**: Te recomiendo usar un entorno virtual para evitar conflictos de dependencias. Si no tienes `virtualenv` instalado, puedes instalarlo con:

  ```bash
  python3 -m venv env
  ```

### Activación del VENV

- Si estás en **Linux**:

  ```bash
  source env/bin/activate
  ```

- Si estás en **Windows**:

  ```bash
  .\env\Scriptsctivate
  ```

## Instalación de Requisitos

- Una vez activado el entorno virtual, instala los requisitos necesarios desde el archivo `requirements.txt` ejecutando el siguiente comando:

  ```bash
  pip install -r requirements.txt
  ```

## Configuración de la Base de Datos

- Ejecuta los siguientes comandos para aplicar las migraciones y configurar la base de datos:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Crear un superusuario** para poder acceder al panel de administración de la aplicación:

  ```bash
  python manage.py createsuperuser
  ```

  Sigue las instrucciones para configurar el nombre de usuario, correo electrónico y contraseña.

## Arrancar el Proyecto

- Una vez que todo esté configurado, ejecuta el siguiente comando para iniciar el servidor local:

  ```bash
  python manage.py runserver
  ```

El proyecto debería estar disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Contacto

Si tienes alguna pregunta o encuentras algún problema, no dudes en abrir un _issue_ en el repositorio o contactar conmigo.

- **Correo electrónico**: [tu-email@example.com](mailto:tu-email@example.com)
- **LinkedIn**: [tu-linkedin](https://www.linkedin.com/in/tu-linkedin)

¡Gracias por revisar mi proyecto!
