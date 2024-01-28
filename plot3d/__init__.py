from .__logger import setup
from .td_app import TDApp
from .td_client import TDClient
from .plot import Plot

# Setup logging
setup()

__all__ = [
    'Plot',
    'TDApp',
    'TDClient'
]
