import abc

import pandas as pd


class BaseTransformer:
    def __init__(self):
        pass

    def transform(self, df) -> pd.DataFrame:
        validated_data = self._initial_validation(df)
        # del data --Optionally delete the variable from memory after use
        transformed_data = self._transform(validated_data)
        # del validated_data
        return self._post_transform_validation(transformed_data)

    @abc.abstractmethod
    def _initial_validation(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError

    @abc.abstractmethod
    def _transform(self, df) -> pd.DataFrame:
        raise NotImplementedError

    @abc.abstractmethod
    def _post_transform_validation(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError


class TransactionTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()

    def _initial_validation(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

    def _transform(self, df) -> pd.DataFrame:
        return df

    def _post_transform_validation(self, df: pd.DataFrame):
        return df


class UsersTransformer(BaseTransformer):
    def __init__(self):
        super().__init__()

    def _initial_validation(self, df: pd.DataFrame):
        return df

    def _transform(self, df) -> pd.DataFrame:
        return df

    def _post_transform_validation(self, df: pd.DataFrame) -> pd.DataFrame:
        return df
