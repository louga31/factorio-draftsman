# test_electric_pole.py
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from draftsman.classes.blueprint import Blueprint
from draftsman.classes.group import Group
from draftsman.entity import ElectricPole, electric_poles
from draftsman.error import InvalidEntityError
from draftsman.warning import DraftsmanWarning

import sys
import pytest

if sys.version_info >= (3, 3):  # pragma: no coverage
    import unittest
else:  # pragma: no coverage
    import unittest2 as unittest


class ElectricPoleTesting(unittest.TestCase):
    def test_constructor_init(self):
        electric_pole = ElectricPole("substation", position=[1, 1], neighbours=[1, 2])

        # Warnings
        with pytest.warns(DraftsmanWarning):
            ElectricPole("small-electric-pole", unused_keyword=10)

        # Errors
        with pytest.raises(InvalidEntityError):
            ElectricPole("this is not an electric pole")

    def test_mergable_with(self):
        group = Group()
        group.entities.append("small-electric-pole")
        group.entities.append("small-electric-pole", tile_position=(5, 0))
        group.add_power_connection(0, 1)
        group.add_circuit_connection("red", 0, 1)
        group.add_circuit_connection("green", 0, 1)

        blueprint = Blueprint()
        blueprint.entities.append(group)
        group.position = (5, 0)

        group1_entity = blueprint.entities[(0, 1)]
        group2_entity = group.entities[0]

        assert group1_entity.mergable_with(group2_entity)
        assert group2_entity.mergable_with(group1_entity)

        group.position = (5, 5)
        assert not group1_entity.mergable_with(group2_entity)

        group2_entity = ElectricPole("medium-electric-pole", tile_position=(5, 0))
        assert not group1_entity.mergable_with(group2_entity)

    def test_merge(self):
        group = Group()
        group.entities.append("small-electric-pole")
        group.entities.append("small-electric-pole", tile_position=(2, 0))
        group.add_power_connection(0, 1)
        group.add_circuit_connection("red", 0, 1)
        group.add_circuit_connection("green", 0, 1)

        blueprint = Blueprint()
        blueprint.entities.append(group)
        group.position = (2, 0)
        blueprint.entities.append(group, merge=True)
        blueprint.add_power_connection((0, 0), (1, 0))

        self.maxDiff = None
        assert len(blueprint.entities) == 2
        assert len(blueprint.entities[0].entities) == 2
        assert len(blueprint.entities[1].entities) == 1
        assert blueprint.to_dict()["blueprint"]["entities"] == [
            {
                "entity_number": 1,
                "name": "small-electric-pole",
                "position": {"x": 0.5, "y": 0.5},
                "neighbours": [2, 3],
                "connections": {
                    "1": {"red": [{"entity_id": 2}], "green": [{"entity_id": 2}]}
                },
            },
            {
                "entity_number": 2,
                "name": "small-electric-pole",
                "position": {"x": 2.5, "y": 0.5},
                "neighbours": [1, 3],
                "connections": {
                    "1": {
                        "red": [{"entity_id": 1}, {"entity_id": 3}],
                        "green": [{"entity_id": 1}, {"entity_id": 3}],
                    }
                },
            },
            {
                "entity_number": 3,
                "name": "small-electric-pole",
                "position": {"x": 4.5, "y": 0.5},
                "neighbours": [2, 1],
                "connections": {
                    "1": {"red": [{"entity_id": 2}], "green": [{"entity_id": 2}]}
                },
            },
        ]

        # Exceeding max number of neighbours
        group = Group("triangle")
        group.entities.append("small-electric-pole")
        for i in range(5):
            group.entities.append("small-electric-pole", tile_position=(-2, i - 2))
            group.add_power_connection(0, -1)

        group2 = Group("line")
        group2.entities.append("small-electric-pole")
        group2.entities.append("small-electric-pole", tile_position=(2, 0))
        group2.entities.append("small-electric-pole", tile_position=(4, 0))
        group2.add_power_connection(0, 1)
        group2.add_power_connection(1, 2)

        blueprint = Blueprint()
        blueprint.entities.append(group)
        blueprint.entities.append(group2, merge=True)
        blueprint.add_power_connection((0, 3), (1, 0))

        assert len(blueprint.entities) == 2
        assert len(blueprint.entities[0].entities) == 6
        assert len(blueprint.entities[1].entities) == 2
        assert blueprint.to_dict()["blueprint"]["entities"] == [
            {
                "entity_number": 1,
                "name": "small-electric-pole",
                "position": {"x": 0.5, "y": 0.5},
                "neighbours": [2, 3, 4, 5, 6],
            },
            {
                "entity_number": 2,
                "name": "small-electric-pole",
                "position": {"x": -1.5, "y": -1.5},
                "neighbours": [1],
            },
            {
                "entity_number": 3,
                "name": "small-electric-pole",
                "position": {"x": -1.5, "y": -0.5},
                "neighbours": [1],
            },
            {
                "entity_number": 4,
                "name": "small-electric-pole",
                "position": {"x": -1.5, "y": 0.5},
                "neighbours": [1, 7],
            },
            {
                "entity_number": 5,
                "name": "small-electric-pole",
                "position": {"x": -1.5, "y": 1.5},
                "neighbours": [1],
            },
            {
                "entity_number": 6,
                "name": "small-electric-pole",
                "position": {"x": -1.5, "y": 2.5},
                "neighbours": [1],
            },
            {
                "entity_number": 7,
                "name": "small-electric-pole",
                "position": {"x": 2.5, "y": 0.5},
                "neighbours": [8, 4],
            },
            {
                "entity_number": 8,
                "name": "small-electric-pole",
                "position": {"x": 4.5, "y": 0.5},
                "neighbours": [7],
            },
        ]

        group = Group()
        group.entities.append("small-electric-pole")
        group.entities.append("small-electric-pole", tile_position=(2, 0))
        group.add_power_connection(0, 1)
        group.add_circuit_connection("red", 0, 1)

        blueprint = Blueprint()
        blueprint.entities.append(group)
        blueprint.entities.append(group, merge=True)

        assert len(blueprint.entities) == 2
        assert len(blueprint.entities[0].entities) == 2
        assert len(blueprint.entities[1].entities) == 0
        assert blueprint.to_dict()["blueprint"]["entities"] == [
            {
                "entity_number": 1,
                "name": "small-electric-pole",
                "position": {"x": 0.5, "y": 0.5},
                "neighbours": [2],
                "connections": {"1": {"red": [{"entity_id": 2}]}},
            },
            {
                "entity_number": 2,
                "name": "small-electric-pole",
                "position": {"x": 2.5, "y": 0.5},
                "neighbours": [1],
                "connections": {"1": {"red": [{"entity_id": 1}]}},
            },
        ]

        # Test wire connections
        group = Group()
        group.entities.append("small-electric-pole")
        group.entities.append("small-electric-pole", tile_position=(2, 0))
        group.add_circuit_connection("red", 0, 1)

        blueprint = Blueprint()
        blueprint.entities.append("small-electric-pole")
        blueprint.entities.append(group, merge=True)

        assert len(blueprint.entities) == 2
        assert len(blueprint.entities[1].entities) == 1
        assert blueprint.to_dict()["blueprint"]["entities"] == [
            {
                "entity_number": 1,
                "name": "small-electric-pole",
                "position": {"x": 0.5, "y": 0.5},
                "connections": {"1": {"red": [{"entity_id": 2}]}},
            },
            {
                "entity_number": 2,
                "name": "small-electric-pole",
                "position": {"x": 2.5, "y": 0.5},
                "connections": {"1": {"red": [{"entity_id": 1}]}},
            },
        ]
