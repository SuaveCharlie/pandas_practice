import abc
import logging
from argparse import ArgumentParser

from dotenv import load_dotenv

from src.enums import DataSource, Exporter, Transformer
from src.utils.logger import get_logger


class Parser:
    """
    Base Parser class that sets up a logger and allows for additional arguments to be added and parsed
    If additional arguments are required, inherit from this class and implement `add_additional_arguments`
    """

    def __init__(self, prog_name: str, prog_desc: str = None):
        get_logger()
        load_dotenv()

        self.prog_name = prog_name
        self.desc = prog_desc
        self._parser = None

        self.set_arguments()

    def set_arguments(self) -> None:
        """Adds the base and any additional arguments to the parser"""
        logging.info("Adding base arguments to parser")
        self.parser.add_argument(
            "--data_location",
            default="LOCAL",
            help="Location of the dataset",
            type=str,
            action="store",
            choices=DataSource.__members__.keys(),
            required=True,
        )
        self.parser.add_argument(
            "--transformer",
            default="TRANSACTION",
            help="Transformer to use",
            type=str,
            action="store",
            choices=Transformer.__members__.keys(),
            required=True,
        )
        self.parser.add_argument(
            "--exporter",
            default="CSV",
            help="Exporter to use",
            action="store",
            choices=Exporter.__members__.keys(),
            type=str,
            required=True,
        )

        try:
            logging.info("Attempting to add any additional arguments")
            self.add_additional_arguments()

        except NotImplementedError:
            logging.warning("Additional arguments not implemented, only base arguments present")

    @property
    def parser(self) -> ArgumentParser:
        """
        ArgumentParser object that can accept arguments when calling a script and pass them into other objects
        """

        if self._parser is None:
            self.parser = ArgumentParser(prog=self.prog_name, description=self.desc)
        return self._parser

    @parser.setter
    def parser(self, value: ArgumentParser) -> None:
        self._parser = value

    @abc.abstractmethod
    def add_additional_arguments(self) -> None:
        """
        Method for adding the program specific arguments to be added
        """
        raise NotImplementedError

    @property
    def arguments(self):
        """Parsed arguments"""
        return self.parser.parse_args()
