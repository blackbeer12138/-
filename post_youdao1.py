import requests

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
   return '15867812304692'


def get_sign():
  return 'fb8c9ef0986f63434368a414e2ca90e8 '


def get_ts():
  import time
  t = time.time()
  ts = str(int(round(t * 1000)))
  return ts


from_data = {
  'i': '我和你',
  'from': 'AUTO',
  'to': 'AUTO',
  'smartresult': 'dict',
  'client': 'fanyideskweb',
  'salt': get_salt(),
  'sign': get_sign(),
  'ts': get_ts(),
  'bv': '0ed2e07b89acaa1301d499442c9fdf79',
  'doctype': 'json',
  'version': '2.1',
  'keyfrom': 'fanyi.web',
  'action': 'FY_BY_REALTlME',
}
response = requests.post(url, from_data)
print(response.text)