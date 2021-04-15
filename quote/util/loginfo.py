import logging
import time


class Loginfo:
    def __init__(self):
        self.logger = logging.getLogger('lin zhang')

    def set_message(self,lever,msg):
        try:
            # 创建时间
            now = time.strftime('%Y-%m-%d')
            # print(now)
            # 创建日志文件输出
            fh = logging.FileHandler('../../log/log'+now+'.log')
            # 创建控制台输出流
            ch = logging.StreamHandler()

            # 创建输出格式
            fm = logging.Formatter('%(name)s--%(asctime)s--%(levelname)s--%(message)s')
            # 日志文件设置输出格式
            fh.setFormatter(fm)
            # 控制端文件设置输出格式
            ch.setFormatter(fm)
            # 文件对象加入logger
            self.logger.addHandler(fh)
            # 控制台对象加入logger
            self.logger.addHandler(ch)
            # 设置logger出入级别
            self.logger.setLevel(level=logging.DEBUG)
            # 打印消息
            # logger.info('this is info message')
            if lever == 'debug':
                self.logger.debug(msg)
            elif lever == 'info':
                self.logger.info(msg)
            elif lever == 'warning':
                self.logger.warning(msg)
            elif lever == 'error':
                self.logger.error(msg)
            elif lever == 'critical':
                self.logger.critical(msg)
            else:
                print('lever is error')
            # 移除文件handler
            self.logger.removeHandler(fh)
            # 移除控制台handler
            self.logger.removeHandler(ch)
        except Exception as e:
            print(e,'file operation error')
        finally:
            # 关闭文件handler
            fh.close()
            # 关闭控制台handler
            ch.close()