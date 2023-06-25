This README was produced by [Anthropic's Claude LLM](https://www.anthropic.com/product)

# dataframe_handlers

`dataframe_handlers` aims to provide an abstract base class and concrete implementations for handling and manipulating dataframes of various types in Python.
While the interface may be applicable to many use cases, the immediate goal is to standardize interaction with dataframe libraries and enable interoperability between them in the context of the [Solara](https://solara.dev) Python library, which can be used to create reactive web apps using pure Python.


## Installation

```
# TODO
# pip install .
```

## Usage

The base class, `BaseDataFrameHandler`, defines an abstract interface with the following methods:

- `get_unique(self, column: str, limit: Optional[int] = None) -> Collection`
- `get_value_counts(column: str, limit: Optional[int] = None) -> Mapping[str, int]`
- `get_data_range(self, column: str) -> Sequence`
- `get_missing_filter(self, column: str) -> Sequence[bool]`
- `get_value_filter(column: str, values: list, invert: bool = False) -> Sequence[bool]:`
- `get_columns(self) -> Collection[str]`
- `get_numeric_columns(self) -> Collection[str]`
- `get_column_types(default_str: bool = True) -> Mapping[str, Union[object, type, str]]`

Concrete implementations of this interface exist for:

- Pandas (`PandasDataFrameHandler`)
- Dask (`DaskHandler`)
- Xarray (`XarrayHandler`)
- Vaex (`VaexHandler`, *currently disabled*)

To use a handler, simply instantiate it passing your dataframe:

```python
import pandas as pd
from dataframe_handlers import PandasDataFrameHandler

df = pd.DataFrame({'A': [1, 2, 3]})
handler = PandasDataFrameHandler(df)

columns = handler.get_columns()
# ['A']
```

Libraries built on the `dataframe_handlers` interface can then support multiple dataframe types interchangeably.

## Contributing

There are a few ways you can contribute to `dataframe_handlers` and help guide its future:

1. Add support for another dataframe library by implementing a new concrete handler class. This helps expand the scope of the project and allows it to support new use cases.

2. Improve or expand the abstract base interface. As new methods are identified to broadly support dataframe interaction and manipulation, the interface can be expanded. However, we aim to keep the interface as concise as possible to facilitate implementation for many types. **User feedback on what methods/functionality would be most useful to support is appreciated!**

3. Improve existing concrete implementations. More comprehensive testing, performance optimizations and support for newer library versions all help improve the quality of the project.

4. Improve documentation. Additional details on implementing new handlers, more examples, and type hints help make the project more contributor-friendly.

5. Improve validation. Stricter checks that subclasses implement the required methods, consistent method signatures, and edge case testing all help users build on the interface.

**We aim for `dataframe_handlers` to be a community project guided by user needs and feedback.** Please feel free to open issues to propose new ideas, give feedback on the direction of the project or interface design, or submit pull requests with your contributions and improvements!

## License

`dataframe_handlers` is licensed under the MIT license. See the LICENSE file for details.
