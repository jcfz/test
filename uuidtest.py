# -*- coding: utf-8 -*-
import uuid

name='test_name'
namespace=12


print uuid.uuid1().hex
#print uuid.uuid3(namespace,name)
print uuid.uuid4().hex
#print uuid.uuid5(namespace,name)
