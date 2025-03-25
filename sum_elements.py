from typing import List

# Constants
MAX_ELEMENTS = 100
MIN_ELEMENTS = 1

def get_valid_number_of_elements() -> int:
    """Get and validate the number of elements from user input."""
    try:
        n = int(input(f"Enter the number of elements ({MIN_ELEMENTS}-{MAX_ELEMENTS}): "))
        if not MIN_ELEMENTS <= n <= MAX_ELEMENTS:
            raise ValueError(f"Number must be between {MIN_ELEMENTS} and {MAX_ELEMENTS}")
        return n
    except ValueError as e:
        raise ValueError("Please enter a valid integer.") from e

def get_numbers(count: int) -> List[int]:
    """Get specified number of integers from user input."""
    numbers = []
    print(f"Enter {count} integers:")
    for i in range(count):
        try:
            number = int(input(f"Number {i + 1}: "))
            numbers.append(number)
        except ValueError:
            raise ValueError("Please enter valid integers.")
    return numbers

def calculate_sum(numbers: List[int]) -> int:
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def main() -> None:
    """Main program execution."""
    try:
        # Get number of elements
        n = get_valid_number_of_elements()
        
        # Get the numbers
        numbers = get_numbers(n)
        
        # Calculate and display sum
        total = calculate_sum(numbers)
        print(f"\nSum of the numbers: {total}")
        
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
