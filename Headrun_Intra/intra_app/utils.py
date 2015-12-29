#!/usr/bin/env python

from __future__ import division
import os
import sys
import logging
import time
import json
import re

class BaseClass():

    def get_log_file_path(self, file_name):
        if not file_name.endswith('.log'):
            file_name = file_name.strip() + '.log'

        base_dir = '/var/log/'
        log_dir = os.path.join(base_dir, 'intra.headrun.com')
        self.ensure_dir_exists(log_dir)
        log_file = os.path.join(log_dir, file_name)
        return log_file

    def ensure_dir_exists(self, dir_name):
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)

    def init_logger(self, file_name, debug_mode = False):
        file_path = self.get_log_file_path(file_name)
        log = logging.getLogger(file_path)
        if file_name != 'stats':
            handler   = logging.handlers.RotatingFileHandler(file_path, maxBytes=52428800, backupCount=1000)
            formatter = logging.Formatter('%(asctime)s.%(msecs)d: %(filename)s: %(lineno)d: %(funcName)s: %(levelname)s: %(message)s', "%Y%m%dT%H%M%S")
        else :
            handler = logging.FileHandler(file_path,mode='a')
            formatter = logging.Formatter('%(message)s')

        handler.setFormatter(formatter)
        log.addHandler(handler)
        if debug_mode:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.INFO)
        return log

    def close_log_handlers(self, log):
        handlers = log.handlers[:]
        for handler in handlers:
            handler.close()

    def get_error_msg(self, e):
        error_msg = e.message
        if not error_msg and len(e.args) == 2:
            error_msg = e.args[-1]
        return error_msg

    def get_required_fileds(self, model_class):
        if not isinstance(model_class, ModelBase):
            return []

        pr_field = model_class._meta.pk
        return [i.name for i in model_class._meta.fields if not i.blank and i != pr_field]

    def parse_model_dict(self, act_dict):
        resl_dict = {}
        for key, value in act_dict.iteritems():
            if isinstance(value, dict):
                resl_dict.update(self.parse_model_dict(value))
            elif isinstance(value, list):
                if key == 'role':
                    values = []
                    for _val in value:
                        values.extend(_val.values())
                    resl_dict[key] = ", ".join(values)
                else:
                    resl_dict[key] = value
            else:
                resl_dict[key] = value
        return resl_dict

    def parse_request_body(self, request):
        try:
            parsed_data = json.loads(request.body)
        except:
            try:
                parsed_data = eval(request.body)
            except:
                parsed_data = {}

        return parsed_data

    def parse_json_data(self, data):
        try:
            parsed_data = json.loads(data)
        except:
            try:
                parsed_data = eval(data)
            except:
                parsed_data = {}

        return parsed_data

    def is_mobile_request(self, request):
        status = False
        ua = request.META.get('HTTP_USER_AGENT', '')
        if not ua:
            return status

        is_android = re.search('android', ua, re.IGNORECASE)
        is_iphone  = re.search('iphone', ua, re.IGNORECASE)
        is_ipad    = re.search('ipad', ua, re.IGNORECASE)
        if is_android or is_iphone or is_ipad:
            status = True

        return status

def main():
    pass

if __name__ == '__main__':
    main()
