from tianqi.city_weather_db import HefengDb
from tianqi.city_weather import HeFeng

if __name__ == '__main__':
    hefeng=HeFeng()
    weathers=hefeng.get_all_weather(50)
    hefengdb=HefengDb()
    hefengdb.save_all(weathers)
    hefengdb.show_all()