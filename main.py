import time

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def main():
    numbers = []
    while True:
        try:
            num = int(input("Enter an integer (or 0 to exit): "))
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Please enter an integer")

    if numbers:
        max_digit_sum = max(digit_sum(num) for num in numbers)
        max_numbers = [num for num in numbers if digit_sum(num) == max_digit_sum]
        print(
            f"Numbers with maximum sum of digits: {', '.join(map(str, max_numbers))} (sum of digits: {max_digit_sum})")
    else:
        print("No integers were entered")

    time.sleep(3)

if __name__ == "__main__":
    main()
