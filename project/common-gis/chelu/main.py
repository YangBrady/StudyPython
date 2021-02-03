from parse_node import parse_junction
import sys

sys.path.append("..")

import env.config as conf
import datetime
import logging

import common.logger as logger
import common.utils as utils
import pandas as pd


def main():
    # 设置log的基本配置
    # logger.configLog(conf.log_file)
    logger.configLog(conf.log_file, conf.log_enable_console)

    # 根据target文件的id和文件路径进行解析
    main_start_time = datetime.datetime.now()
    with open(conf.target_csv_file, 'r', encoding='utf-8') as f:
        junction_nodes = pd.read_csv(f)
        node_index = 0
        node_count = len(junction_nodes)
        estimate_time = node_count * (15 / 60)  # 预计花费时间
        logging.info("---begin parsing json: total[" + str(node_count) + "], estimate_time="
                     + str(estimate_time) + "min ---")
        for row in junction_nodes.iterrows():
            node_index += 1
            input_file = "./input/" + row[1]['xodrFile']
            # 上等变量NodeID 更改变量对应输入Target_Nodes表中的NodeID来完成目标点的变换
            # node_id = 19684
            node_id = row[1]['NodeID']
            start_time = datetime.datetime.now()
            parse_junction(input_file, conf.output_dir, node_id, conf.node_csv_file, conf.target_csv_file)

    logging.info("---all finish parse time: " + str(utils.getTimeSpanMin(main_start_time)) + 'min')


if __name__ == "__main__":
    main()
