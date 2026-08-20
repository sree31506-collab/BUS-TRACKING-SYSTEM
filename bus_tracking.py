class Bus:
    def __init__(self, bus_id, route, stops):
        self.bus_id = bus_id
        self.route = route
        self.stops = stops
        self.current_index = 0

    def current_stop(self):
        return self.stops[self.current_index]

    def next_stop(self):
        if self.current_index < len(self.stops) - 1:
            return self.stops[self.current_index + 1]
        return "Route Completed"

    def move(self):
        if self.current_index < len(self.stops) - 1:
            self.current_index += 1

    def status(self):
        return {
            "Bus ID": self.bus_id,
            "Route": self.route,
            "Current Stop": self.current_stop(),
            "Next Stop": self.next_stop()
        }


def display_bus(bus):
    status = bus.status()

    print("-" * 40)
    print(f"Bus ID       : {status['Bus ID']}")
    print(f"Route        : {status['Route']}")
    print(f"Current Stop : {status['Current Stop']}")
    print(f"Next Stop    : {status['Next Stop']}")
    print("-" * 40)


def main():
    bus1 = Bus(
        "BUS101",
        "Kottapeta - Railway Station",
        ["Kottapeta", "Main Road", "Market", "Railway Station"]
    )

    bus2 = Bus(
        "BUS102",
        "Kottapeta - Bus Stand",
        ["Kottapeta", "College", "Hospital", "Bus Stand"]
    )

    buses = [bus1, bus2]

    print("=" * 40)
    print("       BUS TRACKING SYSTEM")
    print("=" * 40)

    for bus in buses:
        display_bus(bus)

    print("\nUpdating bus locations...\n")

    for bus in buses:
        bus.move()
        display_bus(bus)

    print("Simulation completed successfully.")


if __name__ == "__main__":
    main()
