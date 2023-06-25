from .base import BaseDataFrameHandler

__all__ = ["BaseDataFrameHandler"]

try:
    from .pandas_handler import PandasDataFrameHandler

    __all__.append("PandasDataFrameHandler")

except ImportError:
    pass

try:
    from .dask_handler import DaskDataFrameHandler

    __all__.append("DaskDataFrameHandler")
except ImportError:
    pass

try:
    from .xarray_handler import XarrayDataFrameHandler

    __all__.append("XarrayDataFrameHandler")
except ImportError:
    pass

# try:
#     from .vaex_handler import VaexDataFrameHandler
#
#     __all__.append("VaexDataFrameHandler")
# except ImportError:
#     pass
