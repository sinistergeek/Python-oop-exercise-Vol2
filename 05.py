import time
class Container:

    def get_current_time():
        return time.strftime('%H:%M:%s', time.localtime())

    get_current_time = staticmethod(get_current_time)
