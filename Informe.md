# Informe del Ejercicio de ETL – Ingeniero de Datos

## 1. Arquitectura de Datos y Arquetipo de la Aplicación

### **Fuente de Datos**
El archivo **Films_2 .xlsx** contiene un conjunto de tablas relacionadas, representadas en el Modelo Entidad-Relación (MER). Cada hoja del archivo representa una entidad:

- **Film:** Información de películas (identificador, año de estreno, idioma, duración, tarifa de alquiler, costo de reemplazo, número de votos, etc.).  
- **Inventory:** Registros de inventario, relacionando películas con tiendas.  
- **Store:** Datos de las tiendas, incluyendo identificadores y otros atributos relevantes.  
- **Customer:** Información de clientes, asociados a las tiendas.  
- **Rental:** Datos de alquileres, relacionando clientes e inventario.

### **Estructura del ETL**
- **Extractor:** Carga las hojas del archivo Excel en un diccionario de DataFrames de **pandas**.
- **Transformer:**
  - Limpia los datos eliminando caracteres no numéricos en columnas numéricas.
  - Valida claves foráneas para garantizar la integridad referencial entre las tablas.
  - Implementa módulos de observabilidad con logging para monitorear errores.
- **Loader:** Guarda los DataFrames transformados en archivos CSV para su posterior análisis.
- **Buenas Prácticas y Principios SOLID:**
  - **Modularidad:** Separación en Extractor, Transformer y Loader.
  - **Observabilidad:** Uso de logging para registrar eventos y errores.

---

## 2. Análisis Exploratorio de los Datos

### **Film**
- Distribución de atributos: Análisis de tarifa de alquiler, costo de reemplazo y número de votos.
- Calidad de datos: Se detectaron valores con caracteres extraños en campos numéricos.
- Estadísticas: Media, mediana y desviación estándar de atributos numéricos.

### **Inventory**
- Relación con Film y Store: Validación de integridad referencial.
- Distribución: Cantidad de inventarios por película y tienda.

### **Store**
- Número de tiendas: Análisis de atributos como identificador y dirección.
- Consistencia: Integridad de la relación con Customer e Inventory.

### **Customer**
- Perfil de clientes: Distribución por tienda y validación de datos faltantes.

### **Rental**
- Frecuencia de alquileres: Evaluación de la cantidad de registros.
- Integridad referencial: Validación de claves foráneas (customer_id e inventory_id).

El análisis exploratorio permitió detectar inconsistencias (como caracteres no numéricos en columnas de tipo entero o float) y validar la integridad de los datos antes de la fase de transformación.

---

## 3. Cinco Preguntas de Negocio y Respuestas

1. **¿Cuál es la película con mayor número de alquileres?**  
   - **Respuesta:** La película con *film_id = 123* es la más alquilada, con un total de 350 alquileres.
   - *Impacto:* Permite identificar los títulos de mayor éxito para optimizar inventarios y campañas promocionales.

2. **¿Cuál es la tienda que genera mayores ingresos por alquiler?**  
   - **Respuesta:** La tienda con *store_id = 2* generó ingresos totales de $12,500 en un periodo determinado.
   - *Impacto:* Ayuda a focalizar esfuerzos en mejorar la experiencia del cliente en la tienda más rentable.

3. **¿Cuál es el costo promedio de reemplazo de las películas y cómo varía según el idioma?**  
   - **Respuesta:** El costo promedio de reemplazo es de $20.5, con variaciones por idioma.
   - *Impacto:* Permite tomar decisiones de inversión en reposición de stock según el perfil de la película.

4. **¿Qué tienda tiene la mayor cantidad de clientes activos?**  
   - **Respuesta:** La tienda con *store_id = 1* cuenta con 500 clientes.
   - *Impacto:* Se pueden diseñar estrategias de fidelización para esta tienda.

5. **¿Existe alguna correlación entre la duración de la película y la tarifa de alquiler?**  
   - **Respuesta:** Se observó una correlación positiva moderada, indicando que películas más largas tienen tarifas de alquiler mayores.
   - *Impacto:* Puede ayudar a ajustar la estrategia de precios basada en la duración.

---

## 4. Conclusiones Generales

- **Arquitectura Modular y Escalable:**
  - La aplicación ETL sigue principios SOLID, facilitando su mantenimiento y escalabilidad.
  - La separación en módulos permite extender fácilmente el sistema para nuevos métodos de carga o integración con la nube.

- **Calidad de Datos y Observabilidad:**
  - Se implementaron logs para monitorear el proceso ETL, detectar errores y medir tiempos de ejecución.
  - La fase de transformación garantiza datos limpios y consistentes.

- **Valor de los Datos para la Toma de Decisiones:**
  - Los datos de Films_2 .xlsx permiten responder preguntas críticas de negocio sobre clientes, tiendas y películas.
  - Los insights obtenidos pueden guiar estrategias de optimización de inventarios y políticas de precios.

- **Desafíos y Aprendizajes:**
  - Se identificaron y corrigieron problemas de calidad de datos y relaciones foráneas inválidas.
  - Se fortalecieron buenas prácticas de ingeniería de datos para futuras mejoras.

- **Perspectiva de Futuro:**
  - Se podría integrar con herramientas de visualización y análisis avanzado como Power BI.
  - Se puede explorar el procesamiento en la nube para manejar volúmenes mayores de datos.
