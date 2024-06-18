import threading

class SingletonMeta(type):
    _instances = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]
    
    
class ConfigurationManager(metaclass=SingletonMeta):
    def __init__(self):
        self._config = {}

    def get_config(self, key):
        return self._config.get(key)

    def set_config(self, key, value):
        self._config[key] = value


obj1 = ConfigurationManager()
obj2 = ConfigurationManager()

print(obj1 is obj2)