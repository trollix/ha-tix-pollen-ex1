"""Example climate platform."""
import logging

from homeassistant.components.climate import ClimateEntity
from homeassistant.const import TEMP_CELSIUS

_LOGGER = logging.getLogger(__name__)


class ExampleClimate(ClimateEntity):
    """Example Climate class."""

    def __init__(self, climate_conf):
        """Initialize the Example Climate."""
        self._name = climate_conf.get("name")
        self._target_temperature = climate_conf.get("target_temperature", 20.0)
        self._current_temperature = climate_conf.get("current_temperature", 20.0)
        self._current_humidity = climate_conf.get("current_humidity", 50.0)

    @property
    def name(self):
        """Return the name of the climate device."""
        return self._name

    @property
    def temperature_unit(self):
        """Return the unit of measurement used by the platform."""
        return TEMP_CELSIUS

    @property
    def target_temperature(self):
        """Return the target temperature of the climate device."""
        return self._target_temperature

    async def async_set_temperature(self, **kwargs):
        """Set the target temperature of the climate device."""
        temperature = kwargs.get("temperature")
        if temperature is not None:
            self._target_temperature = temperature
            _LOGGER.debug("Setting temperature to %s", temperature)

    @property
    def current_temperature(self):
        """Return the current temperature of the climate device."""
        return self._current_temperature

    @property
    def current_humidity(self):
        """Return the current humidity of the climate device."""
        return self._current_humidity
