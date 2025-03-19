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
def sort(width: float, height: float, length: float, mass: float):
    volume = width * height * length
    
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
```

## Usage
Call the `sort()` function with the package's dimensions (width, height, length) in centimeters and mass in kilograms. The function will return the category where the package should be dispatched.

### Example Usage:
```python
print(sort(50, 50, 50, 10))    # STANDARD
print(sort(200, 50, 50, 10))   # SPECIAL (bulky)
print(sort(50, 50, 50, 25))    # SPECIAL (heavy)
print(sort(200, 50, 50, 25))   # REJECTED (bulky & heavy)
```

## Requirements
- Python 3.x

## Testing
To verify the implementation, you can run the following test cases:

```python
if __name__ == "__main__":
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
```


## Author
Martin Coronado

