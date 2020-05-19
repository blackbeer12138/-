import unittest

from tianqi.city_weather import HeFeng

from tianqi.city_weather_db import HefengDb


class TestCase(unittest.TestCase):

    def test_save(self):
        hefengDb = HefengDb()
        hefengDb.save({"name": "wufangmiao", "class": "net19049"})
        hefengDb.show_all()
        results = hefengDb.find({"name": "wufangmiao"})
        for each in results:
            self.assertEqual("wufangmiao", each['name'])
            self.assertEqual("net19049", each['class'])
        hefengDb.delete()

    def test_save_all(self):
        hefeng = HeFeng()
        # codes = hefeng.get_city_code()
        # for each in codes:
        #   print(next(codes))
        weathers = hefeng.get_weather(7)
        hefengDb = HefengDb()
        hefengDb.save_all(weathers)
        print("show_all")
        hefengDb.show_all()
        self.assertEqual(7,hefengDb.count())
        hefengDb.delete()


if __name__ == '__main__':
    unittest.main()