def generate_odd_series(a: int):
    if a <= 0:
        return "Error: Input must be a positive integer."

    series = []
    for i in range(1, a + 1):
        series.append(2 * i - 1)

    return series

# ----------- User Input Section -----------
try:
    a = int(input("Enter the value of a: "))

    result = generate_odd_series(a)

    print("\nOutput:")
    if isinstance(result, list):
        print(", ".join(map(str, result)))
    else:
        print(result)

except ValueError:
    print("Error: Please enter a valid integer.")
