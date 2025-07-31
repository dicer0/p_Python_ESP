# 📄 Diseño de Alto Nivel – Backend para RandomCameraReviews

## 🔍 Definiciones y Acrónimos

- **API**: Interfaz de Programación de Aplicaciones.
- **TDD**: Desarrollo Guiado por Pruebas (*Test Driven Development*).
- **HTTP**: Protocolo de Transferencia de Hipertexto.
- **CRUD**: Crear, Leer, Actualizar, Eliminar.
- **POST**: Método HTTP para enviar datos al servidor.
- **GET**: Método HTTP para obtener datos del servidor.
- **Editor (Ed)**: Usuario autorizado que redacta y sube reseñas.
- **Usuario (Lector)**: Visitante que accede a las reseñas, sin autenticación.
- **Review (Reseña)**: Contenido editorial escrito por fotógrafos sobre cámaras específicas.

---

## 🧩 Problema a Resolver

RandomCameraReviews, una empresa especializada en la venta de cámaras fotográficas, necesita un sistema backend escalable que permita a fotógrafos profesionales (editores) subir reseñas, y que al mismo tiempo permita que cualquier persona en el mundo pueda leerlas desde una interfaz desarrollada por el equipo frontend. El objetivo es crear un sistema backend robusto, con pruebas automatizadas (TDD), que pueda ser desplegado en la nube y que esté optimizado para consultas globales.

---

## 🎯 Objetivos

- Permitir a los editores subir reseñas a través de una API autenticada.
- Proporcionar una API pública para que los usuarios puedan consultar reseñas.
- Construir el sistema backend con enfoque TDD para garantizar confiabilidad.
- Facilitar el despliegue y escalabilidad geográfica para operaciones de lectura.

### 👥 Stakeholders (Interesados)

- Equipo de Producto (define requerimientos del negocio).
- Equipo de Ingeniería Backend (desarrolla y mantiene la API).
- Desarrolladores Frontend (consumen la API).
- Editores (suben contenido al sistema).
- Usuarios Finales / Lectores (consumen contenido).

---

## 💭 Suposiciones

- Solo los editores requieren autenticación y acceso de escritura.
- Los usuarios no necesitan registrarse para consultar las reseñas.
- La moderación del contenido se realizará fuera de este sistema.
- Los editores están ubicados principalmente en Sudamérica.
- La mayoría de los usuarios están en Sudamérica y Norteamérica, con menor presencia en Europa y Asia.

---

## 🚧 Limitaciones y Desconocimientos

- No se contempla integración con herramientas de moderación o analítica externa en esta etapa.
- Las estimaciones de tráfico se basan en los mercados actuales; un crecimiento rápido puede requerir balanceo de carga.
- No se contempla la subida de archivos multimedia por el momento.
- No se incluye soporte multilenguaje o localización.

---

## 📌 Alcance del Proyecto

### ✅ Alcance Incluido

- API REST con endpoints para creación de reseñas (`POST /reviews`) y lectura de contenido (`GET /content`).
- Autenticación y control de acceso para editores.
- Almacenamiento y recuperación de datos de reseñas.
- Preparación para distribución geográfica en operaciones de lectura.
- Backend listo para desplegar con soporte para Docker.

### ❌ Fuera de Alcance

- Autenticación para los lectores.
- Flujos de aprobación o moderación de contenido.
- Implementación del frontend.
- Subida de imágenes o contenido multimedia.
- Sistema de puntuación o comentarios en las reseñas.

### 📚 Casos de Uso

1. **Ed sube una reseña**: El editor autenticado utiliza el endpoint `/reviews` para enviar una reseña.
2. **Usuario consulta una reseña**: El visitante accede al endpoint `/content` para visualizar reseñas publicadas.
3. **Editor actualiza una reseña**: (Posible función futura, no implementada en esta versión).
4. **Escalabilidad para lecturas globales**: El sistema se adapta a alta demanda de lectura en distintas regiones.

---

## 🧠 Propuesta

### 🏗️ Arquitectura General

- **Frontend**: Desarrollado por otro equipo, consumirá nuestra API REST.
- **Backend**: API REST desarrollada con Python (FastAPI o Flask).
- **Base de Datos**: PostgreSQL para almacenamiento estructurado.
- **Autenticación**: Tokens JWT para validar editores.
- **Despliegue**: Aplicación dockerizada, compatible con cualquier proveedor cloud.
- **Distribución Global**: Uso de CDN o réplicas de solo lectura para escalar el endpoint `/content`.

---

### 🔄 Endpoints de la API

| Método | Endpoint     | Descripción                                 | Requiere Autenticación |
|--------|--------------|---------------------------------------------|-------------------------|
| POST   | /reviews     | Subir una nueva reseña                      | ✅ Sí                   |
| GET    | /content     | Obtener todas las reseñas disponibles       | ❌ No                   |

---

### 🧱 Componentes del Sistema

- **Servicio de Reseñas**: Maneja la creación y validación de reseñas.
- **Servicio de Contenido**: Optimizado para lectura rápida de reseñas.
- **Servicio de Autenticación**: Emite y valida tokens JWT.
- **Capa de Base de Datos**: Almacena reseñas y credenciales de editores.

---

### 📊 Modelos de Datos (SQL)

```sql
-- Tabla de Editores
CREATE TABLE editors (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL
);

-- Tabla de Reseñas
CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  camera_model TEXT NOT NULL,
  editor_id INTEGER REFERENCES editors(id),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
