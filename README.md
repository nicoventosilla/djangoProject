# Django Project

Este es un proyecto Django para gestionar personas. Incluye funcionalidades para agregar, editar y listar personas.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos previos](#requisitos-previos)
- [Directorios y archivos clave](#directorios-y-archivos-clave)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución del proyecto](#ejecución-del-proyecto)
- [Pruebas](#pruebas)
- [Despliegue](#despliegue)
- [Contribuciones](#contribuciones)

## Características

- Agregar nuevas personas
- Editar información de personas existentes
- Listar todas las personas

## Requisitos previos

- Python 3.12
- Django 5.0.7 o superior

## Directorios y archivos clave

- **djangoProject/**: Contiene la configuración principal del proyecto Django.
  - `settings.py`: Configuraciones de Django para el proyecto.
  - `urls.py`: Enrutamiento de URLs para el proyecto.
  - `wsgi.py`: Configuración WSGI para despliegue.
  - `asgi.py`: Configuración ASGI para soporte asincrónico.

- **personas/**: Contiene la lógica de la aplicación para gestionar personas.
  - `models.py`: Define los modelos de datos.
  - `views.py`: Maneja las solicitudes y respuestas web.
  - `admin.py`: Configuración para la interfaz de administración de Django.
  - `tests.py`: Pruebas unitarias para la aplicación.

- **templates/**: Contiene las plantillas HTML para renderizar páginas web.
  - `index.html`: Página principal que muestra la lista de personas.
  - `nueva_persona.html`: Formulario para agregar una nueva persona.
  - `editar_persona.html`: Formulario para editar una persona.

## Instalación

1. **Clonar el repositorio**:
    ```sh
    git clone https://github.com/yourusername/djangoProject.git
    cd djangoProject
    ```

2. **Crear un entorno virtual**:
    ```sh
    python -m venv venv
    ```

3. **Activar el entorno virtual**:
    - En Windows:
        ```sh
        venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Instalar las dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

1. **Configuración de la base de datos**:
    - Abre `djangoProject/settings.py` y configura el ajuste `DATABASES`. Por ejemplo, para usar SQLite (predeterminado):
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        ```
    - Para PostgreSQL:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_db_name',
                'USER': 'your_db_user',
                'PASSWORD': 'your_db_password',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        ```

2. **Aplicar migraciones**:
    ```sh
    python manage.py migrate
    ```

## Ejecución del proyecto

1. **Iniciar el servidor de desarrollo**:
    ```sh
    python manage.py runserver
    ```

2. Abre tu navegador web y ve a `http://127.0.0.1:8000/`.

## Pruebas

1. **Ejecutar las pruebas**:
    ```sh
    python manage.py test
    ```

## Despliegue

1. **Recopilar archivos estáticos**:
    ```sh
    python manage.py collectstatic
    ```

2. **Configurar tu servidor web** (por ejemplo, Gunicorn, Nginx) para servir la aplicación Django.

Para instrucciones de despliegue más detalladas, consulta la [documentación de despliegue de Django](https://docs.djangoproject.com/en/stable/howto/deployment/).

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.
