import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/etl.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger("ETL")
