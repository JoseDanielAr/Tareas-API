# Tareas App — Full Stack (Flask + React)

API REST construida con Flask y SQLite, con frontend en React + Vite. 

---

## Requisitos previos

- Python 3.11+
- Node.js 18+
- Git

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Tareas-API.git
git clone https://github.com/TU_USUARIO/Tareas-Front.git
```

---

## 2. Correr el backend

```bash
cd Tareas-API

# Crear y activar el entorno virtual
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Correr el servidor
python app.py
```

La API quedará disponible en `http://127.0.0.1:5000`

### Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /tasks | Listar todas las tareas |
| GET | /tasks/\<id\> | Obtener una tarea |
| POST | /tasks | Crear una tarea |
| PUT | /tasks/\<id\> | Actualizar una tarea |
| DELETE | /tasks/\<id\> | Eliminar una tarea |

---

## 3. Correr el frontend

```bash
cd Tareas-Front

# Crear el archivo de variables de entorno
echo VITE_API_URL=http://127.0.0.1:5000 > .env

# Instalar dependencias
npm install

# Correr el servidor de desarrollo
npm run dev
```

El frontend quedará disponible en `http://localhost:5173`

---

## 4. Links de producción

- **Frontend (Vercel):** https://tareas-front.vercel.app
- **Backend (Render):** https://tareas-saiw.onrender.com
