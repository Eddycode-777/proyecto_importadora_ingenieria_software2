# IMPORCOM S.R.L — Sistema de Gestión de Productos

Sistema web CRUD para la gestión de productos de una importadora de artículos de fiestas, desarrollado con Python y Flask siguiendo el patrón MVC.

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Versión | Uso |
|---          |---      |---   |
| Python      | 3.x     | Lenguaje principal |
| Flask       | 3.1.3   | Framework web |
| Flask-
SQLAlchemy    | 3.1.1  | ORM para la base de datos |
| SQLAlchemy  | 2.0.51 | Motor ORM |
| psycopg2-
binary        | 2.9.12 | Conector PostgreSQL |
| python-
dotenv        | 1.2.2  | Variables de entorno |
| Jinja2      | 3.1.6  | Motor de plantillas HTML |
| PostgreSQL  | 14+    | Base de datos relacional |
| CSS         | —       | Estilos del frontend |

---

## 📁 Estructura del proyecto

```
Examen/
├── app.py                        ← Punto de entrada de la aplicación
├── config.py                     ← Configuración (lee variables del .env)
├── .env                          ← Credenciales reales (NO se sube a GitHub)
├── .env.example                  ← Plantilla pública del .env
├── .gitignore                    ← Archivos excluidos del repositorio
├── requirements.txt              ← Dependencias del proyecto
├── README.md                     ← Este archivo
├── models/
│   └── producto_model.py         ← Modelo de datos con SQLAlchemy
├── controllers/
│   └── producto_controller.py    ← Rutas y lógica CRUD (Blueprint)
├── templates/
│   ├── base.html                 ← Layout base (nav, header, footer)
│   ├── index.html                ← Listado de productos
│   ├── crear.html                ← Formulario de creación
│   └── editar.html               ← Formulario de edición
└── static/
    └── style.css                 ← Estilos CSS
```

---

## ⚙️ Requisitos previos

- Python 3.10 o superior
- PostgreSQL instalado y en ejecución
- Git instalado

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd Examen
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar las variables de entorno

Copia el archivo de ejemplo:

```bash
# Windows
copy .env.example .env

# Linux / Mac
cp .env.example .env
```

Edita `.env` con tus credenciales de PostgreSQL:

```ini
DB_USER=postgres
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=examen_importadora
SECRET_KEY=cualquier_clave_segura
FLASK_DEBUG=True
```

### 6. Crear la base de datos en PostgreSQL

Abre pgAdmin o psql y ejecuta:

```sql
CREATE DATABASE examen_importadora;
```

> ✅ La tabla `productos` se crea automáticamente al iniciar la aplicación.

### 7. Ejecutar la aplicación

```bash
python app.py
```

### 8. Abrir en el navegador

```
http://127.0.0.1:5000
```

---

## 📋 Funcionalidades

| Operación | Ruta | Descripción |
|---|---|---|
| ✅ Listar | `/` | Muestra todos los productos |
| ✅ Crear | `/crear` | Formulario para agregar un producto |
| ✅ Editar | `/editar/<id>` | Formulario para modificar un producto |
| ✅ Eliminar | `/eliminar/<id>` | Elimina un producto con confirmación |

---

## 📦 Categorías disponibles

Los productos se clasifican en las siguientes categorías:

- Globos y decoraciones
- Piñatas
- Cotillón
- Vajilla desechable
- Disfraces y accesorios
- Velas y cake toppers
- Serpentinas y confeti
- Luces y efectos
- Artículos temáticos
- Empaque y bolsas

---

## 🏗️ Arquitectura — Patrón MVC

El proyecto sigue el patrón **MVC (Modelo - Vista - Controlador)**:

```
Petición HTTP
     ↓
Controlador (controllers/producto_controller.py)
     ↓              ↑
  Modelo     →   Datos
(models/)        (PostgreSQL)
     ↓
  Vista
(templates/)
     ↓
Respuesta HTML
```

| Capa | Archivo | Responsabilidad |
|---|---|---|
| Modelo | `models/producto_model.py` | Define la tabla y acceso a datos |
| Vista | `templates/` | Renderiza el HTML con Jinja2 |
| Controlador | `controllers/producto_controller.py` | Gestiona rutas y lógica CRUD |
| Configuración | `config.py` + `.env` | Parámetros de conexión |

---


