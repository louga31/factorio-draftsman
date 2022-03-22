# logistic_buffer_container.py

from draftsman.classes import Entity
from draftsman.classes.mixins import (
    ModeOfOperationMixin, ControlBehaviorMixin, CircuitConnectableMixin,
    RequestFiltersMixin, InventoryMixin
)
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import logistic_buffer_containers

import warnings


class LogisticBufferContainer(ModeOfOperationMixin, ControlBehaviorMixin, 
                              CircuitConnectableMixin, RequestFiltersMixin, 
                              InventoryMixin, Entity):
    """
    """
    def __init__(self, name = logistic_buffer_containers[0], **kwargs):
        # type: (str, **dict) -> None
        super(LogisticBufferContainer, self).__init__(
            name, logistic_buffer_containers, **kwargs
        )

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )