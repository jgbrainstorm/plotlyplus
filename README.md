# PlotlyPlus Module

## Introduction
`PlotlyPlus` is a streamlined Python module that seamlessly integrates Plotly Express plotting functions into pandas DataFrames. This tool is designed to enhance the ease and efficiency of visualizing data directly from pandas.

## Key Features
- **Seamless Plotly Express Integration**: Directly integrates Plotly Express plotting functions with pandas DataFrames.
- **Safe Mode**: To avoid naming conflicts, `PlotlyPlus` introduces a 'safe mode' (`plotlyplus_safe`). In this mode, each function is prefixed, ensuring namespace integrity at the cost of slightly reduced convenience.

## Installation
Install `PlotlyPlus` using pip with the following command:
```bash
pip install plotlyplus
```

## Usage

### Standard Mode
In the standard mode, import `plotlyplus` after pandas to automatically enhance DataFrames with Plotly Express functionality.


```python
import pandas as pd
import plotlyplus

df = pd.DataFrame(...)
fig = df.bar(...)  # Plotly Express function as a DataFrame method
fig.show()
```

### Safe Mode
In the safe mode, import `plotlyplus_safe` after pandas to automatically enhance DataFrames with Plotly Express functionality. This mode prefixes the Plotly Express functions to minimize namespace conflicts.

```python
import pandas as pd
import plotlyplus_safe

df = pd.DataFrame(...)
fig = df.px_bar(...)  # Plotly Express function as a DataFrame method
fig.show()
```

## Contributing

Contributions to PlotlyPlus are welcome. Please feel free to submit pull requests, report bugs, or suggest features.


## License

PlotlyPlus is made available under the MIT License.
