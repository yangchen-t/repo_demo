import logging
import sys,os
def data_status(debug,info,warning,error,critical):
                        logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                                filename='output.csv',
                                filemode='w',  ##有w和a，w就是写模式，每次都会重新写日志 #a是追加模式，默认如果不写的话，就是追加模式
                                format=
                                '{ %(created)f- %(funcName)s -  [%(levelname)s] }:= %(message)s'
                                # 日志格式
                                )
                        logger = logging.getLogger('simpleExample')
                        logger.debug(debug)
                        logger.info(info)
                        logger.warning(warning)
                        logger.error(error)
                        logger.critical(critical)
                # data_status(debug=a,info=b,warning=c,error=d,critical=e)

        # data_status(a,b,c,d,e)
data_status()
