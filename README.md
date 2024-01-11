# plotlyplus

## Introduction
`plotlyplus` is a Python module that simplify the calling of plotly.express function. In standard way, one needs to do the following to create a plot using plotly.express based on a dataframe, df, you need to do the following

```python
import pandas as pd
import plotly.express as px

px.scatter(df, x='namex',y='namey')
```
The plotlyplus package add the plotly.express plotting methods to the pandas dataframe class. This will simply the call to the plotting function as:

```python
from plotlyplus.plotlyplus import *

df.scatter(x='namex',y='namey')
```
This is a small and almost trivial tweak, but brings a lot of convenience in daily practical work. Enjoy!

## Key Features
- **Better integration of plotly.express functions to pandas dataframe**: Directly integrates Plotly Express plotting functions with pandas DataFrames.
- **Safe mode**: To avoid naming conflicts, `plotlyplus` introduces a 'safe mode' (`plotlyplus_safe`). In this mode, each plotly.express function is prefixed with `px_``, ensuring namespace integrity at the cost of slightly reduced convenience.

## Installation
Install `PlotlyPlus` using pip with the following command:
```bash
pip install plotlyplus
```

## Usage

### Standard Mode
All plotly.express fundtions become methods of pandas dataframe.

```python
from plotlyplus.plotlyplus import *

df = pd.DataFrame(...)
fig = df.bar(...)  # Plotly Express function as a DataFrame method
fig.show()
```

### Safe Mode
This mode prefixes the Plotly Express functions with `px_` to minimize namespace conflicts.

```python
from plotlyplus.plotlyplus_safe import *

df = pd.DataFrame(...)
fig = df.px_bar(...)  # Plotly Express function as a DataFrame method
fig.show()
```

## Contributing

Contributions to PlotlyPlus are welcome. Please feel free to submit pull requests, report bugs, or suggest features.


## License

PlotlyPlus is made available under the MIT License.
