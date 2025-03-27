from typing import List

# Constants
MAX_ELEMENTS = 100
MIN_ELEMENTS = 1

def get_valid_number_of_elements() -> int:
    """Prompt the user to enter a valid number of elements."""
    while True:
        try:
            n = int(input(f"Enter the number of elements ({MIN_ELEMENTS}-{MAX_ELEMENTS}): "))
            if MIN_ELEMENTS <= n <= MAX_ELEMENTS:
                return n
            print(f"Number must be between {MIN_ELEMENTS} and {MAX_ELEMENTS}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_numbers(count: int) -> List[int]:
    """Prompt the user to enter a list of integers."""
    numbers = []
    print(f"Enter {count} integers:")
    for i in range(count):
        while True:
            try:
                number = int(input(f"Number {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return numbers

def calculate_sum(numbers: List[int]) -> int:
    """Calculate and return the sum of a list of numbers."""
    return sum(numbers)

def main() -> None:
    """Main program execution."""
    try:
        # Get the number of elements
        n = get_valid_number_of_elements()
        
        # Get the numbers
        numbers = get_numbers(n)
        
        # Calculate and display the sum
        total = calculate_sum(numbers)
        print(f"\nSum of the numbers: {total}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
