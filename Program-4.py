def count_multiples(numbers):
    result = {}

    for i in range(1, 10):
        count = 0
        for num in numbers:
            if num % i == 0:
                count += 1
        result[i] = count

    return result


# ----------- User Input Section -----------
try:
    user_input = input("Enter numbers separated by space: ")
    numbers = list(map(int, user_input.split()))

    output = count_multiples(numbers)

    print("\nOutput:")
    print(output)

except ValueError:
    print("Error: Please enter only integers.")
