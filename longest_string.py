a = "Hey Gaurav what your problematic"

b = a.split()

longest_str = ""


for i in b:
    if len(i) > len(longest_str):
        longest_str = i
print(longest_str)


# Time complexity: O(n)
# Space complexity: O(1)