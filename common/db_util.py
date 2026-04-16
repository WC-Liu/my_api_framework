import pymysql
from common.logger import logger
from common.path_util import get_path
from config.settings import (
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DB
)


class DBUtil:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        """连接 MySQL"""
        try:
            self.conn = pymysql.connect(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB,
                charset="utf8",
                #cursorclass=pymysql.cursors.DictCursor
            )
            # 创建数据库游标，.DictCursor返回字典
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            logger.info("✅ MySQL 连接成功！")
        except Exception as e:
            logger.error(f"❌ MySQL 连接失败：{e}")
            raise

    def query(self, sql, args=None):
        """查询数据"""
        try:
            # 当失败重跑时，检测到断连自动重连
            if not self.conn or not self.conn.open:
                self.connect()
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error(f"❌ 查询失败：{e}")
            raise


    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            logger.info("✅ MySQL 连接已关闭")
        except:
            pass


# 全局单例（避免重复创建连接）
db = DBUtil()