class PICMI_PhaseSpacePlugin:
    """
    Specifies the parameters for the Phase Space plugin in PIConGPU.

    This plugin extracts phase-space data from the simulation, allowing
    for detailed analysis of particle distributions in position-momentum space.

    Parameters
    ----------
    phase_space_species_name: string
        Name of the particle species to track (e.g., "electron", "proton").

    phase_space_period: int
        Number of simulation steps between consecutive outputs.

    phase_space_space: string
        Spatial coordinate used in phase space (e.g., 'x', 'y', 'z').

    phase_space_momentum: string
        Momentum coordinate used in phase space (e.g., 'px', 'py', 'pz').

    phase_space_min: float
        Minimum value for the phase-space coordinate range.

    phase_space_max: float
        Maximum value for the phase-space coordinate range.

    phase_space_filter: string
        Filtering method applied to particles (e.g., "all", "energy_filter").

    name: string, optional
        Optional name for the phase-space plugin.
    """

    def __init__(self, phase_space_species_name, phase_space_period,
                 phase_space_space, phase_space_momentum,
                 phase_space_min, phase_space_max,
                 phase_space_filter, name=None, **kw):
        """
        Initialize the Phase Space Plugin parameters.
        """
        self.phase_space_species_name = phase_space_species_name
        self.phase_space_period = phase_space_period
        self.phase_space_space = phase_space_space
        self.phase_space_momentum = phase_space_momentum
        self.phase_space_min = phase_space_min
        self.phase_space_max = phase_space_max
        self.phase_space_filter = phase_space_filter
        self.name = name

        self.handle_init(kw)

    def handle_init(self, kwargs):
        """ Handle additional keyword arguments. """
        for key, value in kwargs.items():
            setattr(self, key, value)
