"""
Classes following the PICMI standard
These should be the base classes for Python implementation of the PICMI standard
"""

from .base import _ClassWithInit

class PICMI_PhaseSpace(_ClassWithInit):
    """
    Specifies the parameters for the output of Phase Space of species such as electrons.

    This plugin extracts phase-space data from the simulation, allowing
    for detailed analysis of particle distributions in position-momentum space.

    Parameters
    ----------
    species: string
        Name of the particle species to track (e.g., "electron", "proton").

    period: int
        Number of simulation steps between consecutive outputs.

    spatial_coordinate: string
        Spatial coordinate used in phase space (e.g., 'x', 'y', 'z').

    momentum: string
        Momentum coordinate used in phase space (e.g., 'px', 'py', 'pz').

    min_momentum: float
        Minimum value for the phase-space coordinate range.

    max_momentum: float
        Maximum value for the phase-space coordinate range.

    name: string, optional
        Optional name for the phase-space plugin.
    """

    def __init__(self, species, period,
                 spatial_coordinate, momentum,
                 min_momentum, max_momentum,
                name=None, **kw):
        """
        Initialize the Phase Space Plugin parameters.
        """
        self.species = species
        self.period = period
        self.spatial_coordinate = spatial_coordinate
        self.momentum = momentum
        self.min_momentum = min_momentum
        self.max_momentum = max_momentum
        self.name = name

        self.handle_init(kw)

    def handle_init(self, kwargs):
        """ Handle additional keyword arguments. """
        for key, value in kwargs.items():
            setattr(self, key, value)
