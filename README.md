# Parking Garage Simulation

An implementation example of the popular programming interview question: "Design a parking garage system."
This project simulates a parking garage system that allows cars to enter, exit, and pay for parking. The simulation runs with random operations over a given time frame.

## Features

- Define a parking garage with a set capacity.
- Allow cars to enter with a randomly generated Swiss-style license plate.
- Track the number of occupied and free spaces.
- Enable cars to exit after payment.
- Print the current state of the garage.

## Usage

The script automatically simulates the behavior of a parking garage:

- Cars enter if there is space.
- Cars exit after making a payment.
- The garage updates its availability dynamically.

### Example Output

```
Entering: ZH123456 at 2025-02-01 14:30:00
Car with plate ZH123456 paid for 0.50 hours.
Car with plate ZH123456 leaves the garage.
Capacity: 140
Taken: 5
Free: 135
Open: True
```

## Classes

### `ParkingGarage`
Represents the parking garage with the following methods:
- `enter(plate)`: Adds a car to the garage if space is available.
- `exit(plate)`: Removes a car from the garage after payment.
- `print_state()`: Displays the garage status.
- `calc_free()`: Updates available spaces.

### `Car`
Represents a parked car with properties:
- `plate`: License plate number.
- `entry_time`: Timestamp of when the car entered.
- `parking_time`: Duration parked.
- `paid`: Payment status.
- `pay(time)`: Processes payment based on parking duration.

## License

This project is open-source and available under the MIT License.

