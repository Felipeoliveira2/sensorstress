import eventlet

from st2reactor.sensor.base import Sensor

class StressSensor(Sensor):
    def __init__(self, sensor_service, config):
        super(StressSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        pass

    def run(self):
        while not self._stop:
            self._logger.debug('StressSensor dispatching trigger...')
        #############################################
            payload_result_snmp = {'servicestatus': 0}
        #############################################
            self.sensor_service.dispatch(trigger='sensorpack.event1', payload=payload_result_snmp)
            eventlet.sleep(1)

    def cleanup(self):
        self._stop = True

    # Methods required for programmable sensors.
    def add_trigger(self, trigger):
        pass

    def update_trigger(self, trigger):
        pass

    def remove_trigger(self, trigger):
        pass