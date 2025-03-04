"""
Classes following the PICMI standard
These should be the base classes for Python implementation of the PICMI standard
"""

from .base import _ClassWithInit

class PICMI_EnergyHistogram(_ClassWithInit):
    """
    Specifies the parameters for the output of Energy Histogram of species such as electrons.

    This plugin records the energy distribution of particles within specified bins,
    useful for analyzing energy spectra.

    Parameters
    ----------
    species: string
        Name of the particle species to track (e.g., "electron", "proton").

    period: int
        Number of simulation steps between consecutive histogram outputs.

    bin_count: int
        Number of bins for the energy histogram.

    min_energy: float
        Minimum energy value for the histogram range (in eV or MeV, depending on the simulation).

    max_energy: float
        Maximum energy value for the histogram range.

    name: string, optional
        Optional name for the energy histogram plugin.
    """

    def __init__(self, species, period, bin_count,
                 min_energy, max_energy, name=None, **kw):
        """
        Initialize the Energy Histogram Plugin parameters.
        """
        self.species = species
        self.period = period
        self.bin_count = bin_count
        self.min_energy = min_energy
        self.max_energy = max_energy
        self.name = name

        self.handle_init(kw)

    def handle_init(self, kwargs):
        """ Handle additional keyword arguments. """
        for key, value in kwargs.items():
            setattr(self, key, value)

