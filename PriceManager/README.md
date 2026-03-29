# mi_app

Aplicación de escritorio con **Python**, **CustomTkinter** y arquitectura por capas (UI, controladores, servicios, modelos).

## Requisitos

- Python 3.10 o superior (recomendado)

## Instalación

1. Crear y activar un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Desde la carpeta `mi_app`:

```bash
python run.py
```

## Pruebas

```bash
pytest tests
```

## Estructura

- `app/` — código de la aplicación
- `assets/` — iconos, imágenes, temas
- `data/` — entrada, salida y archivos temporales
- `tests/` — pruebas
