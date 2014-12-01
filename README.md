python curl反防盗链抓取连接
===

curl 反盗链抓取网页内容

源码地址: https://github.com/maicong/OpenAPI/blob/master/curl_get.php
翻译为python版

依赖
---
需要安装pycurl

pycurl安装时如果ssl backend不同会报错

    import pycurl

    ImportError: pycurl: libcurl link-time ssl backend (openssl) is differ
    ent from compile-time ssl backend (gnutls)

    pip uninstall pycurl
    export PYCURL_SSL_LIBRARY=openssl
    pip install pycurl


Simple Usage
---

    from resist_hotlinking import curl_get

    print curl_get('http://www.baidu.com')
