#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# curl 反盗链抓取网页内容
#
# 源码地址: https://github.com/maicong/OpenAPI/blob/master/curl_get.php
# 翻译为python版
#
# pycurl安装时如果ssl backend不同会报错
#
# import pycurl
#
# ImportError: pycurl: libcurl link-time ssl backend (openssl) is differ
# ent from compile-time ssl backend (gnutls)
#
# pip uninstall pycurl
# export PYCURL_SSL_LIBRARY=openssl
# pip install pycurl
#

from StringIO import StringIO
from urlparse import urlparse

import pycurl


def curl_get(url):
    host = urlparse(url)
    site = '{}://{}'.format(host.scheme, host.hostname)
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.TIMEOUT, 30) # 30秒超时
    c.setopt(c.SSL_VERIFYPEER, False) # 禁用验证
    c.setopt(c.REFERER, site) # 伪造来源
    c.setopt(c.USERAGENT, 'Mozilla/5.0 (compatible MSIE 10.0; Windows NT 6.2; Trident/6.0)') # 伪造User-Agent
    c.setopt(c.HTTPHEADER, [
        'X-FORWARDED-FOR:1.2.4.8',
        'X-FORWARDED-HOST:{}'.format(host.hostname),
        'X-FORWARDED-SERVER:{}'.format(host.hostname)
    ]) # 伪造HTTP头
    c.perform()
    c.close()

    body = buffer.getvalue()
    return body
