# vector.py
# -*- encoding: utf-8 -*-

"""
TODO
"""

from __future__ import unicode_literals, division

from typing import Union, Callable

PrimitiveVector = "Sequence[float, float]"


class Vector(object):
    """
    A simple 2d vector class, used to aid in developent and user experience.
    """

    def __init__(self, x, y):
        # type: (float, float, Vector) -> None
        """
        Constructs a new :py:class:`.Vector`.

        :param x: The x value.
        :param y: The y value.
        """
        self._data = [0, 0]
        self.update(x, y)

    @property
    def x(self):
        # type: () -> Union[float, int]
        """
        The x-coordinate of the point. Returns either a ``float`` or an ``int``,
        depending on the :py:class:`.Vector` queried.

        :getter: Gets the x-coordinate.
        :setter: Sets the x-coordinate.
        :type: Either ``float`` or ``int``.
        """
        return self._data[0]

    @x.setter
    def x(self, value):
        # type: (Union[float, int]) -> None
        self._data[0] = value

        # if self.linked:
        #     self.linked._data[0] = self.linked.transform_x(self._entity, value)

    @property
    def y(self):
        # type: () -> float
        """
        The y-coordinate of the vector. Returns either a ``float`` or an ``int``,
        depending on the :py:class:`.Vector` queried.

        :getter: Gets the y-coordinate.
        :setter: Sets the y-coordinate.
        :type: Either ``float`` or ``int``.
        """
        return self._data[1]

    @y.setter
    def y(self, value):
        # type: (Union[float, int]) -> None
        self._data[1] = value

        # if self.linked:
        #     self.linked._data[1] = self.linked.transform_y(self._entity, value)

    def transform_x(self, x):
        # type: (float) -> float
        """
        Calculates the value to set the linked vector's x coordinate with. Used
        to transform a change in the parent vector into a different change in
        the linked vector. Defaults to just setting the x value of the linked
        vector to the x value of the parent.
        """
        return x

    def transform_y(self, y):
        # type: (float) -> float
        """
        Calculates the value to set the linked vector's y coordinate with. Used
        to transform a change in the parent vector into a different change in
        the linked vector. Defaults to just setting the y value of the linked
        vector to the y value of the parent.
        """
        return y

    # =========================================================================

    @staticmethod
    def from_other(other, type_cast=float):
        # type: (Union[Vector, PrimitiveVector], Callable) -> Vector
        """
        Converts a PrimitiveVector into a :py:class:`.Vector`. Also handles the
        case where a :py:class:`.Vector` is already passed in, in which case that
        instance is simply returned. Otherwise, a new :py:class:`.Vector` is
        constructed, populated, and returned.

        :param point: The PrimitiveVector
        :param type_cast: The internal type to store data as.

        :returns: A new :py:class:`.Vector` with the same position as ``point``.
        """
        if isinstance(other, Vector):
            return other
        elif isinstance(other, (tuple, list)):
            return Vector(type_cast(other[0]), type_cast(other[1]))
        elif isinstance(other, dict):
            return Vector(type_cast(other["x"]), type_cast(other["y"]))
        else:
            raise TypeError("Could not resolve '{}' to a Vector object".format(other))

    def update(self, x, y):
        # type: (Union[float, int], Union[float, int], object) -> None
        """
        Updates the data of the existing vector in-place. Useful for preserving
        linked vectors.
        """
        self._data[0] = x
        self._data[1] = y

        # if self.linked:
        #     self.linked._data[0] = self.linked.transform_x(self._entity, x)
        #     self.linked._data[1] = self.linked.transform_y(self._entity, y)

    def update_from_other(self, other, type_cast=float):
        # type: (Union[Vector, PrimitiveVector], Callable) -> None
        """
        Updates the data of the existing vector in-place from a variable input
        format.

        :param other: The object to get the new set of data from
        :param type_cast: The data type to coerce the input variables towards.
        """
        if isinstance(other, Vector):
            self.update(other.x, other.y)
        elif isinstance(other, (tuple, list)):
            self.update(type_cast(other[0]), type_cast(other[1]))
        elif isinstance(other, dict):
            self.update(type_cast(other["x"]), type_cast(other["y"]))
        else:
            raise TypeError("Could not resolve '{}' to a Vector object".format(other))

    def to_dict(self):
        # type: () -> dict
        """
        Convert this vector to a Factorio-parseable dict with "x" and "y" keys.

        :returns: A dict of the format ``{"x": x, "y": y}``.
        """
        return {"x": self._data[0], "y": self._data[1]}

    # =========================================================================

    def __getitem__(self, index):
        # type: (int) -> Union[float, int]
        if index == "x":
            return self._data[0]
        elif index == "y":
            return self._data[1]
        else:
            return self._data[index]

    def __setitem__(self, index, value):
        # type: (int, Union[float, int]) -> None
        if index == "x":
            self._data[0] = value
        elif index == "y":
            self._data[1] = value
        else:
            self._data[index] = value

    def __add__(self, other):
        # type: (Union[Vector, PrimitiveVector, float, int]) -> Vector
        try:
            return Vector(self[0] + other[0], self[1] + other[1])
        except TypeError:
            return Vector(self[0] + other, self[1] + other)

    def __sub__(self, other):
        # type: (Union[Vector, PrimitiveVector, float, int]) -> Vector
        try:
            return Vector(self[0] - other[0], self[1] - other[1])
        except TypeError:
            return Vector(self[0] - other, self[1] - other)

    def __mul__(self, other):
        # type: (Union[Vector, PrimitiveVector, float, int]) -> Vector
        try:
            return Vector(self[0] * other[0], self[1] * other[1])
        except TypeError:
            return Vector(self[0] * other, self[1] * other)

    def __truediv__(self, other):
        # type: (Union[Vector, float, int]) -> Vector
        try:
            return Vector(self[0] / other[0], self[1] / other[1])
        except TypeError:
            return Vector(self[0] / other, self[1] / other)

    __div__ = __truediv__

    def __floordiv__(self, other):
        # type: (Union[Vector, float, int]) -> Vector
        try:
            return Vector(self[0] // other[0], self[1] // other[1])
        except TypeError:
            return Vector(self[0] // other, self[1] // other)

    def __eq__(self, other):
        # type: (Vector) -> bool
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __abs__(self):
        # type: () -> Vector
        return Vector(abs(self[0]), abs(self[1]))

    def __round__(self, precision=0):
        # type: (int) -> Vector
        return Vector(round(self[0], precision), round(self[1], precision))

    def __str__(self):  # pragma: no coverage
        # type: () -> str
        return "({}, {})".format(self._data[0], self._data[1])

    def __repr__(self):  # pragma: no coverage
        # type: () -> str
        return "<Vector>({}, {})".format(self._data[0], self._data[1])
