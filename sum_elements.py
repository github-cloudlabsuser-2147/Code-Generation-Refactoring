MAX = 100

def calculate_sum(arr: list[int]) -> int:
    """Calculate the sum of a list of integers."""
    return sum(arr)

def get_number_of_elements() -> int:
    """Prompt the user to enter the number of elements within a valid range."""
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX}): "))
            if 1 <= n <= MAX:
                return n
            print(f"Invalid input. Please provide a number ranging from 1 to {MAX}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n: int) -> list[int]:
    """Prompt the user to enter `n` integers."""
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        while True:
            try:
                arr.append(int(input()))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return arr

def main() -> None:
    """Main function to execute the program."""
    try:
        n = get_number_of_elements()
        arr = get_elements(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)

if __name__ == "__main__":
    main()
