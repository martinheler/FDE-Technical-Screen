def sort(width: float, height: float,length: float, mass: float):
    volume = (width*height*length)
    
    isbulky = volume >= 1_000_000 or max(width, height, length) >= 150
    isheavy = mass >= 20

    if (isbulky and isheavy):
        return "REJECTED"
    elif(isbulky or isheavy):
        return "SPECIAL"
    else:
        return "STANDARD"

if __name__ == "__main__":
    print("Package Sorting System (Metric Units)")
    print("Select mode: \"test\" to run test cases, \"try\" to input values manually")
    mode = input("Enter mode: ").strip().lower()
    
    if mode == "test":
        test_cases = [
            (50, 50, 50, 10),    # STANDARD
            (200, 50, 50, 10),   # SPECIAL (bulky)
            (50, 50, 50, 25),    # SPECIAL (heavy)
            (200, 50, 50, 25),   # REJECTED (bulky & heavy)
            (149, 149, 149, 19), # STANDARD
            (150, 100, 100, 10), # SPECIAL (bulky)
            (100, 100, 100, 20), # SPECIAL (heavy)
            (150, 100, 100, 20)  # REJECTED (bulky & heavy)
        ]
        
        for w, h, l, m in test_cases:
            print(f"sort({w}, {h}, {l}, {m}) -> {sort(w, h, l, m)}")
    elif mode == "try":
        try:
            width = float(input("Enter width (cm): "))
            height = float(input("Enter height (cm): "))
            length = float(input("Enter length (cm): "))
            mass = float(input("Enter mass (kg): "))
            print(sort(width, height, length, mass))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
    else:
        print("Invalid mode selected.")
