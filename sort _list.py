n = [1,7,22,5,46,20,2,3]
c = []
for i in range(len(n)):
    m = n[0]
    for j in n:
        if j < m:
            m = j
    c.append(m)
    n.remove(m)
print(c)


#Time complexity - 0(n2)
#space complxity - 0(n)










    