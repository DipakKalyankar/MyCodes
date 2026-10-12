def process_numbers(numbers):
    total = 0
    count = 0
    largest = 0

    for n in numbers:
        if n >= 0 and n % 2 == 0:
            square = n * n
            total += square
            count += 1

            if square > largest:
                largest = square

    print("Total:", total)
    print("Count:", count)
    print("Largest squared value:", largest)


numbers = [-2, 1, 2, 3, 4, 6, -8]
process_numbers(numbers)
