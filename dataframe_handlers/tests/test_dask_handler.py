import dask.dataframe as dd
import pytest

from . import DataFrameHandlerTestBase, test_pandas_df
from ..dask_handler import DaskDataFrameHandler


class TestDaskDataFrameHandler(DataFrameHandlerTestBase):
    @pytest.fixture
    def data(self):
        return dd.from_pandas(test_pandas_df, npartitions=2)

    def create_handler(self, data):
        return DaskDataFrameHandler(data)
