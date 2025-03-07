# Proyecto ETL

## Overview

Este proyecto implementa un proceso ETL (Extracción, Transformación y Carga) en Python, diseñado para procesar y limpiar los datos contenidos en el archivo **Films_2 .xlsx**. La arquitectura se ha desarrollado siguiendo buenas prácticas de ingeniería de datos y agregando observabilidad mediante logging para monitorear la ejecución y detectar errores.

## Estructura del Proyecto

La organización del proyecto es la siguiente:

```
etl_project/
├── etl/
│   ├── extractor.py         # Módulo de extracción: Lee el archivo Excel (omitiendo la primera hoja que contiene el MER) y carga cada hoja en un DataFrame.
│   ├── transformer.py       # Módulo de transformación: Limpia datos numéricos, valida claves foráneas y registra eventos mediante logging.
│   ├── loader.py            # Módulo de carga: Exporta los DataFrames transformados a archivos CSV.
├── logging_config.py        # Configuración del módulo de logging para la observabilidad del proceso.
├── main.py                  # Orquestador del proceso ETL que ejecuta la extracción, transformación y carga.
├── informe_etl.md           # Informe del ejercicio (análisis, arquitectura, preguntas de negocio y conclusiones).
├── Films2.xlsx              # Archivo de datos de entrada.
└── README.md                # Este archivo.
```

## Detalle de Implementación

### Extracción
- **Extractor (`etl/extractor.py`)**:
  - Lee el archivo Excel utilizando **pandas** (la librería `openpyxl` se utiliza internamente) y omite la primera hoja que contiene el MER.
  - Cada hoja se carga en un DataFrame, y se limpian los nombres de las columnas (se eliminan espacios en blanco).
  - Se registran eventos importantes (inicio y fin de la extracción) en el log.

### Transformación
- **Transformer (`etl/transformer.py`)**:
  - Realiza la limpieza de datos en columnas numéricas, eliminando caracteres no numéricos y convirtiendo valores a tipos adecuados (float o int).
  - Valida la integridad referencial entre las tablas, comprobando que las claves foráneas existan en las tablas padre, eliminando registros que no cumplan con esta validación.
  - Se incluyen logs detallados en cada paso (inicio y final de la limpieza, advertencias en validación de claves, etc.) para facilitar la observabilidad.

### Carga
- **Loader (`etl/loader.py`)**:
  - Guarda cada DataFrame transformado en un archivo CSV en la carpeta de salida (por defecto, `output/`).
  - Registra en los logs la ubicación de los archivos guardados.

### Observabilidad
- **Logging:**
  - Se ha configurado un módulo de logging (en `logging_config.py`) que genera un archivo de logs (`logs/etl.log`).
  - Cada módulo del proceso ETL registra eventos importantes, errores y tiempos de ejecución, permitiendo un monitoreo detallado del proceso.

## Dependencias

- **Python 3.x**
- **pandas**
- **openpyxl**

Para instalar las dependencias, puedes usar:
```bash
pip install -r requirements.txt
```

## Ejecución del Proyecto

1. **Preparar el entorno:**  
   - Clona el repositorio y crea un entorno virtual.
   - Instala las dependencias.

2. **Ejecutar el ETL:**  
   - Asegúrate de tener el archivo **Films_2 .xlsx** en la raíz del proyecto.
   - Ejecuta el pipeline:
     ```bash
     python main.py
     ```
   - El proceso registrará los eventos en `logs/etl.log` y generará archivos CSV en la carpeta `output/`.

## Justificación del Diseño

### Arquitectura Modular y SOLID
- **Modularidad:** La separación en módulos (Extractor, Transformer, Loader) facilita el mantenimiento y la escalabilidad del sistema.

### Observabilidad y Calidad de Datos
- **Logging:** Se implementa un sistema de logging para registrar el flujo de ejecución, errores y tiempos de ejecución, lo que es vital para diagnosticar problemas en producción.
- **Validación de Datos:** La fase de transformación incluye validaciones para garantizar que las relaciones entre las tablas sean consistentes y que los datos numéricos sean limpios, asegurando la calidad de la información procesada.

## Posibles Mejoras Futuras
- **Integración con la nube:** Subir los resultados a un bucket para un almacenamiento centralizado y escalable.
- **Visualización:** Integrar dashboards interactivos (por ejemplo, con Power BI) para facilitar la toma de decisiones basadas en los datos procesados.

## Conclusión
Este proyecto ETL demuestra una implementación escalable y modular en Python, siguiendo las mejores prácticas de ingeniería de datos y principios SOLID. La aplicación no solo procesa y limpia los datos, sino que también incorpora mecanismos de observabilidad críticos para monitorear la ejecución y garantizar la calidad de los resultados.
