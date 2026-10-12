model = {"Room1": None, "Room2": None}
count = {"Room1": 0, "Room2": 0}

def update_model(room, reading):
    model[room] = reading

def temperature_agent(room, reading):
    update_model(room, reading)

    if reading == "Cold":
        count[room] += 1
        return "Turn Heater ON"

    elif reading == "Hot":
        return "Turn Heater OFF"

    elif model["Room1"] == "Normal" and model["Room2"] == "Normal":
        return "All Rooms Comfortable - Idle"

    else:
        return "Move to Other Room to Check"


percept_sequence = [
    ("Room1", "Cold"),
    ("Room1", "Normal"),
    ("Room2", "Hot"),
    ("Room2", "Normal")
]

print("Room Reading Action Model")

for room, reading in percept_sequence:
    action = temperature_agent(room, reading)
    print(room, reading, action, model)

print("Heater ON count:", count)