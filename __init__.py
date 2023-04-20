"""Custom integration to integrate with HACS."""
import logging

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "example_hacs_integration"


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the example HACS integration."""
    _LOGGER.info("Setting up example HACS integration")
    return True


async def async_setup_entry(hass: HomeAssistant, entry: dict):
    """Set up example HACS from a config entry."""
    _LOGGER.info("Setting up example HACS entry")
    # TODO: Set up your HACS integration here
    return True


async def async_unload_entry(hass: HomeAssistant, entry: dict):
    """Unload a config entry."""
    _LOGGER.info("Unloading example HACS entry")
    # TODO: Unload resources allocated to your HACS integration here
    return True

