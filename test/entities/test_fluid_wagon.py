# test_fluid_wagon.py

from draftsman.entity import FluidWagon, fluid_wagons
from draftsman.error import InvalidEntityError
from draftsman.warning import DraftsmanWarning

from schema import SchemaError

from unittest import TestCase

class FluidWagonTesting(TestCase):
    def test_constructor_init(self):
        fluid_wagon = FluidWagon(
            "fluid-wagon",
            position = {"x": 1.0, "y": 1.0},
            orientation = 0.75,
        )
        self.assertEqual(
            fluid_wagon.to_dict(),
            {
                "name": "fluid-wagon",
                "position": {"x": 1.0, "y": 1.0},
                "orientation": 0.75,
            }
        )

        # Warnings
        with self.assertWarns(DraftsmanWarning):
            FluidWagon("fluid-wagon", unused_keyword = "whatever")
        # Warn if the locomotive is not on a rail (close enough to one?)
        # TODO (Complex)

        # Errors
        with self.assertRaises(InvalidEntityError):
            FluidWagon("this is not a fluid wagon")
        with self.assertRaises(TypeError):
            FluidWagon("fluid-wagon", orientation = "wrong")