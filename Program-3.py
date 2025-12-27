def generate_series(a: int):
    if a <= 0:
        return "Error: Input must be a positive integer."

    # If a is even, reduce by 1
    terms = a if a % 2 != 0 else a - 1

    series = []
    for i in range(terms):
        series.append(2 * i + 1)

    return series


# ----------- User Input Section -----------
try:
    a = int(input("Enter the value of a: "))

    result = generate_series(a)

    print("\nOutput:")
    if isinstance(result, list):
        print(", ".join(map(str, result)))
    else:
        print(result)

except ValueError:
    print("Error: Please enter a valid integer.")
