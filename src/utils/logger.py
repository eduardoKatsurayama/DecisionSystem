import logging
import sys

from pythonjsonlogger import jsonlogger


class StackdriverJsonFormatter(jsonlogger.JsonFormatter, object):
    def __init__(self, fmt="%(levelname) %(message) %(filename)s %(lineno)d",
                 style='%', *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

    def process_log_record(self, log_record):
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']
        return super(StackdriverJsonFormatter, self).process_log_record(
            log_record)

    def add_fields(self, log_record, record, message_dict):
        super(StackdriverJsonFormatter, self).add_fields(log_record,
                                                         record, message_dict)

        file_formated = "{}:{}".format(log_record['filename'],
                                       log_record['lineno'])
        log_record['module'] = file_formated
        del log_record['filename']
        del log_record['lineno']


handler = logging.StreamHandler(sys.stdout)
formatter = StackdriverJsonFormatter()
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
