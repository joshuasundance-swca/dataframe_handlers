# import pytest
# import vaex
# import xarray as xr
#
# from . import DataFrameHandlerTestBase, test_pandas_df
# from ..vaex_handler import VaexDataFrameHandler
#
#
# class TestXarrayDataFrameHandler(DataFrameHandlerTestBase):
#     @pytest.fixture
#     def data(self):
#         return xr.Dataset.from_dataframe(test_pandas_df)
#
#     def create_handler(self, data):
#         return XarrayDataFrameHandler(data)
#
# class TestVaexDataFrameHandler(DataFrameHandlerTestBase):
#     @pytest.fixture
#     def data(self):
#         return vaex.from_pandas(test_pandas_df)
