# import xarray as xr
# from typing import Optional
# from .base import BaseDataFrameHandler
#
#
# class XarrayDataFrameHandler(BaseDataFrameHandler):
#     df: xr.DataArray
#
#     def __init__(self, df: xr.DataArray):
#         super().__init__(df)
#
#     def get_unique(self, column: str, limit: Optional[int] = None) -> list:
#         unique_values = self.df[column].values
#         unique_values = list(set(unique_values))
#         return unique_values[:limit] if limit is not None else unique_values
#
#     def get_value_counts(self, column: str, limit: Optional[int] = None) -> xr.DataArray:
#         value_counts = self.df[column].value_counts()
#         if limit is not None:
#             value_counts = value_counts[:limit]
#         return value_counts
#
#     def get_data_range(self, column: str) -> tuple:
#         min_value = float(self.df[column].min().values)
#         max_value = float(self.df[column].max().values)
#         return min_value, max_value
#
#     def get_missing_filter(self, column: str) -> xr.DataArray:
#         missing_filter = xr.where(self.df[column].isnull(), True, False)
#         return missing_filter
#
#     def get_value_filter(self, column: str, values: list, invert: bool = False) -> xr.DataArray:
#         value_filter = self.df[column].isin(values)
#         if invert:
#             value_filter = ~value_filter
#         return value_filter
#
#     def get_columns(self) -> list[str]:
#         return list(self.df.dims)
#
#     def get_numeric_columns(self) -> list[str]:
#         numeric_columns = [
#             column for column in self.df.dims
#             if self.df[column].dtype.kind in ['i', 'u', 'f']
#         ]
#         return numeric_columns
#
#     def get_column_types(self, default_str: bool = True) -> dict:
#         dtype_dict = {
#             'i': int,
#             'u': int,
#             'f': float,
#             'b': bool,
#             'M': 'datetime64[ns]'
#         }
#         column_types = {
#             column: dtype_dict.get(self.df[column].dtype.kind, str if default_str else self.df[column].dtype)
#             for column in self.df.coords.keys()
#         }
#         return column_types
