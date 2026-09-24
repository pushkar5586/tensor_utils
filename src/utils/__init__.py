"""Top-level package imports for clean user-facing APIs."""

from .tensor_utils import add_past_windows, add_future_windows

__all__ = ["add_past_windows", "add_future_windows"]
__version__ = "0.1.0"