import json
a={"data":{"deposit_amount":0,"deposit_time":"2016-04-28 10:54:19","balance_type_id":1,"result_code":0,"balance_after":"500","balance_before":"500"},"return_code":0,"return_message":"success"}
a_str=json.dumps(a)
print a_str

data=json.loads(a_str)
print data
print data.get('data')

code=int(-11)
if code not in [0,-11]:
    print 'aaaa'
else:
    print 'bbbb'
