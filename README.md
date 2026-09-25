# tensor_utils

Personal Python utility functions for manipulating data tensors.

## Installation

```bash
pip install git+https://github.com/pushkar5586/tensor_utils.git
```

## Documentation

https://pushkar5586.github.io/tensor_utils/

## Quick example

```python
import numpy as np
from tensor_utils import add_past_windows

A = np.arange(10)
windows = add_past_windows(A, lb=3, strict_lookback=True)
```

See the [API Reference](api.md) for the full function reference.
