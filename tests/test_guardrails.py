import os
import importlib
import sys
from pathlib import Path
import pytest

# Ensure import from src/
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from safeguards.mode import get_mode, Mode  # noqa: E402
from safeguards.guards import (  # noqa: E402
    assert_simulation_mode,
    forbid_live_orders,
    LiveModeBlockedError,
)


def test_default_mode_is_simulation(monkeypatch):
    monkeypatch.delenv("SIMULATION_MODE", raising=False)
    assert get_mode() == Mode.SIMULATION


def test_live_mode_is_blocked(monkeypatch):
    monkeypatch.setenv("SIMULATION_MODE", "LIVE")
    # Even reading env should not allow LIVE usage
    with pytest.raises(LiveModeBlockedError):
        assert_simulation_mode()


def test_forbid_live_orders_always_raises(monkeypatch):
    # Regardless of env, placing orders is disabled
    monkeypatch.delenv("SIMULATION_MODE", raising=False)
    with pytest.raises(LiveModeBlockedError):
        forbid_live_orders()
