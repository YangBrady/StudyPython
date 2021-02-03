"""
add by liangms
date 2021-1-15
"""

from pyproj import Transformer
import math
from numpy import array


class odrCoorTransform:

    def xyz2World(self, x, y, z):
        """
        xyz转经纬度
        :param x:平面坐标x--对应于经度lng
        :param y:平面坐标y--对应于纬度lat
        :param z:平面坐标z--对应于高度alt
        :return lng lat alt
        """
        return

    def world2xyz(self, lng, lat, alt):
        """
        经纬度转xyz
        :param lng:坐标经度x
        :param lat:坐标纬度y
        :param alt:坐标海拔z
        :return x y z
        """
        return


class geoReference():
    """
    opendrive的坐标参考系统
    """

    def __init__(self, strPrj):
        self._prj = strPrj
        listPrj = str(self._prj).split("+")
        self._lat0 = 0
        self._lng0 = 0
        self._x0 = 0
        self._y0 = 0
        hasLat_0 = False
        for item in listPrj:
            if (str(item).find("lat_0") != -1):
                latArr = item.split("=")
                self._lat0 = float(latArr[1])
            if (str(item).find("lon_0") != -1):
                latArr = item.split("=")
                self._lng0 = float(latArr[1])
            if (str(item).find("x_0") != -1):
                xArr = item.split("=")
                self._x0 = float(xArr[1])
                hasLat_0 = True
            if (str(item).find("y_0") != -1):
                yArr = item.split("=")
                self._y0 = float(yArr[1])
                # if(hasLat_0):
        #     self._y0,self._x0,z= self.world2xyzReal(self.lng0,self.lat0,0)

    @property
    def Prj(self):
        """
        opendrive的坐标参考系统
        """
        return self._prj

    @property
    def x0(self):
        """
        坐标参考系统的投影原点坐标X0
        """
        return self._x0

    @property
    def y0(self):
        """
        坐标参考系统的投影原点坐标y0
        """
        return self._y0

    @property
    def lat0(self):
        """
        坐标参考系统的纬度原点坐标lat0
        """
        return self._lat0

    @property
    def lng0(self):
        """
        坐标参考系统的经度度原点坐标lat0
        """
        return self._lng0


class commonCoorTransform(odrCoorTransform):

    def __init__(self, xyzPrj, worldPrj="epsg:4326"):
        super().__init__()
        self._xyzPrj = xyzPrj
        self._worldPrj = worldPrj

        self.xyz2worldTransform = Transformer.from_crs(self._xyzPrj, self._worldPrj)
        self.world2xyzTransform = Transformer.from_crs(self._worldPrj, self._xyzPrj)
        geoRefer = geoReference(xyzPrj)
        x0, y0, z0 = self.world2xyz(geoRefer.lng0, geoRefer.lat0, 0)
        if (round(x0, 5) == round(geoRefer.x0) and round(y0, 5) == round(geoRefer.y0)):
            self._x0 = geoRefer.x0
            self._y0 = geoRefer.y0
        else:
            self._x0 = geoRefer.x0 + x0
            self._y0 = geoRefer.y0 + y0

        self._utmPrj = self.getUtmPrj(geoRefer.lng0)

    @property
    def worldPrj(self):
        return self._worldPrj

    @property
    def xyzPrj(self):
        return self._xyzPrj

    def xyz2World(self, x, y, z):
        # return self.xyz2WorldReal(self._x0+x,self._y0+y,z)
        return self.xyz2WorldReal(x, y, z)  # 暂时使用这个，匹配三龙湾的坐标
        # return self.xyz2WorldReal(self._x0+y,self._y0+x,z)#opendrive 

    def world2xyz(self, lng, lat, alt):
        """
        经纬度转投影参考的xyz
        :param lng:坐标经度
        :param lat:坐标纬度
        :param alt:坐标海拔
        :return x y z
        """
        return self.world2xyzReal(lng, lat, alt)

    def xyz2WorldReal(self, x, y, z):
        transprojr = self.xyz2worldTransform
        lat, lng, alt = transprojr.transform(x, y, z)
        return lng, lat, alt

    def world2xyzReal(self, lng, lat, alt):
        """
        经纬度转投影参考的xyz
        :param lng:坐标经度
        :param lat:坐标纬度
        :param alt:坐标海拔
        :return x y z
        """
        transprojr = self.world2xyzTransform
        return transprojr.transform(lat, lng, alt)

    def world2OdrXyz(self, lng, lat, alt):
        """
        经纬度转opendrive的xyz
        :param lng:坐标经度
        :param lat:坐标纬度
        :param alt:坐标海拔
        :return x,y,z
        """
        x, y, z = self.world2xyz(lng, lat, alt)
        return x - self._x0, y - self._y0, z

    def getUtmPrj(self, lng):
        zone = math.ceil(lng / 6) + 30
        prjStr = "+proj=utm +zone=" + str(zone) + " +ellps=WGS84 +datum=WGS84 +units=m +no_defs"
        return prjStr

    def wgs2utm(self, lng, lat, alt):
        """
        wgs84转utm
        :param lng:坐标经度
        :param lat:坐标纬度
        :param alt:坐标海拔
        :return x y z
        """
        transprojr = Transformer.from_crs("epsg:4326", self._utmPrj)
        return transprojr.transform(lat, lng, alt)

    def utm2wgs(self, y, x, z):
        """
        wgs84转utm
        :param x:投影坐标x--对应于经度lng
        :param y:投影坐标y--对应于纬度lat
        :param z:投影坐标z--对应于高度alt
        :return lng lat alt
        """
        transprojr = Transformer.from_crs(self._utmPrj, "epsg:4326")
        lat, lng, alt = transprojr.transform(y, x, z)
        return lng, lat, alt


class enuCoorTransform(odrCoorTransform):

    # def __init__(self,originLng,originLat,originAlt):
    def __init__(self):
        # 应用于局部坐标系ENU的坐标转换，<header>中存在值为localEnuExt的userdata时生效
        ori_str = "-2401961.17873523,5382411.39108763,2429216.19390428;-0.913194779774907,-0.407523366436648,0;0.155287762246027,-0.347975074621994,0.924553437254137;-0.37677712920038,0.844297372523425,0.381052413273504"
        v1, v2, v3, v4 = ori_str.split(';')
        self._v1 = [float(i) for i in list(v1.split(','))]
        self._v2 = [float(i) for i in list(v2.split(','))]
        self._v3 = [float(i) for i in list(v3.split(','))]
        self._v4 = [float(i) for i in list(v4.split(','))]
        super().__init__()

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def v3(self):
        return self._v3

    @property
    def v4(self):
        return self._v4

    def xyz2World(self, x, y, z):
        world = array(self._v1) + array(self._v2) * x + array(self._v3) * y + array(self._v4) * z
        return self.xyz2llh(world)

    # 从x,y,z格式的坐标转换为弧度制（Longitude,Latitude,Height）的函数
    def xyz2llh(self, xyz):
        pi = math.pi
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        x2 = x ** 2
        y2 = y ** 2
        z2 = z ** 2

        a = 6378137.0000  # earth radius in meters
        b = 6356752.3142  # earth semiminor in meters
        e = math.sqrt(1 - (b / a) ** 2)
        b2 = b * b
        e2 = e ** 2
        ep = e * (a / b)
        r = math.sqrt(x2 + y2)
        r2 = r * r
        E2 = a ** 2 - b ** 2
        F = 54 * b2 * z2
        G = r2 + (1 - e2) * z2 - e2 * E2
        c = (e2 * e2 * F * r2) / (G * G * G)
        s = (1 + c + math.sqrt(c * c + 2 * c)) ** (1 / 3);
        P = F / (3 * (s + 1 / s + 1) ** 2 * G * G);
        Q = math.sqrt(1 + 2 * e2 * e2 * P)
        ro = -(P * e2 * r) / (1 + Q) + math.sqrt(
            (a * a / 2) * (1 + 1 / Q) - (P * (1 - e2) * z2) / (Q * (1 + Q)) - P * r2 / 2)
        tmp = (r - e2 * ro) ** 2
        U = math.sqrt(tmp + z2)
        V = math.sqrt(tmp + (1 - e2) * z2);
        zo = (b2 * z) / (a * V);

        height = U * (1 - b2 / (a * V))

        lat = math.atan((z + ep * ep * zo) / r)

        temp = math.atan(y / x);
        if x >= 0:
            long = temp
        elif (x < 0) and (y >= 0):
            long = pi + temp
        else:
            long = temp - pi

        # llh = [lat*180/pi,long*180/pi,height]
        llh = [long * 180 / pi, lat * 180 / pi, height]
        return llh

    def enu2lla(self, X, Y, Z):
        xyz = array(self._v1) + array(self._v2) * X + array(self._v3) * Y + array(self._v4) * Z
        pi = math.pi
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        x2 = x ** 2
        y2 = y ** 2
        z2 = z ** 2

        a = 6378137.0000  # earth radius in meters
        b = 6356752.3142  # earth semiminor in meters
        e = math.sqrt(1 - (b / a) ** 2)
        b2 = b * b
        e2 = e ** 2
        ep = e * (a / b)
        r = math.sqrt(x2 + y2)
        r2 = r * r
        E2 = a ** 2 - b ** 2
        F = 54 * b2 * z2
        G = r2 + (1 - e2) * z2 - e2 * E2
        c = (e2 * e2 * F * r2) / (G * G * G)
        s = (1 + c + math.sqrt(c * c + 2 * c)) ** (1 / 3)
        P = F / (3 * (s + 1 / s + 1) ** 2 * G * G)
        Q = math.sqrt(1 + 2 * e2 * e2 * P)
        ro = -(P * e2 * r) / (1 + Q) + math.sqrt(
            (a * a / 2) * (1 + 1 / Q) - (P * (1 - e2) * z2) / (Q * (1 + Q)) - P * r2 / 2)
        tmp = (r - e2 * ro) ** 2
        U = math.sqrt(tmp + z2)
        V = math.sqrt(tmp + (1 - e2) * z2)
        zo = (b2 * z) / (a * V)

        height = U * (1 - b2 / (a * V))

        lat = math.atan((z + ep * ep * zo) / r)

        temp = math.atan(y / x)
        if x >= 0:
            long = temp
        elif (x < 0) and (y >= 0):
            long = pi + temp
        else:
            long = temp - pi

        llh = [lat * 180 / pi, long * 180 / pi, height]

        return llh


class carlarTransform():

    def __init__(self, strPrj):
        geoRefer = geoReference(strPrj)
        self._x0 = geoRefer.x0
        self._y0 = geoRefer.y0
        self.latOrigin = geoRefer.lat0
        self.lonOrigin = geoRefer.lng0
        self.altitudeOrigin = 0
        self.EARTH_RADIUS_EQUA = 6378137.0

    def LatToScale(self, lat):
        return math.cos(math.radians(lat))

    def LatLonToMercator(self, lat, lon, scale):
        mx = scale * math.radians(lon) * self.EARTH_RADIUS_EQUA
        my = scale * self.EARTH_RADIUS_EQUA * math.log(math.tan((90.0 + lat) * math.pi / 360.0))
        return mx, my

    def MercatorToLatLon(self, mx, my, scale):
        lon = mx * 180.0 / (math.pi * self.EARTH_RADIUS_EQUA * scale)
        lat = 360.0 * math.atan(math.exp(my / (self.EARTH_RADIUS_EQUA * scale))) / math.pi - 90.0
        return lat, lon

    def LatLonAddMeters(self, lat_start, lon_start, dx, dy):
        scale = self.LatToScale(lat_start)
        mx, my = self.LatLonToMercator(lat_start, lon_start, scale)
        mx += dx
        my += dy
        lat_end, lon_end = self.MercatorToLatLon(mx, my, scale)
        return lat_end, lon_end

    def carla2World(self, x, y, z):
        lat, lng = self.LatLonAddMeters(self.latOrigin, self.lonOrigin, x, -y)
        alt = self.altitudeOrigin + z
        return lng, lat, alt

    def world2Carla(self, lng, lat, alt):
        scale = self.LatToScale(self.latOrigin)
        sx, sy = self.LatLonToMercator(self.latOrigin, self.lonOrigin, scale)
        scale1 = self.LatToScale(lat)
        ex, ey = self.LatLonToMercator(lat, lng, scale)
        dx = ex - sx
        dy = ey - sy
        z = alt - self.altitudeOrigin
        return dx, -dy, z
