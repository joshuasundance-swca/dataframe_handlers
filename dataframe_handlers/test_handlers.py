import dask.dataframe as dd
import pandas as pd
import pytest

# import numpy as np
# import xarray as xr
# import vaex

from . import (
    PandasDataFrameHandler,
    DaskDataFrameHandler,
    # VaexDataFrameHandler,
    # XarrayDataFrameHandler
)

data_A = [1, 2, 3, 4, 5]
data_B = ["foo", "bar", "foo", "baz", "qux"]
data_C = [True, False, True, True, False]


class DataFrameHandlerTestBase:
    @pytest.fixture
    def handler(self, data):
        return self.create_handler(data)

    @pytest.fixture
    def data(self):
        pass

    def create_handler(self, data):
        pass

    @staticmethod
    def test_get_unique(handler):
        unique_values = handler.get_unique("B")
        expected_values = ["foo", "bar", "baz", "qux"]
        assert unique_values == expected_values

    @staticmethod
    def test_get_value_counts(handler):
        value_counts = handler.get_value_counts("B")
        # expected_counts = [('foo', 2), ('bar', 1), ('baz', 1), ('qux', 1)]
        expected_counts = pd.DataFrame(
            {"value": ["foo", "bar", "baz", "qux"], "count": [2, 1, 1, 1]},
        )
        pd.testing.assert_frame_equal(value_counts, expected_counts)

    @staticmethod
    def test_get_data_range(handler):
        data_range = handler.get_data_range("A")
        expected_range = (1, 5)
        assert data_range == expected_range

    @staticmethod
    def test_get_missing_filter(handler):
        missing_filter = pd.Series(handler.get_missing_filter("B"))
        expected_filter = pd.Series([False, False, False, False, False])
        pd.testing.assert_series_equal(
            missing_filter,
            expected_filter,
            check_names=False,
        )

    @staticmethod
    def test_get_value_filter(handler):
        value_filter = pd.Series(handler.get_value_filter("B", ["foo", "baz"]))
        expected_filter = pd.Series([True, False, True, True, False])
        pd.testing.assert_series_equal(value_filter, expected_filter, check_names=False)

    @staticmethod
    def test_get_columns(handler):
        columns = handler.get_columns()
        expected_columns = ["A", "B", "C"]
        assert columns == expected_columns

    @staticmethod
    def test_get_numeric_columns(handler):
        numeric_columns = handler.get_numeric_columns()
        expected_columns = ["A"]
        assert numeric_columns == expected_columns

    @staticmethod
    def test_get_column_types(handler):
        column_types = handler.get_column_types()
        expected_types = {"A": int, "B": str, "C": bool}
        assert column_types == expected_types


class TestPandasDataFrameHandler(DataFrameHandlerTestBase):
    @pytest.fixture
    def data(self):
        data = {
            "A": data_A,
            "B": data_B,
            "C": data_C,
        }
        return pd.DataFrame(data)

    def create_handler(self, data):
        return PandasDataFrameHandler(data)


class TestDaskDataFrameHandler(DataFrameHandlerTestBase):
    @pytest.fixture
    def data(self):
        data = {
            "A": data_A,
            "B": data_B,
            "C": data_C,
        }
        df = pd.DataFrame(data)
        return dd.from_pandas(df, npartitions=2)

    def create_handler(self, data):
        return DaskDataFrameHandler(data)


# class TestVaexDataFrameHandler(DataFrameHandlerTestBase):
#     @pytest.fixture
#     def data(self):
#         data = {
#             'A': data_A,
#             'B': data_B,
#             'C': data_C
#         }
#         return vaex.from_pandas(pd.DataFrame(data))
#
#     def create_handler(self, data):
#         return VaexDataFrameHandler(data)


# class TestXarrayDataFrameHandler:
#     @pytest.fixture
#     def sample_data(self):
#         data = np.array(list(zip(data_A, data_B, data_C)))
#         da = xr.DataArray(
#             data,
#             coords={
#                 'idx': np.arange(data.shape[0]),
#                 'column': list("ABC")
#             },
#             dims=['idx', 'column']
#         )
#         return da
#
#     @pytest.fixture
#     def handler(self, sample_data):
#         return XarrayDataFrameHandler(sample_data)
#
#     def test_get_unique(self, handler):
#         unique_values = handler.get_unique('B')
#         expected_values = ['foo', 'bar', 'baz', 'qux']
#         assert sorted(unique_values) == sorted(expected_values)
#
#     def test_get_value_counts(self, handler):
#         value_counts = handler.get_value_counts('B')
#         expected_counts = [('foo', 2), ('bar', 1), ('baz', 1), ('qux', 1)]
#         assert sorted(value_counts) == sorted(expected_counts)
#
#     def test_get_data_range(self, handler):
#         data_range = handler.get_data_range('A')
#         expected_range = (1.0, 5.0)
#         assert data_range == expected_range
#
#     def test_get_missing_filter(self, handler):
#         missing_filter = handler.get_missing_filter('B')
#         expected_filter = xr.DataArray([False, False, False, False, False], dims='dim')
#         assert xr.testing.assert_equal(missing_filter, expected_filter)
#
#     def test_get_value_filter(self, handler):
#         value_filter = handler.get_value_filter('B', ['foo', 'baz'])
#         expected_filter = xr.DataArray([True, False, True, True, False], dims='dim')
#         assert xr.testing.assert_equal(value_filter, expected_filter)
#
#     def test_get_columns(self, handler):
#         columns = handler.get_columns()
#         expected_columns = ['A', 'B', 'C']
#         assert sorted(columns) == sorted(expected_columns)
#
#     def test_get_numeric_columns(self, handler):
#         numeric_columns = handler.get_numeric_columns()
#         expected_columns = ['A']
#         assert sorted(numeric_columns) == sorted(expected_columns)
#
#     def test_get_column_types(self, handler):
#         column_types = handler.get_column_types()
#         expected_types = {'A': int, 'B': str, 'C': bool}
#         assert column_types == expected_types


if __name__ == "__main__":
    pytest.main([__file__])
