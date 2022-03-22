# rail_chain_signal.py

from draftsman.classes import Entity
from draftsman.classes.mixins import (
    ReadRailSignalMixin, ControlBehaviorMixin, CircuitConnectableMixin, 
    EightWayDirectionalMixin
)
from draftsman import signatures
from draftsman.utils import signal_dict
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import rail_chain_signals

from schema import SchemaError
from typing import Union
import warnings


class RailChainSignal(ReadRailSignalMixin, ControlBehaviorMixin, 
                      CircuitConnectableMixin, EightWayDirectionalMixin, 
                      Entity):
    """
    """
    def __init__(self, name = rail_chain_signals[0], **kwargs):
        # type: (str, **dict) -> None
        super(RailChainSignal, self).__init__(
            name, rail_chain_signals, **kwargs
        )

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )

    # =========================================================================

    @property
    def blue_output_signal(self):
        # type: () -> dict
        """
        TODO
        """
        return self.control_behavior.get("blue_output_signal", None)

    @blue_output_signal.setter
    def blue_output_signal(self, value):
        # type: (Union[str, dict]) -> None
        if value is None:
            self.control_behavior.pop("blue_output_signal", None)
        elif isinstance(value, str):
            self.control_behavior["blue_output_signal"] = signal_dict(value)
        else: # dict or other
            try:
                value = signatures.SIGNAL_ID.validate(value)
                self.control_behavior["blue_output_signal"] = value
            except SchemaError:
                raise TypeError("Incorrectly formatted SignalID")