"""Example custom light platform."""

DOMAIN = "example_light"

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Example custom light platform."""
    add_entities([ExampleLight()])


class ExampleLight(LightEntity):
    """Example Light."""

    def __init__(self):
        """Initialize an example light."""
        self._state = False

    @property
    def name(self):
        """Return the name of the light."""
        return "Example Light"

    @property
    def is_on(self):
        """Return the state of the light."""
        return self._state

    def turn_on(self, **kwargs):
        """Turn the light on."""
        self._state = True

    def turn_off(self, **kwargs):
        """Turn the light off."""
        self._state = False
