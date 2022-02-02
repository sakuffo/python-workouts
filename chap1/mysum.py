def mysum(*numbers):
    output = 0
    for num in numbers:
        output += num

    return output


print(mysum(1, 2, 34, 5, 6))
print(mysum(1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2))
