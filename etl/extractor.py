import pandas as pd
import logging
from logging_config import logger

class Extractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_data(self):
        """Cargar archivo excel."""
        try:
            xls = pd.ExcelFile(self.file_path)
            sheet_names = xls.sheet_names[1:]
            data = {sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in sheet_names}

            for sheet in data:
                data[sheet].columns = data[sheet].columns.str.strip()

            logger.info(f"Extracción completada. {len(data)} hojas procesadas.")
            return data
        except Exception as e:
            logger.error(f"Error en la extracción: {e}")
            return None