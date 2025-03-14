"""
Classes following the PICMI standard
These should be the base classes for Python implementation of the PICMI standard
"""

from .base import _ClassWithInit

class PICMI_PNG(_ClassWithInit):
    """
    Specifies the parameters for PNG output in PIConGPU.

    This plugin generates 2D PNG images of field and particle data.

    Parameters
    ----------
    data_list: list of strings
        List of field or current quantities to output (e.g., ['Ex', 'Ey', 'Ez', 'Bx', 'By', 'Bz', 'Jx', 'Jy', 'Jz']).

    period: int
        Number of simulation steps between consecutive image outputs.

    axis: string
        Axis combination for the 2D slice (e.g., "yx").

    slice_point: float
        Ratio for the slice position in the dimension not used in axis (e.g., "z") (0.0 to 1.0).

    species: string
        Name of the particle species to count (e.g., "electron", "proton").

    folder_name: string
        Folder name where the PNGs will be stored.
        
    scale_image: float
        Scaling factor applied to the image before writing to file (default: 1.0).

    scale_to_cellsize: bool
        Whether to scale the image to account for non-quadratic cell sizes.

    white_box_per_gpu: bool
        If true, draws white lines indicating GPU boundaries.

    em_field_scale_channel1: int
        Scaling mode for EM fields in channel 1:
        -1: Auto (adaptive scaling for each output)
         3: Plasma Wave (scaling from plasma frequency)
         6: Custom (use custom normalization factors)
         7: Incident (scaling from incident field amplitude)

    em_field_scale_channel2: int
        Same as em_field_scale_channel1, but for channel 2.

    em_field_scale_channel3: int
        Same as em_field_scale_channel1, but for channel 3.

    custom_normalization_si: list of 3 floats
        Custom normalization factors for B, E, and current (when using scale mode 6).

    pre_particle_density_opacity: float
        Opacity of the particle density overlay (0.0 to 1.0).

    pre_channel1_opacity: float
        Opacity for channel 1 data (0.0 to 1.0).

    pre_channel2_opacity: float
        Opacity for channel 2 data (0.0 to 1.0).

    pre_channel3_opacity: float
        Opacity for channel 3 data (0.0 to 1.0).

    pre_particle_density_color_scales: string
        Color scale for particle density (e.g., "red", "green", "blue", "gray", "grayInv", "none").

    pre_channel1_color_scales: string
        Color scale for channel 1 (same options as above).

    pre_channel2_color_scales: string
        Color scale for channel 2 (same options as above).

    pre_channel3_color_scales: string
        Color scale for channel 3 (same options as above).

    pre_channel1: string
        Custom expression for channel 1 (e.g., "field_E.x() * field_E.x();").

    pre_channel2: string
        Custom expression for channel 2 (e.g., "field_E.y()").

    pre_channel3: string
        Custom expression for channel 3 (e.g., "-1.0_X * field_E.y()").

    """

    def __init__(self, data_list, period, axis, slice_point, folder_name, species, scale_image,
                 scale_to_cellsize, white_box_per_gpu,
                 em_field_scale_channel1, em_field_scale_channel2, em_field_scale_channel3,
                 custom_normalization_si,
                 pre_particle_density_opacity,
                 pre_channel1_opacity, pre_channel2_opacity, pre_channel3_opacity,
                 pre_particle_density_color_scales,
                 pre_channel1_color_scales, pre_channel2_color_scales, pre_channel3_color_scales,
                 pre_channel1, pre_channel2, pre_channel3,
                 **kw):

        self.data_list = data_list
        self.period = period
        self.axis = axis
        self.slice_point = slice_point
        self.folder_name = folder_name
        self.species = species
        self.scale_image = scale_image
        self.scale_to_cellsize = scale_to_cellsize
        self.white_box_per_gpu = white_box_per_gpu
        self.em_field_scale_channel1 = em_field_scale_channel1
        self.em_field_scale_channel2 = em_field_scale_channel2
        self.em_field_scale_channel3 = em_field_scale_channel3
        self.custom_normalization_si = custom_normalization_si or [0.0, 0.0, 0.0]
        self.pre_particle_density_opacity = pre_particle_density_opacity
        self.pre_channel1_opacity = pre_channel1_opacity
        self.pre_channel2_opacity = pre_channel2_opacity
        self.pre_channel3_opacity = pre_channel3_opacity
        self.pre_particle_density_color_scales = pre_particle_density_color_scales
        self.pre_channel1_color_scales = pre_channel1_color_scales
        self.pre_channel2_color_scales = pre_channel2_color_scales
        self.pre_channel3_color_scales = pre_channel3_color_scales
        self.pre_channel1 = pre_channel1
        self.pre_channel2 = pre_channel2
        self.pre_channel3 = pre_channel3


        self.handle_init(kw)

    def handle_init(self, kwargs):
        """ Handle additional keyword arguments. """
        for key, value in kwargs.items():
            setattr(self, key, value)

