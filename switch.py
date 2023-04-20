"""Example switch platform."""
import logging

from homeassistant.components.switch import SwitchEntity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "example_hacs_integration"


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add switches for passed config_entry in HA."""
    switches = []
    for switch_conf in config_entry.data.get("switches", []):
        switches.append(ExampleSwitch(switch_conf))
    async_add_entities(switches)


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
        """Return true if the switch is on."""
        return self._state

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        self._state = True
        _LOGGER.debug("Turning on %s", self.name)

    async def async_turn_off(self, **kwargs):
        """Turn the switch off."""
        self._state = False
        _LOGGER.debug("Turning off %s", self.name)
