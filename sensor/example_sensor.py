"""Example sensor platform."""

"""
Dans `example_sensor.py`, nous avons créé une classe `ExampleSensor` 
qui hérite de la classe `Entity` de Home Assistant. 
La méthode `__init__`  initialise l'objet de capteur avec le nom 
et l'état spécifiés dans la configuration. Elle a également des méthodes 
pour récupérer le nom et l'état du capteur, ainsi qu'une méthode pour mettre à jour 
l'état du capteur.

Vous pouvez remplacer cet exemple par la définition de vos propres classes de capteurs, 
qui reflètent les fonctionnalités et le comportement de vos  propres capteurs.

"""

import logging

from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)


class ExampleSensor(Entity):
    """Example Sensor class."""

    def __init__(self, sensor_conf):
        """Initialize the Example Sensor."""
        self._name = sensor_conf.get("name")
        self._state = sensor_conf.get("state", None)

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the sensor state."""
        self._state = 42
        _LOGGER.debug("Updating %s", self.name)
