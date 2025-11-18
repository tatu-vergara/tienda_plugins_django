# Tatu plugins - Tienda de Plug-ins de Audio

Proyecto final del Módulo 7 — Desarrollo Web con Django

Tatu plugins es una aplicación web desarrollada con Django + MySQL para gestionar una tienda de plug-ins digitales de audio.
Incluye CRUD completo de productos, categorías, etiquetas y detalles técnicos, junto con consultas avanzadas usando el ORM de Django y un dump SQL para facilitar la reproducción del proyecto.

🚀 Tecnologías utilizadas

Python 3.x

Django 5.x

MySQL 8.x

HTML5 + CSS

Django Admin

ORM de Django (filter, exclude, annotate, raw)

## Funcionalidades principales
✔ CRUD completo
Productos

Cada producto tiene:

Nombre

Descripción

Precio

Categoría

Etiquetas (many-to-many)

Detalles técnicos (dimensiones de la interfaz + peso en MB)

### Acciones disponibles:

Crear

Listar

Ver detalle

Editar

Eliminar

### Categorías

Lista

Crear

Editar

Eliminar

### Etiquetas

Lista

Crear

Editar

Eliminar

## Relaciones entre modelos

1 categoría → muchos productos

muchos productos ↔ muchas etiquetas

1 producto ↔ 1 detalle técnico (OneToOneField)

## Consultas avanzadas implementadas

Disponible en:
👉 /productos/analitica/

Incluye:

filter()

exclude()

annotate() con agregaciones (conteo, promedios)

raw() con SQL parametrizado

## Seguridad

CSRF en todos los formularios

Sesiones y middleware de seguridad (Django por defecto)

Uso de autenticación de Django (django.contrib.auth)

Panel admin para gestionar todos los modelos

## Estructura de templates
templates/
│
├── base.html
├── index.html
│
├── productos/
│   ├── lista.html
│   ├── crear.html
│   ├── detalle.html
│   ├── editar.html
│   └── eliminar.html
│
├── categorias/
│   ├── lista.html
│   └── formulario.html
│
└── etiquetas/
    ├── lista.html
    └── formulario.html

## Base de datos incluida (Dump MySQL)

Este proyecto incluye un dump SQL listo para importar llamado:

db_inicial.sql

Este archivo contiene:

la estructura de la base de datos

los datos iniciales del proyecto (categorías, productos, etiquetas, detalles)

### Cómo importar la base de datos

Crear la base de datos vacía:

CREATE DATABASE tienda_plugins_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;


Importar el dump:

mysql -u tu_usuario -p tienda_plugins_db < db_inicial.sql


Con eso tendrás toda la base de datos lista con los mismos datos del proyecto original.

## Instalación y ejecución del proyecto

### 1. Clonar el repositorio
git clone <URL_DEL_REPO>
cd tienda_plugins

### 2. Crear y activar un entorno virtual
Windows
python -m venv .venv
.venv\Scripts\activate

Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Configurar MySQL en tienda_plugins/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tienda_plugins_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}

### 5. (Opción A — Recomendada) Usar el dump SQL
mysql -u tu_usuario -p tienda_plugins_db < db_inicial.sql


Listo. No necesitas migraciones.

### 6. (Opción B — Alternativa) Construir la BD desde cero
python manage.py migrate
python manage.py createsuperuser


(Pero recuerda que los datos iniciales vienen listos en db_inicial.sql.)

### 7. Ejecutar servidor
python manage.py runserver
