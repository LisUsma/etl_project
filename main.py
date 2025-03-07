import time
from etl.extractor import Extractor
from etl.transformer import Transformer
from etl.loader import Loader
from logging_config import logger

file_path = "Films_2 .xlsx"

extractor = Extractor(file_path)
transformer = Transformer()
loader = Loader(output_folder="output")

start_time = time.time()

logger.info("Iniciando proceso ETL.")

data = extractor.extract_data()
if data:
    clean_data = transformer.transform(data)
    loader.save_to_csv(clean_data) 
    logger.info("Proceso ETL finalizado con éxito.")
else:
    logger.error("Error en la extracción de datos. No se puede continuar con el ETL.")

# Calcular tiempo total
end_time = time.time()
execution_time = round(end_time - start_time, 2)
logger.info(f"Tiempo total de ejecución: {execution_time} segundos.")
