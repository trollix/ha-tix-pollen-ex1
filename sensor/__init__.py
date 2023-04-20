"""Example sensor platform."""
from .example_sensor import ExampleSensor

DOMAIN = "example_hacs_integration"


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add sensors for passed config_entry in HA."""
    sensors = []
    for sensor_conf in config_entry.data.get("sensors", []):
        sensors.append(ExampleSensor(sensor_conf))
    async_add_entities(sensors)
