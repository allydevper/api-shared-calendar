# api-shared-calendar

API para el proyecto Shared Calendar hecha con FastAPI (python).

## Descripción

Esta API permite gestionar eventos, participantes y disponibilidades para un calendario compartido. Utiliza FastAPI para la creación de endpoints y Supabase como base de datos.

## Requisitos

- Python 3.8 o superior
- FastAPI
- Supabase
- Dotenv para la gestión de variables de entorno

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/allydevper/api-shared-calendar.git
   cd api-shared-calendar
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env`:

   ```
   SUPABASE_URL=tu_supabase_url
   SUPABASE_KEY=tu_supabase_key
   ```

## Uso

Para iniciar el servidor de desarrollo, ejecuta:
