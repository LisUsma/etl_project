import os
import pandas as pd
import logging
from logging_config import logger

class Loader:
    def __init__(self, output_folder="output"):
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def save_to_csv(self, data):
        """Guardado en archivos CSV."""
        logger.info("Iniciando guardado en CSV.")
        for table_name, df in data.items():
            file_path = os.path.join(self.output_folder, f"{table_name}.csv")
            df.to_csv(file_path, index=False)
            logger.info(f"Datos guardados en {file_path}")

        logger.info("Guardado completado.")
