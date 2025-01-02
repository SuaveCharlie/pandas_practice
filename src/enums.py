"""Enums used to point programmatically at classes, used for instantiation"""

from enum import Enum

from src.data_loader.base_data_loader import DBLoader, LocalLoader, S3Loader
from src.export.base_exporter import CSVExporter
from src.transformers.base_transformer import TransactionTransformer, UsersTransformer


class DataSource(Enum):
    """The different Data Source locations"""

    S3 = S3Loader
    LOCAL = LocalLoader
    DATABASE = DBLoader


class Transformer(Enum):
    """The dataset specific transformation classes"""

    TRANSACTIONS = TransactionTransformer
    USERS = UsersTransformer


class Exporter(Enum):
    """The destination specific exporter classes"""

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
