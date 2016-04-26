# -*- coding:utf-8 -*-
# raise 抛出异常
def ThorwErr(value):
    try:
        print value
        a=1/value
        print a
    except Exception, e:
        print '=====duplicate_key=====user_id:',value
        return
def ThorwEx(value):
    if value==0:
        raise Exception('exception-------')

def ThorwExTest(value):
    try:
        a=1/value
    except Exception,e:
        raise e

print '1'
import datetime
print datetime.date.today()

ThorwErr(0)
print '2'
ThorwEx(1)
print '3'
ThorwExTest(0)
print '4'
