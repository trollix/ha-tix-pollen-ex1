"""Example binary sensor platform."""
import logging

from homeassistant.components.binary_sensor import BinarySensorEntity

_LOGGER = logging.getLogger(__name__)


class ExampleBinarySensor(BinarySensorEntity):
    """Example Binary Sensor class."""

    def __init__(self, binary_sensor_conf):
        """Initialize the Example Binary Sensor."""
        self._name = binary_sensor_conf.get("name")
        self._state = binary_sensor_conf.get("state", False)

    @property
    def name(self):
        """Return the name of the binary sensor."""
        return self._name

    @property
    def is_on(self):
        """Return the state of the binary sensor."""
        return self._state
