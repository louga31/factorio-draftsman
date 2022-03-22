# solar_panel.py

from draftsman.classes import Entity
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import solar_panels

import warnings


class SolarPanel(Entity):
    def __init__(self, name = solar_panels[0], **kwargs):
        # type: (str, **dict) -> None
        super(SolarPanel, self).__init__(name, solar_panels, **kwargs)

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )