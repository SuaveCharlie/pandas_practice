from enum import Enum

from src.data_loader.base_data_loader import DBLoader, LocalLoader, S3Loader
from src.export.base_exporter import CSVExporter
from src.transformers.base_transformer import TransactionTransformer, UsersTransformer


class DataSource(Enum):
    S3 = S3Loader
    LOCAL = LocalLoader
    DATABASE = DBLoader


class Transformer(Enum):
    TRANSACTIONS = TransactionTransformer
    USERS = UsersTransformer


class Exporter(Enum):
    CSV = CSVExporter


class DataType(Enum):
    INTEGER = "INTEGER"
    REAL = "REAL"
    BOOLEAN = "BOOLEAN"
    STRING = "STRING"
    DATE = "DATE"
    TIME = "TIME"
    DATETIME = "DATETIME"
    TIMESTAMP = "TIMESTAMP"
