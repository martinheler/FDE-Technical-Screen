# Package Sorting Function

## Objective
This project implements a package sorting function for Thoughtful’s robotic automation factory. The function determines the correct stack for a package based on its dimensions and mass.

## Sorting Rules
Packages are classified into different categories based on the following criteria:

- A package is **bulky** if:
  - Its volume (Width × Height × Length) is **≥ 1,000,000 cm³**.
  - OR any of its dimensions is **≥ 150 cm**.
- A package is **heavy** if its mass is **≥ 20 kg**.

### Stacks:
- **STANDARD**: Packages that are **neither bulky nor heavy**.
- **SPECIAL**: Packages that are **either bulky or heavy** but not both.
- **REJECTED**: Packages that are **both bulky and heavy**.

## Implementation
The function `sort(width, height, length, mass)` determines the classification:

```python
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
```

## Usage
Call the `sort()` function with the package's dimensions (width, height, length) in centimeters and mass in kilograms. The function will return the category where the package should be dispatched, along with the calculated **volume and mass**.

### Example Usage:
```python
print(sort(50, 50, 50, 10))    # Volume: 125000.00 cm³, Mass: 10.00 kg, Category: STANDARD
print(sort(200, 50, 50, 10))   # Volume: 500000.00 cm³, Mass: 10.00 kg, Category: SPECIAL
print(sort(50, 50, 50, 25))    # Volume: 125000.00 cm³, Mass: 25.00 kg, Category: SPECIAL
print(sort(200, 50, 50, 25))   # Volume: 500000.00 cm³, Mass: 25.00 kg, Category: REJECTED
```

## Interactive Mode
The program allows users to select between two modes:
1. **Test Mode (`test`)**: Runs predefined test cases.
2. **Try Mode (`try`)**: Allows users to input package dimensions and mass manually.

### Running the Program:
```sh
python package_sorting.py
```
You will be prompted to enter a mode:
- Enter `test` to see predefined test cases.
- Enter `try` to input custom values.

## Requirements
- Python 3.x

## Testing
To verify the implementation, run the script and choose `test` mode, or run test cases manually:

```python
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
```

## Author
Martin Coronado

