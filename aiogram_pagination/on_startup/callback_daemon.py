import time

from ..data.config import configurator
from ..data.loader import storages


class CallbackDaemon:

    def __init__(self):
        self.configurator = configurator
        self.cache_time_limit = self.configurator.config['cache_time_limit']
        self.callback_storage = storages.get_storage(self.configurator.config)

    def run_callback_daemon(self):
        while True:
            self.callback_storage.on_callbacks_exceeding_time_limit(self.cache_time_limit)
            time.sleep(3600)
