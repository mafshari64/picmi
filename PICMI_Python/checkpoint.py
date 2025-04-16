"""
Classes following the PICMI standard
These should be the base classes for Python implementation of the PICMI standard
"""

from .base import _ClassWithInit
from typing import Optional, Dict

class PICMI_Checkpoint(_ClassWithInit):
    """
    Specifies the parameters for creating checkpoints in PIC simulations.

    This plugin saves simulation state snapshots at specified intervals,
    allowing for simulation restarts or analysis. At least one of period or
    timePeriod must be provided.

    Parameters
    ----------
    period: int, optional
        Specify on which time steps to create checkpoints.
        Unit: steps (simulation time steps). Required if timePeriod is not provided.

    timePeriod: float, optional
        Specify the interval in minutes for creating checkpoints.
        Unit: minutes. Required if period is not provided.

    directory: str, optional
        Directory inside simOutput for writing checkpoints (default: "checkpoints").

    file: str, optional
        Relative or absolute fileset prefix for checkpoint files.

    restart: bool, optional
        If True, restart simulation from the latest checkpoint.

    tryRestart: bool, optional
        If True, restart from the latest checkpoint if available, else start from scratch.

    restartStep: int, optional
        Specific checkpoint step to restart from.

    restartDirectory: str, optional
        Directory inside simOutput containing checkpoints for restart (default: "checkpoints").

    restartFile: str, optional
        Relative or absolute fileset prefix for reading checkpoints.

    restartChunkSize: int, optional
        Number of particles processed in one kernel call during restart.

    restartLoop: int, optional
        Number of times to restart the simulation after it finishes.

    openPMD: dict, optional
        Dictionary of openPMD-specific settings (e.g., {"ext": "h5", "json": "{}"}).

    name: str, optional
        Optional name for the checkpoint plugin.
    """

    def __init__(
        self,
        period: Optional[int] = None,
        timePeriod: Optional[float] = None,
        directory: Optional[str] = None,
        file: Optional[str] = None,
        restart: Optional[bool] = None,
        tryRestart: Optional[bool] = None,
        restartStep: Optional[int] = None,
        restartDirectory: Optional[str] = None,
        restartFile: Optional[str] = None,
        restartChunkSize: Optional[int] = None,
        restartLoop: Optional[int] = None,
        openPMD: Optional[Dict] = None,
        name: Optional[str] = None,
        **kw
    ):
        """
        Initialize the Checkpoint Plugin parameters.
        """
        self.period = period
        self.timePeriod = timePeriod
        self.directory = directory
        self.file = file
        self.restart = restart
        self.tryRestart = tryRestart
        self.restartStep = restartStep
        self.restartDirectory = restartDirectory
        self.restartFile = restartFile
        self.restartChunkSize = restartChunkSize
        self.restartLoop = restartLoop
        self.openPMD = openPMD
        self.name = name

        self.handle_init(kw)

    def handle_init(self, kwargs):
        """ Handle additional keyword arguments. """
        for key, value in kwargs.items():
            setattr(self, key, value)