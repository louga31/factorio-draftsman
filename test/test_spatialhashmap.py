# test_spatialhashmap.py

from draftsman.blueprint import SpatialHashMap
from draftsman.tile import Tile

from unittest import TestCase


class SpatialHashMapTesting(TestCase):
    def test_init(self):
        map = SpatialHashMap()
        self.assertEqual(map.map, {})
        self.assertEqual(map.cell_size, 8)

        self.assertEqual(
            map.map_coords(10, 10),
            (1, 1)
        )

    def test_add(self):
        map = SpatialHashMap()
        tile_to_add = Tile("refined-concrete", 0, 0)
        map.add(tile_to_add)
        self.assertEqual(map.map, {(0, 0): [tile_to_add]})
        other_tile_to_add = Tile("landfill", 1, 1)
        map.add(other_tile_to_add)
        self.assertEqual(
            map.map, 
            {
                (0, 0): [
                    tile_to_add, other_tile_to_add
                ]
            }
        )

    def test_remove(self):
        map = SpatialHashMap()
        tile_to_add = Tile("refined-concrete", 0, 0)
        map.add(tile_to_add)
        other_tile_to_add = Tile("landfill", 1, 1)
        map.add(other_tile_to_add)
        map.remove(other_tile_to_add)
        self.assertEqual(
            map.map,
            {
                (0, 0): [
                    tile_to_add
                ]
            }
        )
        map.remove(tile_to_add)
        self.assertEqual(map.map, {})
        map.remove(Tile("landfill", 0, 0))
        self.assertEqual(map.map, {})
        pass

    def test_get_in_radius(self):
        map = SpatialHashMap()
        tile_to_add = Tile("refined-concrete", 0, 0)
        map.add(tile_to_add)
        other_tile_to_add = Tile("landfill", 10, 0)
        map.add(other_tile_to_add)
        another_tile_to_add = Tile("refined-hazard-concrete-left", 7, 7)
        map.add(another_tile_to_add)
        results = map.get_in_radius(5, (0, 0))
        self.assertEqual(
            results,
            [tile_to_add]
        )
        results = map.get_in_radius(100, (0, 0))
        self.assertEqual(
            results,
            [tile_to_add, another_tile_to_add, other_tile_to_add]
        )
        results = map.get_in_radius(100, (0, 0), limit = 1)
        self.assertEqual(
            results,
            [tile_to_add]
        )

    def test_get_on_point(self):
        map = SpatialHashMap()
        tile_to_add = Tile("refined-concrete", 0, 0)
        map.add(tile_to_add)
        results = map.get_on_point((0, 0))
        self.assertEqual(
            results,
            [tile_to_add]
        )
        other_tile_to_add = Tile("landfill", 0, 0)
        map.add(other_tile_to_add)
        results = map.get_on_point((0, 0))
        self.assertEqual(
            results,
            [tile_to_add, other_tile_to_add]
        )
        results = map.get_on_point((0, 0), limit = 1)
        self.assertEqual(
            results,
            [tile_to_add]
        )

    def test_get_in_area(self):
        map = SpatialHashMap()
        tile_to_add = Tile("refined-concrete", 0, 0)
        map.add(tile_to_add)
        other_tile_to_add = Tile("landfill", 10, 0)
        map.add(other_tile_to_add)
        another_tile_to_add = Tile("refined-hazard-concrete-left", 7, 7)
        map.add(another_tile_to_add)
        results = map.get_in_area([[0, 0], [4, 4]])
        self.assertEqual(
            results,
            [tile_to_add]
        )
        results = map.get_in_area([[0, 0], [8, 8]])
        self.assertEqual(
            results,
            [tile_to_add, another_tile_to_add]
        )
        results = map.get_in_area([[-100, -100], [100, 100]])
        self.assertEqual(
            results,
            [tile_to_add, another_tile_to_add, other_tile_to_add]
        )
        results = map.get_in_area([[-100, -100], [100, 100]], limit = 1)
        self.assertEqual(
            results,
            [tile_to_add]
        )