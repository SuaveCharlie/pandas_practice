"""Example runner file to process some imaginary Transaction files"""

from src.enums import DataSource, Exporter, Transformer
from src.pandas_practice.pandas_practice import PandasPractice
from src.utils.parser import Parser


class TransactionsParser(Parser):
    """Subclass of the Parser, adds a program name and an opportunity to add additional CLI arguments"""

    def __init__(self):
        super().__init__(prog_name="Transactions")

    def add_additional_arguments(self) -> None:
        """Method that adds additional CLI arguments"""


if __name__ == "__main__":
    parser = TransactionsParser()

    data_loader = DataSource[parser.arguments.data_location]
    transformer = Transformer[parser.arguments.transformer]
    exporter = Exporter[parser.arguments.exporter]

    PandasPractice(
        data_loader=data_loader.value(),
        transformer=transformer.value(),
        exporter=exporter.value(),
    ).run()
