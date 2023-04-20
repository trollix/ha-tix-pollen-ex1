"""Example sensor platform."""
import logging

from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "example_hacs_integration"


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add sensors for passed config_entry in HA."""
    sensors = []
    for sensor_conf in config_entry.data.get("sensors", []):
        sensors.append(ExampleSensor(sensor_conf))
    async_add_entities(sensors)


class ExampleSensor(Entity):
    """Example Sensor class."""

    def __init__(self, sensor_conf):
        """Initialize the Example Sensor."""
        self._name = sensor_conf.get("name")
        self._state = sensor_conf.get("state", None)

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the sensor state."""
        self._state = 42
        _LOGGER.debug("Updating %s", self.name)
