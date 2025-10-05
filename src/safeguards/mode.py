import enum
import os


class Mode(str, enum.Enum):
    SIMULATION = "SIMULATION"
    LIVE = "LIVE"


def get_mode() -> Mode:
    """
    Returns the current execution mode from environment.
    Defaults to SIMULATION.
    """
    raw = os.getenv("SIMULATION_MODE", "SIMULATION").strip().upper()
    try:
        return Mode(raw)
    except Exception:
        return Mode.SIMULATION
