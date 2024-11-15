import unittest
from robot_movement import Terrain

class TestTerrain(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain(10, 10)

    def test_add_robot(self):
        self.terrain.add_robot(1)
        self.assertEqual(self.terrain.get_robot_location(1), (0, 0))

    def test_move_robot(self):
        self.terrain.add_robot(1)
        self.terrain.move_robot(1, 'E3')
        self.assertEqual(self.terrain.get_robot_location(1), (3, 0))
        self.terrain.move_robot(1, 'S2')
        self.assertEqual(self.terrain.get_robot_location(1), (3, 2))

    def test_multiple_robots_no_collision(self):
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)
        self.terrain.move_robot(1, 'E3')
        self.terrain.move_robot(2, 'S2')
        self.assertEqual(self.terrain.get_robot_location(1), (3, 0))
        self.assertEqual(self.terrain.get_robot_location(2), (0, 2))

    def test_collision(self):
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)
        self.terrain.move_robot(1, 'E3')
        self.terrain.move_robot(2, 'E3')
        self.assertEqual(self.terrain.get_robot_location(1), (3, 0))
        self.assertEqual(self.terrain.get_robot_location(2), (2, 0))

if __name__ == '__main__':
    unittest.main()
