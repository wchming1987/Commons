#!/usr/bin/env python
#-*- coding=UTF-8 -*-

import httplib2
import json
import random
import string
import time
import urllib

from securUtil import SecurUtil


class smsUtil():

    @staticmethod
    def baseHTTPSRequest(url, data):

        # 配置 HTTP Request Header
        AppKey = '1958cd7bc542a299b0c3bc428f14006e'
        AppSecret = 'a3774be7f5a4'
        Nonce = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 62)))
        CurTime = '%.0f' % time.time()
        CheckSum = SecurUtil.hashForString('sha1', '%s%s%s' % (AppSecret, Nonce, CurTime))

        headers = {}
        headers['AppKey'] = AppKey
        headers['Nonce'] = Nonce
        headers['CurTime'] = CurTime
        headers['CheckSum'] =CheckSum
        headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
        print(headers)

        # 将数据转换为 JSON 格式
        #json_data = json.dumps(data)
        #print(json_data)

        conn = httplib2.Http(disable_ssl_certificate_validation=True)
        resp, content = conn.request('https://api.netease.im/sms/sendtemplate.action', method='POST', body=urllib.urlencode(data), headers=headers)
        print(resp.status)
        print(content)

        return resp.status, content

    @staticmethod
    def sendTemplate(templateid, mobiles, params):
        url = 'https://api.netease.im:443/sms/sendtemplate.action'

        data = {}
        data['templateid'] = templateid
        data['mobiles'] = mobiles
        data['params'] = params

        smsUtil.baseHTTPSRequest(url, data)

