import pytest

from . import DataFrameHandlerTestBase, test_pandas_df
from ..pandas_handler import PandasDataFrameHandler


class TestPandasDataFrameHandler(DataFrameHandlerTestBase):
    @pytest.fixture
    def data(self):
        return test_pandas_df
