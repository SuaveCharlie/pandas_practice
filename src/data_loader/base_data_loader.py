import abc

import pandas as pd

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     import pandas as pd


class BaseDataLoader:
    """
    Class for loading data from different locations

    Uses abstract methods to implement the different loaders;
    - Checking that the data is accessible - credentials and/or file location
    - Implemented loading method
    """

    def __init__(self):
        pass

    def load_data(self, *args, **kwargs):
        self._validate_data_location(*args, **kwargs)
        return self._load_data(*args, **kwargs)

    @abc.abstractmethod
    def _validate_data_location(self, *args, **kwargs) -> None:
        """
        Checks that the data can be accessed; different loaders will require different checks
        """
        raise NotImplementedError("This is the base class!")

    @abc.abstractmethod
    def _load_data(self, *args, **kwargs) -> pd.DataFrame:
        raise NotImplementedError("This is the base class!")


class DBLoader(BaseDataLoader):
    def __init__(self):
        super().__init__()

    def _validate_data_location(self, *args, **kwargs) -> None:
        """Checks that the database can be accessed and that the table exists"""

    def _load_data(self, *args, **kwargs) -> pd.DataFrame:
        pass


class S3Loader(BaseDataLoader):
    def __init__(self):
        super().__init__()

    def _validate_data_location(self, *args, **kwargs) -> None:
        """Checks that the S3 credentials exist"""

    def _load_data(self, *args, **kwargs) -> pd.DataFrame:
        pass


class LocalLoader(BaseDataLoader):
    def __init__(self):
        super().__init__()

    def _validate_data_location(self, *args, **kwargs) -> None:
        """Checks that the local file exists"""

    def _load_data(self, *args, **kwargs) -> pd.DataFrame:
        pass


class APILoader(BaseDataLoader):
    def __init__(self):
        super().__init__()

    def _validate_data_location(self, *args, **kwargs) -> None:
        """Checks that the credentials for the remote API exist"""

    def _load_data(self, *args, **kwargs) -> pd.DataFrame:
        pass
