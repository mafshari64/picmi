"""
Classes following the PICMI standard
These should be the base classes for Python implementation of the PICMI standard
"""

from .base import _ClassWithInit

class PICMI_MacroParticleCount(_ClassWithInit):
    """
    Specifies the parameters for counting the total number of macro particles of a given species.

    This plugin counts the number of macro particles in the simulation,
    useful for tracking particle statistics and population dynamics.

    Parameters
    ----------
    species: string
        Name of the particle species to count (e.g., "electron", "proton").

    period: int
        Number of simulation steps between consecutive counts.
        Unit: steps (simulation time steps).

    name: string, optional
        Optional name for the macro particle count plugin.
    """

    def __init__(self, species, period, name=None, **kw):
        """
        Initialize the Macro Particle Count Plugin parameters.
        """
        self.species = species
        self.period = period
        self.name = name

        self.handle_init(kw)

    def handle_init(self, kwargs):
        """ Handle additional keyword arguments. """
        for key, value in kwargs.items():
            setattr(self, key, value)

