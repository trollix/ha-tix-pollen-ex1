"""Example custom light platform."""

import voluptuous as vol

from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_COLOR_TEMP,
    ATTR_HS_COLOR,
    PLATFORM_SCHEMA,
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
    SUPPORT_COLOR_TEMP,
    LightEntity,
)
import homeassistant.helpers.config_validation as cv

from . import DOMAIN

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({vol.Required("name"): cv.string})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Example custom light platform."""
    add_entities([ExampleLight(config["name"])])


class ExampleLight(LightEntity):
    """Example Light."""

    def __init__(self, name):
        """Initialize an example light."""
        self._name = name
        self._state = False
        self._brightness = 255
        self._color_temp = 366

    @property
    def name(self):
        """Return the name of the light."""
        return self._name

    @property
    def is_on(self):
        """Return the state of the light."""
        return self._state

    @property
    def brightness(self):
        """Return the brightness of the light."""
        return self._brightness

    @property
    def color_temp(self):
        """Return the color temperature of the light."""
        return self._color_temp

    def turn_on(self, **kwargs):
        """Turn the light on."""
        if ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]

        if ATTR_COLOR_TEMP in kwargs:
            self._color_temp = kwargs[ATTR_COLOR_TEMP]

        if ATTR_HS_COLOR in kwargs:
            hs_color = kwargs[ATTR_HS_COLOR]
            self._color_temp = int(hs_color[0] * 653.5)
            self._brightness = hs_color[1]

        self._state = True

    def turn_off(self, **kwargs):
        """Turn the light off."""
        self._state = False
