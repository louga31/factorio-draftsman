# tile.py

from draftsman.tile import Tile
from draftsman.error import InvalidTileError

from unittest import TestCase

class TileTesting(TestCase):
    def test_constructor(self):
        # Specific position
        tile = Tile("hazard-concrete-right", 100, -100)
        self.assertEqual(tile.name, "hazard-concrete-right")
        self.assertEqual(tile.position["x"],  100)
        self.assertEqual(tile.position["y"], -100)
        # Default position
        tile = Tile("hazard-concrete-right")
        self.assertEqual(tile.name, "hazard-concrete-right")
        self.assertEqual(tile.position["x"], 0)
        self.assertEqual(tile.position["y"], 0)
        # Invalid name
        with self.assertRaises(InvalidTileError):
            tile = Tile("weeeeee")

    def test_set_name(self):
        tile = Tile("hazard-concrete-left")
        self.assertEqual(tile.name, "hazard-concrete-left")
        self.assertEqual(tile.position["x"], 0)
        self.assertEqual(tile.position["y"], 0)
        tile.set_name("refined-hazard-concrete-left")
        self.assertEqual(tile.name, "refined-hazard-concrete-left")
        self.assertEqual(tile.position["x"], 0)
        self.assertEqual(tile.position["y"], 0)
        # Invalid name
        with self.assertRaises(InvalidTileError):
            tile.set_name("weeeeee")

    def test_set_position(self):
        tile = Tile("landfill", 0, 0)
        tile.set_position(-123, 123)
        self.assertEqual(tile.position["x"], -123)
        self.assertEqual(tile.position["y"], 123)

    def test_to_dict(self):
        tile = Tile("landfill", 123, 123)
        self.assertEqual(
            tile.to_dict(),
            {"name": "landfill", "position": {"x": 123, "y": 123}}
        )

    def test_repr(self):
        tile = Tile("concrete", 0, 0)
        self.assertEqual(
            str(tile),
            "<Tile>{'name': 'concrete', 'position': {'x': 0, 'y': 0}}"
        )
