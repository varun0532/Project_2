def print_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

# Example usage:
print_triangle(5)