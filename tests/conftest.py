"""
Mock macOS-only dependencies and import csshi (which has no .py extension)
so that tests can run on any platform.
"""

import importlib.util
import pathlib
import sys
from importlib.machinery import SourceFileLoader
from unittest.mock import MagicMock

# Stub out iterm2 and all sub-modules before anything imports them
for mod in [
    "iterm2",
    "iterm2.app",
    "iterm2.broadcast",
    "iterm2.connection",
    "iterm2.profile",
    "iterm2.session",
    "iterm2.tab",
]:
    sys.modules.setdefault(mod, MagicMock())

sys.modules.setdefault("AppKit", MagicMock())

# Load csshi (no .py extension) as a regular module
_csshi_path = str(pathlib.Path(__file__).parent.parent / "csshi")
_loader = SourceFileLoader("csshi", _csshi_path)
_spec = importlib.util.spec_from_file_location("csshi", _csshi_path, loader=_loader)
assert _spec is not None
_csshi = importlib.util.module_from_spec(_spec)
_loader.exec_module(_csshi)
sys.modules["csshi"] = _csshi
