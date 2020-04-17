import requests


url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
form_data={
    'i':' 我和你',
    'from':' AUTO',
    'to':' AUTO',
    'smartresult':' dict',
    'client':' fanyideskweb',
    'salt':' 15867812304692',
    'sign':' fb8c9ef0986f63434368a414e2ca90e8 ',
    'ts':' 1586781230469',
    'bv':' 37074a7035f34bfbf10d32bb8587564a',
    'doctype':' json',
    'version':' 2.1',
    'keyfrom':' fanyi.web',
    'action':' FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)