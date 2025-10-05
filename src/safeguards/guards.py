import os
import sys
from .mode import Mode, get_mode


class LiveModeBlockedError(RuntimeError):
    pass


def assert_simulation_mode() -> None:
    mode = get_mode()
    if mode == Mode.LIVE:
        raise LiveModeBlockedError(
            "LIVE mode is forbidden. Set SIMULATION_MODE=SIMULATION."
        )


def forbid_live_orders() -> None:
    assert_simulation_mode()
    raise LiveModeBlockedError(
        "Order placement is disabled (simulation-only)."
    )
