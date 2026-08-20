# 🚌 Bus Tracking System

## Description

The Bus Tracking System is a Python-based simulation project designed to track
the movement of buses along predefined routes. It displays the bus ID, route,
current stop, and next stop.

## Features

- Track multiple buses
- Display current bus location
- Display next bus stop
- Simulate bus movement
- Automated testbench using Python unittest
- Console-based simulation output

## Technologies Used

- Python 3
- Object-Oriented Programming
- Python unittest

## Project Structure

Bus-Tracking-System/
│
├── README.md
├── bus_tracking.py
├── test_bus_tracking.py
├── simulation_output.txt
└── requirements.txt

## How to Run

### Step 1: Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

### Step 2: Open the project folder

cd Bus-Tracking-System

### Step 3: Run the bus tracking simulation

python bus_tracking.py

### Step 4: Run the testbench

python -m unittest test_bus_tracking.py

## Expected Result

The program displays the bus ID, route, current stop, and next stop.
The simulation then moves each bus to its next stop.

## Testing

The testbench verifies:

1. Bus ID
2. Current bus stop
3. Next bus stop
4. Bus movement
5. Route completion

## Future Improvements

- GPS-based real-time tracking
- Interactive map integration
- Estimated time of arrival (ETA)
- Web/mobile application
- Database integration
- Live passenger notifications

## Author

Your Name
