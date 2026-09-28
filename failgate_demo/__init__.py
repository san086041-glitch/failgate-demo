"""failgate-demo: tiny text utilities (config parsing, slugs, sequences)."""

from failgate_demo.config import get, parse
from failgate_demo.seq import chunks, unique
from failgate_demo.text import slugify

__all__ = ["chunks", "get", "parse", "slugify", "unique"]
__version__ = "0.3.0"
