import pandas as pd
import pytest
from dataframe_handlers import get_handler

data_A = [1, 2, 3, 4, 5]
data_B = ["foo", "bar", "foo", "baz", "qux"]
data_C = [True, False, True, True, False]

test_data = {
    "A": data_A,
    "B": data_B,
    "C": data_C,
}

test_pandas_df = pd.DataFrame(test_data)


class DataFrameHandlerTestBase:
    @pytest.fixture
    def handler(self, data):
        return get_handler(data)

    @pytest.fixture
    def data(self):
        pass

    @staticmethod
    def test_get_unique(handler):
        unique_values = handler.get_unique("B")
        expected_values = ["foo", "bar", "baz", "qux"]
        assert set(unique_values) == set(expected_values)

    @staticmethod
    def test_get_value_counts(handler):
        value_counts = handler.get_value_counts("B")
        expected_counts = pd.DataFrame(
            {"value": ["foo", "bar", "baz", "qux"], "count": [2, 1, 1, 1]},
        )
        pd.testing.assert_frame_equal(
            pd.DataFrame(value_counts).sort_values("value").reset_index(drop=True),
            expected_counts.sort_values("value").reset_index(drop=True),
        )

    @staticmethod
    def test_get_data_range(handler):
        data_range = handler.get_data_range("A")
        expected_range = (1, 5)
        assert tuple(data_range) == expected_range

    @staticmethod
    def test_get_missing_filter(handler):
        missing_filter = list(handler.get_missing_filter("B"))
        expected_filter = [False, False, False, False, False]
        assert missing_filter == expected_filter

    @staticmethod
    def test_get_value_filter(handler):
        value_filter = list(handler.get_value_filter("B", ["foo", "baz"]))
        expected_filter = [True, False, True, True, False]
        assert value_filter == expected_filter

    @staticmethod
    def test_get_columns(handler):
        columns = handler.get_columns()
        expected_columns = ["A", "B", "C"]
        assert set(columns) == set(expected_columns)

    @staticmethod
    def test_get_numeric_columns(handler):
        numeric_columns = list(handler.get_numeric_columns())
        expected_columns = ["A"]
        assert numeric_columns == expected_columns

    @staticmethod
    def test_get_column_types(handler):
        column_types = dict(handler.get_column_types())
        expected_types = {"A": int, "B": str, "C": bool}
        assert column_types == expected_types
