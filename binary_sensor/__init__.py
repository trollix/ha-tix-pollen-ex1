"""Example binary sensor platform."""
from .example_binary_sensor import ExampleBinarySensor

DOMAIN = "example_hacs_integration"


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add binary sensors for passed config_entry in HA."""
    binary_sensors = []
    for binary_sensor_conf in config_entry.data.get("binary_sensors", []):
        binary_sensors.append(ExampleBinarySensor(binary_sensor_conf))
    async_add_entities(binary_sensors)