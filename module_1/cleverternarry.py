light = input("Light Color: ")

action = "stop" if light == "red" else "look" if light == "yellow" else "go" if light == "green" else "Light is broken"

print(action)