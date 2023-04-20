"""Example switch platform."""
import logging

from homeassistant.components.switch import SwitchEntity

_LOGGER = logging.getLogger(__name__)


class ExampleSwitch(SwitchEntity):
    """Example Switch class."""

    def __init__(self, switch_conf):
        """Initialize the Example Switch."""
        self._name = switch_conf.get("name")
        self._state = switch_conf.get("state", False)

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def is_on(self):
        """Return the state of the switch."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        self._state = True
        _LOGGER.debug("Turning on %s", self.name)

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        self._state = False
        _LOGGER.debug("Turning off %s", self.name)
