from django.test import TestCase

# Create your tests here.
import json
#序列号：将数据对象转换为一个标准格式字符串，比如json字符串
data_dic = {'name':"rain", 'age':22, 'is_married':False}
print(json.dumps(data_dic))

data_list = [{'name':"rains"},{'name':'jack'}]
data_set = ({'name':"rains"},{'name':'jack'})

print(json.dumps(data_set))

#反序列号
json_data = json.dumps(data_dic)
data = json.loads(json_data)
print(data, type(data))