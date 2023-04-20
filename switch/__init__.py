"""Example switch platform."""
from .example_switch import ExampleSwitch

DOMAIN = "example_hacs_integration"


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add switches for passed config_entry in HA."""
    switches = []
    for switch_conf in config_entry.data.get("switches", []):
        switches.append(ExampleSwitch(switch_conf))
    async_add_entities(switches)
