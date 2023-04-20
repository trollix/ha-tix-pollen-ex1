"""Example climate platform."""
from .example_climate import ExampleClimate

DOMAIN = "example_hacs_integration"


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Add climate devices for passed config_entry in HA."""
    climates = []
    for climate_conf in config_entry.data.get("climates", []):
        climates.append(ExampleClimate(climate_conf))
    async_add_entities(climates)
