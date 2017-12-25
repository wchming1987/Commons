#!/usr/bin/env python
#-*- coding=UTF-8 -*-

from hashlib import md5
from hashlib import sha1
from hashlib import sha224
from hashlib import sha384
from hashlib import sha512

#__all__ = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'new', 'algorithms_guaranteed', 'algorithms_available', 'pbkdf2_hmac')  
#Python计算字符串的hash值  
class SecurUtil():

    @staticmethod
    def hashForString(method, srcbyte): 
        #将字符串和汉字转化成byte类型
        srcbyte = srcbyte.encode("utf-8")

        if method == 'md5':
            m = md5()
            m.update(srcbyte)
            srcbyte = m.hexdigest()
        elif method == 'sha1':
            s = sha1()
            s.update(srcbyte)
            srcbyte = s.hexdigest()
        elif method == 'sha224':
            s = sha224()
            s.update(srcbyte)
            srcbyte = s.hexdigest()
        elif method == 'sha384':
            s = sha384()
            s.update(srcbyte)
            srcbyte = s.hexdigest()
        elif method == 'sha512':
            s = sha512()
            s.update(srcbyte)
            srcbyte = s.hexdigest()

        return srcbyte

