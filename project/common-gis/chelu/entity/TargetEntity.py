class TargetFileEntity:
    def __init__(self):
        self._node_name = None
        self._target_lon = None
        self._target_lat = None
        self._direction = {}

    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        self._node_name = node_name

    @property
    def target_lon(self):
        return self._target_lon

    @target_lon.setter
    def target_lon(self, target_lon):
        self._target_lon = target_lon

    @property
    def target_lat(self):
        return self._target_lat

    @target_lat.setter
    def target_lat(self, target_lat):
        self._target_lat = target_lat

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction
