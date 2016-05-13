# -*- coding:utf-8 -*-

s='你好！'
s1='你好'
if s1!=s:
    print '===='
else:
    print '!='
#cmp
s='abc'
s1='a'
s2='bc'
s3='abc'

print cmp(s,s1)
print cmp(s,s2)
print cmp(s,s3)

#is
s4=s1+s2
print s4
print s is s1
print s is s4
print s4 is s
print s is s3
