import astropy.units as u

def inches_from_size(size):

    if isinstance(size, tuple):
        width, height = size

        width_unit = height_unit = None
        if isinstance(width, u.Quantity):
            width_unit = width.unit
        if isinstance(height, u.Quantity):
            height_unit = height.unit
        if height_unit is None:
            height_unit = width_unit
        if height_unit is None:
            height_unit = u.imperial.inch
        if width_unit is None:
            width_unit = u.imperial.inch

