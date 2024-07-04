import importlib.metadata
import warnings

try:
    __version__ = importlib.metadata.version("official_genailib_wl")
except importlib.metadata.PackageNotFoundError as e:
    warnings.warn("Could not determine version of official_genailib_wl", stacklevel=1)
    warnings.warn(str(e), stacklevel=1)
    __version__ = "unknown"
