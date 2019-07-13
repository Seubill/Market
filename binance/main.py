# -*- coding:utf-8 -*-
import sys

import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
from quant import const
from quant.utils import tools
from quant.utils import logger
from quant.config import config
from quant.market import Market
from quant.market import Orderbook


class MyStrategy:

    def __init__(self):
        self.strategy = config.strategy
        self.platform = const.BINANCE
        self.symbol = config.symbol
        
        plt.ion()
        plt.figure(1)

        Market(const.MARKET_TYPE_ORDERBOOK, self.platform, self.symbol, self.on_event_orderbook_update)

    async def on_event_orderbook_update(self, orderbook: Orderbook):
        #logger.debug("orderbook:", orderbook, caller=self)
        logger.info("platform:", orderbook.platform)  # 打印行情平台
        logger.info("symbol:", orderbook.symbol)  # 打印行情交易对
        logger.info("asks:", orderbook.asks)  # 打印卖盘数据
        logger.info("bids:", orderbook.bids)  # 打印买盘数据 
        logger.info("timestamp:", orderbook.timestamp)  # 打印行情更新时间戳(毫秒)
        #plt.clf()
        #plt.plot(np.array(orderbook.bids))
        #plt.draw()


def main():
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = None

    from quant.quant import quant
    quant.initialize(config_file)
    MyStrategy()
    quant.start()



if __name__ == '__main__':
    main()
