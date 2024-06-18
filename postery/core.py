import parampl


class Postery:
    def __init__(self,
                 size: str | tuple[float, float],
                 dpi: int = 200
                 ):

        self.figsize, self.size_name = inches_from_size(size)


        self.size = size
