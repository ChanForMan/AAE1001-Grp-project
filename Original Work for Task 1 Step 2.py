# Define the planes and their costs
planes = {
    'A321neo': {
        'fuel_consumption_rate': 54,  # kg/min
        'time_cost': 10,  # $/min
        'fixed_cost': 1800,  # $
    },
    'A330-900neo': {
        'fuel_consumption_rate': 84,  # kg/min
        'time_cost': 15,  # $/min
        'fixed_cost': 2000,  # $
    },
    'A350-900': {
        'fuel_consumption_rate': 90,  # kg/min
        'time_cost': 20,  # $/min
        'fixed_cost': 2500,  # $
    }
}

# Define the number of flights for each plane
def calculate_cost(plane, flights):
    fuel_cost_per_kg = 0.8  # $/kg
    flight_time = 120  # min
    cost_per_flight = (
        fuel_cost_per_kg * plane['fuel_consumption_rate'] * flight_time +
        plane['time_cost'] * flight_time +
        plane['fixed_cost']
    )
    total_cost = cost_per_flight * flights
    return total_cost

# Input the number of flights for each plane
a321_flights = int(input("Enter the number of A321neo flights: "))
a330_flights = int(input("Enter the number of A330-900neo flights: "))
a350_flights = int(input("Enter the number of A350-900 flights: "))

# Calculate the cost for each plane
cost_a321 = calculate_cost(planes['A321neo'], a321_flights)
cost_a330 = calculate_cost(planes['A330-900neo'], a330_flights)
cost_a350 = calculate_cost(planes['A350-900'], a350_flights)

# Store the costs in a dictionary
costs = {
    'A321neo': cost_a321,
    'A330-900neo': cost_a330,
    'A350-900': cost_a350
}

# Find the plane with the lowest cost
lowest_cost_plane = min(costs, key=costs.get)
lowest_cost = costs[lowest_cost_plane]

print(f"The lowest cost is for {lowest_cost_plane} with a total cost of ${lowest_cost}")
