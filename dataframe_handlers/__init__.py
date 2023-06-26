from .base import BaseDataFrameHandler

__all__ = ["BaseDataFrameHandler"]

dispatch_dict = {}

try:
    import pandas as pd
    from .pandas_handler import PandasDataFrameHandler

    __all__.append("PandasDataFrameHandler")
    dispatch_dict[pd.DataFrame] = PandasDataFrameHandler

except ImportError:
    pass

try:
    import dask.dataframe as dd
    from .dask_handler import DaskDataFrameHandler

    __all__.append("DaskDataFrameHandler")
    dispatch_dict[dd.DataFrame] = DaskDataFrameHandler
except ImportError:
    pass

try:
    import xarray as xr
    from .xarray_handler import XarrayDataFrameHandler

    __all__.append("XarrayDataFrameHandler")
    dispatch_dict[xr.Dataset] = XarrayDataFrameHandler
except ImportError:
    pass

# try:
#     import vaex
#     from .vaex_handler import VaexDataFrameHandler
#
#     __all__.append("VaexDataFrameHandler")
#     dispatch_dict[vaex.dataframe.DataFrame] = VaexDataFrameHandler
# except ImportError:
#     pass


def get_handler(df, handler_type=None):
    if handler_type is not None:
        return handler_type(df)
    for df_type, df_handler in dispatch_dict.items():
        if isinstance(df, df_type):
            return df_handler(df)


__all__.append("dispatch_dict")
__all__.append("get_handler")
