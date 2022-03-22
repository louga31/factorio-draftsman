# train_stop.py

from draftsman.classes import Entity
from draftsman.classes.mixins import (
    ColorMixin, CircuitConditionMixin, EnableDisableMixin, 
    LogisticConditionMixin, ControlBehaviorMixin, CircuitConnectableMixin,
    DoubleGridAlignedMixin, DirectionalMixin
)
import draftsman.signatures as signatures
from draftsman.utils import signal_dict
from draftsman.warning import DraftsmanWarning

from draftsman.data.entities import train_stops

from schema import SchemaError
from typing import Union
import warnings


class TrainStop(ColorMixin, CircuitConditionMixin, EnableDisableMixin, 
                LogisticConditionMixin, ControlBehaviorMixin, 
                CircuitConnectableMixin, DoubleGridAlignedMixin, 
                DirectionalMixin, Entity):
    """
    """
    def __init__(self, name = train_stops[0], **kwargs):
        # type: (str, **dict) -> None
        super(TrainStop, self).__init__(name, train_stops, **kwargs)

        self.station = None
        if "station" in kwargs:
            self.station = kwargs["station"]
            self.unused_args.pop("station")
        self._add_export("station", lambda x: x is not None)

        self.manual_trains_limit = None
        if "manual_trains_limit" in kwargs:
            self.manual_trains_limit = kwargs["manual_trains_limit"]
            self.unused_args.pop("manual_trains_limit")
        self._add_export("manual_trains_limit", lambda x: x is not None)

        for unused_arg in self.unused_args:
            warnings.warn(
                "{} has no attribute '{}'".format(type(self), unused_arg),
                DraftsmanWarning,
                stacklevel = 2
            )

    # =========================================================================

    @property
    def station(self):
        # type: () -> str
        """
        TODO
        """
        return self._station

    @station.setter
    def station(self, value):
        # type: (str) -> None
        if value is None or isinstance(value, str):
            self._station = value
        else:
            raise TypeError("'station' must be a str or None")

    # =========================================================================

    @property
    def manual_trains_limit(self):
        # type: () -> int
        """
        TODO
        """
        return self._manual_trains_limit

    @manual_trains_limit.setter
    def manual_trains_limit(self, value):
        # type: (int) -> None
        if value is None or isinstance(value, int):
            self._manual_trains_limit = value
        else:
            raise TypeError("'manual_trains_limit' must be an int or None")

    # =========================================================================

    @property
    def read_from_train(self):
        # type: () -> bool
        """
        TODO
        """
        return self.control_behavior.get("read_from_train", None)

    @read_from_train.setter
    def read_from_train(self, value):
        # type: (bool) -> None
        if value is None:
            self.control_behavior.pop("read_from_train", None)
        elif isinstance(value, bool):
            self.control_behavior["read_from_train"] = value
        else:
            raise TypeError("'read_from_train' must be a bool or None")

    # =========================================================================

    @property
    def read_stopped_train(self):
        # type: () -> bool
        """
        TODO
        """
        return self.control_behavior.get("read_stopped_train", None)

    @read_stopped_train.setter
    def read_stopped_train(self, value):
        # type: (bool) -> None
        if value is None:
            self.control_behavior.pop("read_stopped_train", None)
        elif isinstance(value, bool):
            self.control_behavior["read_stopped_train"] = value
        else:
            raise TypeError("'read_stopped_train' must be a bool or None")

    # =========================================================================

    @property
    def train_stopped_signal(self):
        # type: () -> dict
        """
        TODO
        """
        return self.control_behavior.get("train_stopped_signal", None)

    @train_stopped_signal.setter
    def train_stopped_signal(self, value):
        # type: (Union[str, dict]) -> None
        if value is None:
            self.control_behavior.pop("train_stopped_signal", None)
        elif isinstance(value, str):
            value = signal_dict(value)
            self.control_behavior["train_stopped_signal"] = value
        else: # dict or other
            try:
                value = signatures.SIGNAL_ID.validate(value)
                self.control_behavior["train_stopped_signal"]=value
            except SchemaError:
                raise TypeError("Incorrectly formatted SignalID")

    # =========================================================================

    @property
    def signal_limits_trains(self):
        # type: () -> bool
        """
        TODO
        """
        return self.control_behavior.get("set_trains_limit", None)

    @signal_limits_trains.setter
    def signal_limits_trains(self, value):
        # type: (bool) -> None
        if value is None:
            self.control_behavior.pop("set_trains_limit", None)
        elif isinstance(value, bool):
            self.control_behavior["set_trains_limit"] = value
        else:
            raise TypeError("'set_trains_limit' must be a bool or None")

    # =========================================================================

    @property
    def trains_limit_signal(self):
        # type: () -> dict
        """
        TODO
        """
        return self.control_behavior.get("trains_limit_signal", None)

    @trains_limit_signal.setter
    def trains_limit_signal(self, value):
        # type: (Union[str, dict]) -> None
        if value is None:
            self.control_behavior.pop("trains_limit_signal", None)
        elif isinstance(value, str):
            value = signal_dict(value)
            self.control_behavior["trains_limit_signal"] = value
        else: # dict or other
            try:
                value = signatures.SIGNAL_ID.validate(value)
                self.control_behavior["trains_limit_signal"] = value
            except SchemaError:
                raise TypeError("Incorrectly formatted SignalID")

    # =========================================================================

    @property
    def read_trains_count(self):
        # type: () -> bool
        """
        TODO
        """
        return self.control_behavior.get("read_trains_count", None)

    @read_trains_count.setter
    def read_trains_count(self, value):
        # type: (bool) -> None
        if value is None:
            self.control_behavior.pop("read_trains_count", None)
        elif isinstance(value, bool):
            self.control_behavior["read_trains_count"] = value
        else:
            raise TypeError("'read_trains_count' must be a bool or None")

    # =========================================================================

    @property
    def trains_count_signal(self):
        # type: () -> dict
        """
        TODO
        """
        return self.control_behavior.get("trains_count_signal", None)

    @trains_count_signal.setter
    def trains_count_signal(self, value):
        # type: (Union[str, dict]) -> None
        if value is None:
            self.control_behavior.pop("trains_count_signal", None)
        elif isinstance(value, str):
            value = signal_dict(value)
            self.control_behavior["trains_count_signal"] = value
        else: # dict or other
            try:
                value = signatures.SIGNAL_ID.validate(value)
                self.control_behavior["trains_count_signal"] = value
            except SchemaError:
                raise TypeError("Incorrectly formatted SignalID")