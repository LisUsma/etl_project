import pandas as pd
import re
import logging
from logging_config import logger

class Transformer:
    def __init__(self):
        # Columnas que solo deben contener números
        self.numeric_columns = {
            "customer": ["customer_id", "store_id", "address_id"],
            "store": ["store_id", "manager_staff_id", "address_id"],
            "film": ["film_id", "release_year", "language_id", "rental_duration", "rental_rate", "length", "replacement_cost", "num_voted_users"],
            "inventory": ["inventory_id", "film_id", "store_id"],
            "rental": ["rental_id", "customer_id", "inventory_id", "staff_id"]
        }

        # Relaciones entre tablas (FK → PK)
        self.relations = [
            ("inventory", "film_id", "film", "film_id"),
            ("inventory", "store_id", "store", "store_id"),
            ("customer", "store_id", "store", "store_id"),
            ("rental", "customer_id", "customer", "customer_id"),
            ("rental", "inventory_id", "inventory", "inventory_id"),
        ]

    def clean_numeric_columns(self, data):
        """ Elimina caracteres no numéricos. """
        logger.info("Iniciando limpieza.")
        cleaned_data = {}
        
        # Definir qué columnas deben mantenerse como float
        float_columns = {
            "film": ["rental_rate", "replacement_cost"],
        }

        for table, df in data.items():
            cleaned_df = df.copy()
            
            if table in self.numeric_columns:
                for col in self.numeric_columns[table]:
                    if col in cleaned_df:
                        if table in float_columns and col in float_columns[table]:
                            # Si la columna es float, limpiamos sin cambiar su tipo
                            cleaned_df[col] = (
                                cleaned_df[col]
                                .astype(str)
                                .apply(lambda x: re.sub(r'[^\d.]', '', x) if pd.notna(x) else x)  # Mantiene los decimales
                                .astype(float)  # Convierte a float de nuevo
                            )
                        else:
                            # Para las demás columnas numéricas, limpiamos y las dejamos como string o int
                            cleaned_df[col] = (
                                cleaned_df[col]
                                .astype(str)
                                .apply(lambda x: re.sub(r'\D', '', x) if pd.notna(x) else x)  # Solo números enteros
                                .replace('', '0')  # Reemplaza vacíos por "0"
                            )

            cleaned_data[table] = cleaned_df

        logger.info("Limpieza completa.")
        return cleaned_data

    def validate_foreign_keys(self, data):
        """ Validación claves foráneas. """
        logger.info("Iniciando validación de claves foráneas.")
        cleaned_data = {k: v.copy() for k, v in data.items()}  # Copia para no modificar la original

        for child_table, foreign_key, parent_table, primary_key in self.relations:
            if child_table in cleaned_data and parent_table in cleaned_data:
                fk_values = set(cleaned_data[child_table][foreign_key].dropna().unique())
                pk_values = set(cleaned_data[parent_table][primary_key].dropna().unique())

                missing_keys = fk_values - pk_values
                if missing_keys:
                    logger.warning(f"{len(missing_keys)} claves en '{child_table}.{foreign_key}' no existen en '{parent_table}.{primary_key}'. Se eliminarán.")
                    cleaned_data[child_table] = cleaned_data[child_table][cleaned_data[child_table][foreign_key].isin(pk_values)]
                else:
                    logger.info(f"Validación de '{child_table}.{foreign_key}' exitosa.")

        logger.info("Validación de claves foráneas finalizada.")
        return cleaned_data

    def transform(self, data):
        logger.info("Iniciando transformación de datos.")
        cleaned_data = self.clean_numeric_columns(data)
        cleaned_data = self.validate_foreign_keys(cleaned_data)
        logger.info("Transformación de datos completada.")
        return cleaned_data