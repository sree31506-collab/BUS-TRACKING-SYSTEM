import unittest
from bus_tracking import Bus


class TestBusTracking(unittest.TestCase):

    def setUp(self):
        self.bus = Bus(
            "BUS101",
            "Kottapeta - Railway Station",
            ["Kottapeta", "Main Road", "Market", "Railway Station"]
        )

    def test_bus_id(self):
        self.assertEqual(self.bus.bus_id, "BUS101")

    def test_current_stop(self):
        self.assertEqual(self.bus.current_stop(), "Kottapeta")

    def test_next_stop(self):
        self.assertEqual(self.bus.next_stop(), "Main Road")

    def test_bus_movement(self):
        self.bus.move()
        self.assertEqual(self.bus.current_stop(), "Main Road")

    def test_route_completion(self):
        for _ in range(3):
            self.bus.move()

        self.assertEqual(self.bus.current_stop(), "Railway Station")
        self.assertEqual(self.bus.next_stop(), "Route Completed")


if __name__ == "__main__":
    unittest.main()
