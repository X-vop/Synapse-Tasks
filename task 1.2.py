gadgets = [
    ("Explosive Batarangs", 3, True),
    ("Batarangs", 5, True),
    ("Smoke Pellets", 0, False),
    ("Tear Gas Grenades", 2, True),
    ("Night Vision Goggles", 1, True),
    ("Batclaw", 0, False),
    ("Grapple Gun", 3, True),
    ("Batsignal", 0, False),
    ("Utility Belt", 1, True),
    ("Batmobile Tires", 4, True)
]

sorted_gadgets = sorted(gadgets, key= lambda x: (-x[1], x[0]))
print(sorted_gadgets)


"""
g2 = [] #for availability
for i in range(0,len(gadgets)):
    if gadgets[i][2]==True:
        g2.insert(0,gadgets[i])
    else:
        g2.append(gadgets[i])
print(g2)
#for quantity priority

for i in range(0,len(g2)-1):
    for j in range(0,len(g2)-i-1):
        if g2[j+1][1]>g2[j][1]:
            temp = g2[j+1]
            g2[j+1]=g2[j]
            g2[j]=temp
print(g2)

"""

