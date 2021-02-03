import logging
import pandas as pd
from lxml import etree
from opendrive2lanelet.opendriveparser.parser import parse_opendrive
import sys

sys.path.append("..")
import common.utils as utils
from entity.TargetEntity import TargetNode
from entity.NodeEntity import NodeEntity
from odrCoorTransform import (
    enuCoorTransform, commonCoorTransform)


def parse_junction(inputFile, outputDir, Node_ID, nodeCsvFile, targetCsvFile):
    # 读取roadList
    with open(targetCsvFile, 'r', encoding='utf-8') as f:
        nodes = pd.read_csv(f, dtype={'link_North': str, 'link_East': str, 'link_South': str, 'link_West': str})
    nodes = nodes.where(nodes.notnull(), None)  # 将NaN转换成None
    target_node_map, road_list = get_target_node_map(nodes)

    o_step_length = 5
    with open(inputFile, 'r', encoding='utf-8') as fh:
        open_drive = parse_opendrive(etree.parse(fh).getroot())

    ivics_road = list()
    open_drive_road_ids = {road.id: road for road in open_drive.roads}
    for r in road_list:
        if open_drive_road_ids.get(r) is not None:
            ivics_road.append(r)
    #
    # junctions = open_drive.junctions
    #
    # sidewalk = pd.DataFrame(columns=['dir', 'junction', 'lon', 'lat', 'x', 'y', 'z'])
    # walk = pd.DataFrame(columns=['dir', 'junction', 'lon', 'lat', 'x', 'y', 'z'])
    # cpoints = pd.DataFrame(columns=['code', 'road', 'laneSectionIndex', 'lane', 'x',
    #                                 'y', 'z', 'tangent', 'Node', 'Length', 'Lane Type', 'laneChange', 'laneSpeed'])
    # linkage_dict = {}
    #
    # header = open_drive.header
    # # 添加原点初始属性
    # if (hasattr(header, 'mapId')):
    #     mapId = header.mapId
    # else:
    #     mapId = 1100
    #
    # # 从地图头文件中读取原点初始属性
    # try:
    #     prjCrs = header.geo_reference
    #     if prjCrs is None:
    #         odrCoorTran = enuCoorTransform()
    #     else:
    #         odrCoorTran = commonCoorTransform(prjCrs)
    # except Exception as e:
    #     logging.exception(e)
    #     pass

    node_xyz_map = get_node_xyz_map(nodeCsvFile)
    #
    # for road in ivics_road:
    #     step_length = o_step_length  # 步长先默认为5米 mod by liangms  2021-1-27
    #     # if road.length < o_step_length:
    #     #     step_length = road.length/2
    #     # else:
    #     #     step_length = o_step_length
    #     for directions, dic in ivics_link_dict.items():
    #         if road.id in dic['roadlist']:
    #             upStreamNode = dic['upstreamNode']
    #             s_dir = dic['s_direction']
    #             break
    #     # logging.info(s_dir)
    #     s = 0
    #
    #     # 添加Node信息
    #     if road.junction is None:
    #         Node = -1
    #     else:
    #         Node = road.junction.id
    #
    #     # 进行控制点生成
    #     while s <= road.length:
    #
    #         # 判断所处的geometry
    #         geom_index = 0
    #         geom = None
    #         planView = road._planView
    #         geo_len = len(planView._geo_lengths)
    #         for l in range(geo_len):
    #             if round(s, 5) <= round(planView._geo_lengths[l + 1], 5):
    #                 geom = planView._geometries[l]
    #                 geom_offset = planView._geo_lengths[l + 1]
    #
    #                 # mod by liangms 去掉直线判断
    #                 # # 直线车道判断
    #                 # if geom.__class__.__name__ == "Line" and s > step_length:
    #                 #     s = geom_offset
    #
    #                 delta_s = s - planView._geo_lengths[l]
    #                 # 计算出对应车道参考线坐标
    #                 hdg = geom.calc_position(delta_s)[1]
    #                 posx = geom.calc_position(delta_s)[0][0]
    #                 posy = geom.calc_position(delta_s)[0][1]
    #                 # logging.info(road.id, s)  # ,s,posx,posy,hdg
    #                 break
    #             else:
    #                 continue
    #
    #         # 判断所处的elevations
    #         elev = road.elevationProfile.elevations
    #         lth = len(elev)
    #         for l in range(lth):
    #             if elev[-l][0].start_pos <= s:
    #                 [a, b, c, d] = elev[-l][0].polynomial_coefficients
    #                 elev_s = s - elev[-l][0].start_pos
    #                 elev_record = float(
    #                     a + b * elev_s + c * elev_s ** 2 + d * elev_s ** 3)
    #             else:
    #                 elev_record = 0
    #
    #         # 判断所处的LaneOffSet
    #         l_offsets = road.lanes.laneOffsets
    #         if len(l_offsets) > 0:
    #             for l in range(len(l_offsets)):
    #                 if l_offsets[-l - 1].start_pos <= s:
    #                     [a, b, c, d] = l_offsets[-l - 1].polynomial_coefficients
    #                     loff_s = s - l_offsets[-l - 1].start_pos
    #                     lane_offset_record = float(
    #                         a + b * loff_s + c * loff_s ** 2 + d * loff_s ** 3)
    #                     break
    #                 else:
    #                     continue
    #         else:
    #             lane_offset_record = 0
    #         # 判断所处的LaneSection
    #         lane_sct = road.lanes.lane_sections
    #         lane_section = None
    #         for sct in lane_sct:
    #             if round(s, 5) <= round(sct.sPos + sct.length, 5):
    #                 lane_section = sct
    #                 break
    #             else:
    #                 continue
    #         # logging.info('Lane Section id is %d ' % lane_section.idx)
    #
    #         # 判断所处的laneOffset
    #
    #         s_lane = s - lane_section.sPos
    #
    #         # 处理右车道 平移距离为负
    #         if s_dir == 'right':
    #             r_lane_id = 1
    #             if len(lane_section.rightLanes) > 0:
    #                 for r_lane in lane_section.rightLanes:
    #                     if r_lane.type != 'driving':
    #                         continue
    #                     code = str(mapId) + '_' + str(road.id) + '_' + \
    #                            str(lane_section.idx) + '_' + str(r_lane.id)
    #
    #                     if r_lane._roadMarks is not None and len(r_lane._roadMarks) > 0:
    #                         if r_lane._roadMarks[0].laneChange is not None:
    #                             laneChange = r_lane._roadMarks[0].laneChange
    #                         else:
    #                             laneChange = 'Not Defined'
    #
    #                     LaneType = r_lane.type
    #                     # 记录车道限速
    #                     laneSpeed = r_lane.speed.max
    #                     if laneSpeed is None:
    #                         laneSpeed = 'Not Defined'
    #
    #                     dist = - \
    #                                mathUtils.calc_total_width(r_lane, s_lane, road.length) + \
    #                            mathUtils.calc_cur_width(
    #                                r_lane, s_lane, road.length) / 2
    #                     side = mathUtils.calc_translation(
    #                         dist + lane_offset_record, hdg)
    #                     x_record = posx + side[0]
    #                     y_record = posy + side[1]
    #                     lng, lat, alt = odrCoorTran.xyz2World(
    #                         x_record, y_record, elev_record)
    #                     nodeDistance = mathUtils.calcDistance(x_record, y_record, nodex, nodey)
    #                     cpoints = cpoints.append(
    #                         [{'code': str(code), 'road': int(road.id), 'laneSectionIndex': int(lane_section.idx),
    #                           'lane': int(r_lane_id), 'x': float(x_record), 'y': float(y_record),
    #                           'z': float(elev_record), 'lng': lng, 'lat': lat, 'alt': alt, 'nodeDistance': nodeDistance,
    #                           'tangent': float(hdg), 'Node': int(Node), 'Length': float(road.length),
    #                           'Lane Type': LaneType, 'laneChange': laneChange, 'laneSpeed': laneSpeed,
    #                           'step': step_length}], ignore_index=True)
    #                     # logging.info('Added 1 Point %d %d %f %s' %
    #                     #       (road.id, r_lane.id, s, geom.__class__.__name__))
    #                     walk, sidewalk = parseSideWalk(s_dir,
    #                                                    s, road, dir_dict, walk, Node_ID, x_record, y_record,
    #                                                    elev_record, lat, lng, sidewalk)
    #                     r_lane_id += 1
    #         else:
    #             # 处理左车道 平移距离为正
    #             l_lane_id = 1
    #             if len(lane_section.leftLanes) > 0:
    #                 for l_lane in lane_section.leftLanes:
    #                     if l_lane.type != 'driving':
    #                         continue
    #                     code = str(mapId) + '_' + str(road.id) + '_' + \
    #                            str(lane_section.idx) + '_' + str(l_lane.id)
    #
    #                     if l_lane._roadMarks is not None and len(l_lane._roadMarks) > 0:
    #                         if l_lane._roadMarks[0].laneChange is not None:
    #                             laneChange = l_lane._roadMarks[0].laneChange
    #                         else:
    #                             laneChange = 'Not Defined'
    #
    #                     LaneType = l_lane.type
    #                     # 记录车道限速
    #                     laneSpeed = l_lane.speed.max
    #                     if laneSpeed is None:
    #                         laneSpeed = 'Not Defined'
    #
    #                     dist = mathUtils.calc_total_width(
    #                         l_lane, s_lane, road.length) - mathUtils.calc_cur_width(l_lane, s_lane, road.length) / 2
    #                     side = mathUtils.calc_translation(
    #                         dist + lane_offset_record, hdg)
    #                     x_record = posx + side[0]
    #                     y_record = posy + side[1]
    #                     lng, lat, alt = odrCoorTran.xyz2World(
    #                         x_record, y_record, elev_record)
    #                     nodeDistance = mathUtils.calcDistance(x_record, y_record, nodex, nodey)
    #                     cpoints = cpoints.append(
    #                         [{'code': str(code), 'road': int(road.id), 'laneSectionIndex': int(lane_section.idx),
    #                           'lane': int(l_lane_id), 'x': float(x_record), 'y': float(y_record),
    #                           'z': float(elev_record), 'lng': lng, 'lat': lat, 'alt': alt, 'nodeDistance': nodeDistance,
    #                           'tangent': float(hdg), 'Node': int(Node), 'Length': float(road.length),
    #                           'Lane Type': LaneType, 'laneChange': laneChange, 'laneSpeed': laneSpeed,
    #                           'step': step_length}], ignore_index=True)
    #                     # logging.info('Added 1 Point %d %d %f %s' %
    #                     #       (road.id, l_lane.id, s, geom.__class__.__name__))
    #
    #                     walk, sidewalk = parseSideWalk(s_dir,
    #                                                    s, road, dir_dict, walk, Node_ID, x_record, y_record,
    #                                                    elev_record, lat, lng, sidewalk)
    #                     l_lane_id += 1
    #
    #         if step_length > road.length and s == 0:
    #             s = road.length - step_length
    #         if (s < road.length and road.length - s <= step_length and road.length >= step_length):
    #             s = road.length
    #             continue
    #         s += step_length
    #
    # # 创建目标Node字典
    # Road_group = cpoints.groupby(['road'])
    # LaneDict = {}
    # LinkList = []
    #
    # ivics_Lane_Dict = {}
    #
    # if (link_North is None):
    #     Target_Road = [link_East, link_South, link_West]
    #     Target_Road_name = ['link_East', 'link_South', 'link_West']
    # else:
    #     Target_Road = [link_North, link_East, link_South, link_West]
    #     Target_Road_name = ['link_North',
    #                         'link_East', 'link_South', 'link_West']
    #
    # '''
    # 创建Linklist的时候对子road进行分组
    # '''
    #
    # for d in range(len(Target_Road)):
    #
    #     Link_name = Target_Road_name[d]
    #     # mod by liangms 缺少进口道的方向不计算
    #     if (not ivics_link_dict.__contains__(Link_name)):
    #         continue
    #     # ivics_link_dict[Link_name] = {}
    #     ivics_link_dict[Link_name]['Lanes'] = ivics_Lane_Dict
    #     for sublink in Target_Road[d]:
    #         for roadid, laneset in Road_group:
    #             if roadid != int(sublink):
    #                 continue
    #             # logging.info('\nCurrent road id is %d ' % roadid)
    #             # logging.info(laneset)
    #             lane = laneset.groupby('lane')
    #
    #             for laneid, c_points in lane:
    #
    #                 # logging.info('\nCurrent lane id is %d,%d ' % (roadid, laneid))
    #                 # logging.info(len(c_points))
    #
    #                 # LaneDict[str(laneid)] = c_points
    #                 #
    #                 if str(laneid) not in list(ivics_Lane_Dict.keys()):
    #                     ivics_Lane_Dict[str(laneid)] = c_points
    #                     # logging.info('New')
    #                 else:
    #                     ivics_Lane_Dict[str(laneid)] = ivics_Lane_Dict[str(
    #                         laneid)].append(c_points)
    #                     # ivics_link_dict[Link_name][str(laneid)] = pd.merge(ivics_Lane_Dict[str(laneid)],(c_points))
    #                     # logging.info('Merge')
    #             # ivics_link_dict[Link_name] = ivics_Lane_Dict
    #     ivics_Lane_Dict = {}
    #     '''
    #             LinkList.append(LaneDict)
    #             LaneDict = {}
    #     '''
    #
    # Road_group = cpoints.groupby(['road'])
    # LaneDict = {}
    # LinkDict = {}
    # Pre_calc = {}
    #
    # for roadid, laneset in Road_group:
    #     lane_groupby = laneset.groupby('lane')
    #     for laneid, c_points in lane_groupby:
    #         Pre_calc[str(laneid)] = c_points
    #         # 此处创建添加车道属性所用的字典
    #         LaneDict['code'] = c_points.iloc[0]['code']
    #         LaneDict['Road'] = roadid
    #         LaneDict['Lane'] = laneid
    #         LaneDict['Node'] = c_points.iloc[0]['Node']
    #         LaneDict['road_length'] = c_points.iloc[0]['Length']
    #         LaneDict['Ctrl_points'] = Pre_calc
    #         LaneDict['Lane Type'] = c_points.iloc[0]['Lane Type']
    #         LaneDict['laneChange'] = c_points.iloc[0]['laneChange']
    #         LaneDict['laneSpeed'] = c_points.iloc[0]['laneSpeed']
    #         LaneDict['step'] = c_points.iloc[0]['step']
    #         LinkDict[str(roadid) + r'_' + str(laneid)] = LaneDict
    #         Pre_calc = {}
    #         LaneDict = {}
    #
    # # 进行结果的写入
    # # pd.DataFrame(ivics_link_dict).to_csv('test.csv')
    # # logging.info(roadlist)
    # cpoints.to_csv(outputDir + '/opendrive' + str(Node_ID) + '.csv')
    # walk.to_csv(outputDir + '/walk' + str(Node_ID) + '.csv')
    # sidewalk.to_csv(outputDir + '/sidewalk' + str(Node_ID) + '.csv', index=False)
    # write_jsonfile(Node_ID, Node_Name, target_lon, target_lat,
    #                ivics_link_dict, outputDir, Target_Road_name, roadlist, nodeCsvFile)


# TODO 创建文件夹，这一步可以后面具体写文件再做
def mkdir(inputFile, outputDir, Node_ID):
    utils.mkdir(outputDir + "/" + utils.getFileName(inputFile) + "_" + str(Node_ID))


def get_target_node_map(nodes):
    target_node_map = {}
    road_list = []

    # 将各个方向的Link集合装到一个map
    for row in nodes.iterrows():
        target_node = TargetNode()
        target_node.node_name = row[1]['Node_Name']
        target_node.target_lon = row[1]['target_lon']
        target_node.target_lat = row[1]['target_lat']
        for direction in ["link_East", "link_South", "link_West", "link_North"]:
            direction_links = row[1][direction]
            if direction_links is not None:
                target_node.direction = direction_links.split(',')
                logging.info("target_node.direction=" + target_node.direction)
                # road_list += target_node.direction

        curr_node_id = row[1]['NodeID']
        target_node_map[curr_node_id] = target_node

        road_list = [int(i) for i in road_list]
    return target_node_map, road_list


def get_node_xyz(Node_ID, nodeCsvFile):
    # 获取交叉口中心点的xyz值
    with open(nodeCsvFile, 'r', encoding='utf-8') as u:
        nodecv = pd.read_csv(u)
        nodecv = nodecv.where(nodecv.notnull(), None)
        for row in nodecv.iterrows():
            if row[1]['NodeID'] == Node_ID:
                nodex = row[1]['x']
                nodey = row[1]['y']
                break
    return nodex, nodey


# 获取交叉口中心点的xyz值
def get_node_xyz_map(nodeCsvFile):
    with open(nodeCsvFile, 'r', encoding='utf-8') as u:
        nodecv = pd.read_csv(u)
        nodecv = nodecv.where(nodecv.notnull(), None)
    node_xyz_map = {}
    for row in nodecv.iterrows():
        node_entity = NodeEntity()
        node_entity.NodeID = row[1]['NodeID']
        node_entity.x = row[1]['x']
        node_entity.y = row[1]['y']
        node_entity.z = row[1]['z']
        node_entity.NodeType = row[1]['NodeType']
        node_entity.lng = row[1]['lng']
        node_entity.lat = row[1]['lat']
        node_entity.alt = row[1]['alt']
    return node_xyz_map

# def cc(target_node_map):
#     ivics_link_dict = {}
#
#     for key in target_node_map:
#         print(f'{key}: {target_node_map[key]}')
#         target_node = target_node_map[key]
#         if target_node.
#
#     for direction in dir_dict.keys():
#         # mod by liangms 缺少进口道的方向不计算
#         if (len(dir_dict[direction]) == 0):
#             continue
#         upstream_node = 0
#         s_dir = 'left'
#
#         ivics_link_dict[direction] = {}
#         ivics_link_dict[direction]['roadlist'] = [
#             int(num) for num in dir_dict[direction]]
#         start, end = int(ivics_link_dict[direction]['roadlist'][0]), int(
#             ivics_link_dict[direction]['roadlist'][-1])
#         for rd in ivics_road:
#             if rd.id not in ivics_link_dict[direction]['roadlist']:
#                 continue
#
#             # 使用末尾road对左右车道进行校验
#             upstream_node, s_dir = parseSDir(
#                 ivics_link_dict, direction, rd, Node_ID, start, upstream_node, s_dir)
#             # if rd.id ==15294 :
#             # s_dir = 'right'
#         # mod by liangms
#         if (upstream_node is not None):
#             ivics_link_dict[direction]['upstreamNode'] = upstream_node
#         if (s_dir is not None):
#             ivics_link_dict[direction]['s_direction'] = s_dir
