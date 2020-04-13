import requests

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
  return ''


def get_sign():
  return ''


def get_ts():
  return ''


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