class TargetFileDirection:
    def __init__(self):
        self._link_east = []
        self._link_south = []
        self._link_west = []
        self._link_north = []

    @property
    def link_east(self):
        return self._link_east

    @link_east.setter
    def link_east(self, link_east):
        self._link_east = link_east

    @property
    def link_south(self):
        return self._link_south

    @link_south.setter
    def link_south(self, link_south):
        self._link_south = link_south

    @property
    def link_west(self):
        return self._link_west

    @link_west.setter
    def link_west(self, link_west):
        self._link_west = link_west

    @property
    def link_north(self):
        return self._link_north

    @link_north.setter
    def link_north(self, link_north):
        self._link_north = link_north
