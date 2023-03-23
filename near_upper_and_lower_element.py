
b = [2,3,4,5,6,8,9,10]
n = 5



# Nearest lower number
lower_number = 0
for i in b:
    if i < n:
        lower_number = i

# Nearest upper number
upper_number = 0
for j in b:
    if j > n:
        upper_number = j
        break

print("The nearest lower number is", lower_number)
print("The nearest upper number is", upper_number)


# Time complexity: O(n)
# Space complexity: O(1)

