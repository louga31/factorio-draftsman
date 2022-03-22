# boiler.py

from draftsman.classes import Entity
from draftsman.classes.mixins import DirectionalMixin
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import boilers

import warnings


class Boiler(DirectionalMixin, Entity):
    def __init__(self, name = boilers[0], **kwargs):
        # type: (str, **dict) -> None
        super(Boiler, self).__init__(name, boilers, **kwargs)

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )