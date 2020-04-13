import unittest
from post_youdao import *

class postyoudaotext(unittest.TestCase):
    def text_someing(self):
        self.assertEqual(True,True)

    def text_get_ts(self):
        get_ts=mock.Mock(return_valve='1584684880395')
        self.assertEqual('1584684880395',)

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15846848803956')
        self.assertEqual('15846848803956',get_salt())
if __name__ == '__main__':
    unittest.main()
