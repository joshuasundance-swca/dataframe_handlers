import dask.dataframe as dd
import pandas as pd
from typing import Optional
from .pandas_handler import PandasDataFrameHandler


class DaskDataFrameHandler(PandasDataFrameHandler):
    df: dd.DataFrame

    def __init__(self, df: dd.DataFrame):
        super().__init__(df)

    def get_unique(self, column: str, limit: Optional[int] = None) -> list:
        unique_values = self.df[column].unique().compute()
        return (
            unique_values[:limit].tolist()
            if limit is not None
            else unique_values.tolist()
        )

    def get_value_counts(
        self,
        column: str,
        limit: Optional[int] = None,
    ) -> pd.DataFrame:
        value_counts_df = (
            self.df[column]
            .value_counts(dropna=False)
            .reset_index(drop=False)
            .rename(
                columns={
                    column: "value",
                },
            )
        )
        value_counts_df = (
            value_counts_df if limit is None else value_counts_df.head(limit)
        )
        return value_counts_df.compute()

    def get_data_range(self, column: str) -> tuple:
        min_value, max_value = (
            self.df[column].min().compute(),
            self.df[column].max().compute(),
        )
        return min_value, max_value

    def get_missing_filter(self, column: str) -> dd.Series:
        return self.df[column].isna()

    def get_value_filter(
        self,
        column: str,
        values: list,
        invert: bool = False,
    ) -> dd.Series:
        _filter = self.df[column].isin(values)
        return ~_filter if invert else _filter
