class NodeEntity:
    def __init__(self):
        self._NodeID = None
        self._x = None
        self._y = None
        self._z = None
        self._NodeType = None
        self._lng = None
        self._lat = None
        self._alt = None

    @property
    def NodeID(self):
        return self.NodeID()

    @NodeID.setter
    def NodeID(self, NodeID):
        self._NodeID = NodeID

    @property
    def x(self):
        return self.x()

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self.y()

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def z(self):
        return self.z()

    @z.setter
    def z(self, z):
        self._z = z

    @property
    def NodeType(self):
        return self.NodeType()

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType

    @property
    def lng(self):
        return self.lng()

    @lng.setter
    def lng(self, lng):
        self._lng = lng

    @property
    def lat(self):
        return self.lat()

    @lat.setter
    def lat(self, lat):
        self._lat = lat

    @property
    def alt(self):
        return self.alt()

    @alt.setter
    def alt(self, alt):
        self._alt = alt
