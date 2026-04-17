print("🔌 Electronics Calculator")

color_codes = {
    "black": 0, "brown": 1, "red": 2, "orange": 3,
    "yellow": 4, "green": 5, "blue": 6,
    "violet": 7, "grey": 8, "white": 9
}

while True:
    print("\n1. Ohm's Law (V = I * R)")
    print("2. Power Calculation (P = V * I)")
    print("3. Resistor Color Code")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        I = float(input("Enter Current (A): "))
        R = float(input("Enter Resistance (Ohm): "))
        print("Voltage =", I * R)

    elif choice == '2':
        V = float(input("Enter Voltage (V): "))
        I = float(input("Enter Current (A): "))
        print("Power =", V * I)

    elif choice == '3':
        print("\nEnter colors (lowercase):")
        c1 = input("1st band: ")
        c2 = input("2nd band: ")
        c3 = input("Multiplier band: ")

        if c1 in color_codes and c2 in color_codes and c3 in color_codes:
            value = (color_codes[c1] * 10 + color_codes[c2]) * (10 ** color_codes[c3])
            print("Resistance =", value, "Ohms")
        else:
            print("Invalid color entered!")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")