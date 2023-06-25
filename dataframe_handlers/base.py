import xarray as xr
import abc
import pandas as pd
from typing import Optional, Union
import dask.dataframe as dd

SUPPORTED_DFS = Union[
    pd.DataFrame,
    # "geopandas.GeoDataFrame",
    # "vaex.dataframe.DataFrame",
    dd.DataFrame,
    xr.DataArray,
]


class BaseDataFrameHandler(abc.ABC):
    def __init__(self, df: SUPPORTED_DFS):
        """
        Initialize DataFrameHandler.

        Args:
            df: DataFrame object to be handled.
        """
        self.df = df

    @abc.abstractmethod
    def get_unique(self, column: str, limit: Optional[int] = None) -> list:
        """
        Get unique values in a column of the DataFrame.

        Args:
            column: Name of the column.
            limit: Maximum number of unique values to return.

        Returns:
            List of unique values.
        """
        pass

    @abc.abstractmethod
    def get_value_counts(
        self,
        column: str,
        limit: Optional[int] = None,
    ) -> pd.DataFrame:
        """
        Count the occurrences of each value in a column of the DataFrame.

        Args:
            column: Name of the column.
            limit: Maximum number of value counts to return.

        Returns:
            DataFrame with value counts.
        """
        pass

    @abc.abstractmethod
    def get_data_range(self, column: str) -> tuple:
        """
        Get the minimum and maximum values in a column of the DataFrame.

        Args:
            column: Name of the column.

        Returns:
            Tuple containing the minimum and maximum values.
        """
        pass

    @abc.abstractmethod
    def get_missing_filter(self, column: str) -> pd.Series:
        """
        Filter the DataFrame based on missing values in a column.

        Args:
            column: Name of the column.

        Returns:
            Boolean Series indicating missing values.
        """
        pass

    @abc.abstractmethod
    def get_value_filter(
        self,
        column: str,
        values: list,
        invert: bool = False,
    ) -> pd.Series:
        """
        Filter the DataFrame based on specified values in a column.

        Args:
            column: Name of the column.
            values: List of values to filter on.
            invert: Flag indicating whether to invert the filter.

        Returns:
            Boolean Series indicating the filtered rows.
        """
        pass

    @abc.abstractmethod
    def get_columns(self) -> list[str]:
        pass

    @abc.abstractmethod
    def get_numeric_columns(self) -> list[str]:
        pass

    @abc.abstractmethod
    def get_column_types(self, default_str: bool = True) -> dict:
        """
        Get the types of columns in the DataFrame.

        Args:
            default_str: If not numeric or bool, default to str.

        Returns:
            Dictionary mapping column names to their types.
        """
        pass
