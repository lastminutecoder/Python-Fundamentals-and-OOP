light = input("Light Color: ")

result = "stop" if light == "red" else "look" if light == "yellow" else "go" if light == "green" else "Light is broken"

print(result)