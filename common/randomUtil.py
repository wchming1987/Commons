#!/usr/bin/env python
# -*- coding=utf-8 -*-

import random
import string


class randomUtil():
    # 获取随机长度的随机字符串（包括数字和字母）
	@staticmethod
	def randStrAnyLen(len):
	    return ''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, len)))

    # 获取固定长度的随机字符串（包括数字和字母）
	@staticmethod
	def randStrFixedLen(len):
	    return ''.join(random.sample(string.ascii_letters + string.digits, len))

	
    # 获取随机长度的随机字母字符串
	@staticmethod
	def randAsciiStrAnyLen(len):
	    return ''.join(random.sample(string.ascii_letters, random.randint(1, len)))

    # 获取固定长度的随机字母字符串
	@staticmethod
	def randAsciiStrFixedLen(len):
	    return ''.join(random.sample(string.ascii_letters, len))

    # 获取随机长度的随机数字字符串
	@staticmethod
	def randNumStrAnyLen(len):
	    return ''.join(random.sample(string.digits, random.randint(1, len)))

    # 获取固定长度的随机数字字符串
	@staticmethod
	def randNumStrFixedLen(len):
	    return ''.join(random.sample(string.digits, len))

