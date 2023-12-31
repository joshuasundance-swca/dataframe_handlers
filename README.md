This README was produced by [Anthropic's Claude LLM](https://www.anthropic.com/product)

# dataframe_handlers

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
![Test coverage](./coverage.svg)


`dataframe_handlers` aims to provide an abstract base class and concrete implementations for handling and manipulating dataframes of various types in Python.
While the interface may be applicable to many use cases, the immediate goal is to standardize interaction with dataframe libraries and enable interoperability between them in the context of the [Solara](https://solara.dev) Python library, which can be used to create reactive web apps using pure Python.


## Installation

https://pypi.org/project/dataframe-handlers

```bash
# any of the following

pip install dataframe-handlers
pip install dataframe-handlers[pandas]
pip install dataframe-handlers[dask]
pip install dataframe-handlers[xarray]
# pip install dataframe-handlers[vaex]
pip install dataframe-handlers[testing]

pip install dataframe-handlers[pandas,xarray,testing]
```

## Usage

The base class, `BaseDataFrameHandler`, defines an abstract interface with the following methods:

- `get_unique(column: str, limit: Optional[int] = None) -> Collection`
- `get_value_counts(column: str, limit: Optional[int] = None) -> Mapping[str, int]`
- `get_data_range(column: str) -> Sequence`
- `get_missing_filter(column: str) -> Sequence[bool]`
- `get_value_filter(column: str, values: list, invert: bool = False) -> Sequence[bool]`
- `get_columns() -> Collection[str]`
- `get_numeric_columns() -> Collection[str]`
- `get_column_types(default_str: bool = True) -> Mapping[str, Union[object, type, str]]`

Concrete implementations of this interface exist for:

- Pandas (`PandasDataFrameHandler`)
- Dask (`DaskDataFrameHandler`)
- Xarray (`XarrayDataFrameHandler`)
- Vaex (`VaexDataFrameHandler`, *currently disabled*)

The easiest way to get a handler does not require knowing what type of dataframe you're dealing with.

You can do this by using `dataframe_handlers.get_handler`, which will return a handler of the appropriate type based on the type of dataframe it is given.

```python
import pandas as pd
from dataframe_handlers import get_handler

df = pd.DataFrame({'A': [1, 2, 3]})
handler = get_handler(df)

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

**We aim for `dataframe_handlers` to be a community project guided by user needs and feedback.** Please feel free to open issues or start a discussion to propose new ideas, give feedback on the direction of the project or interface design, or submit pull requests with your contributions and improvements!

For specific instructions, please see `CONTRIBUTING.md`.


## License

`dataframe_handlers` is licensed under the MIT license. See the LICENSE file for details.
