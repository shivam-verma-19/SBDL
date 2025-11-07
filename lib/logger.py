# lib/logger.py
import logging

class Log4j:
    def __init__(self, spark, force_python_log=False):
        if hasattr(spark, "_jvm") and not force_python_log:
            self.logger = spark._jvm.org.apache.log4j.LogManager.getLogger(__name__)
            self.use_log4j = True
        else:
            self.logger = logging.getLogger(__name__)
            logging.basicConfig(level=logging.INFO,
                                format="%(asctime)s [%(levelname)s] %(message)s")
            self.use_log4j = False

    def info(self, msg):
        if self.use_log4j:
            self.logger.info(msg)
        else:
            self.logger.info(msg)

