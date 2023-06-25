import pandas as pd

from .base import BaseDataFrameHandler
from typing import Optional


class PandasDataFrameHandler(BaseDataFrameHandler):
    df: pd.DataFrame

    def __init__(self, df: pd.DataFrame):
        super().__init__(df)

    def get_unique(self, column: str, limit: Optional[int] = None) -> list:
        return self.df[column].unique()[:limit].tolist()

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
        return value_counts_df if limit is None else value_counts_df.head(limit)

    def get_data_range(self, column: str) -> tuple:
        return tuple(self.df[column].describe()[["min", "max"]])

    def get_missing_filter(self, column: str) -> pd.Series:
        return self.df[column].isna()

    def get_value_filter(
        self,
        column: str,
        values: list,
        invert: bool = False,
    ) -> pd.Series:
        _filter = self.df[column].isin(values)
        return ~_filter if invert else _filter

    def get_columns(self) -> list[str]:
        return self.df.columns.tolist()

    def get_numeric_columns(self) -> list[str]:
        return self.df.select_dtypes(include=["number"]).columns.tolist()

    def get_column_types(self, default_str: bool = True) -> dict:
        dtype_dict = {
            "i": int,
            "u": int,
            "f": float,
            "b": bool,
        }
        return self.df.dtypes.apply(
            lambda dtype: dtype_dict.get(
                dtype.kind,
                str if default_str else dtype,
            ),
        ).to_dict()
