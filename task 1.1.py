Kevin = {"Halsey", "Taylor Swift","Mitski","Joji","Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj" , "Conan Gray", "One Direction", "Justin Bieber"}
Stuart= {"Kendrick Lamar", "Steve Lacey" , "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay" , "Kanye West" , "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron" , "Mitski", "Arctic Monkeys", "Steve Lacey", "Kendrick Lamar" , "Isabel LaRosa" , "Shawn Mendes", "Coldplay"}
Edith = {"Metallica" , "Billie Eilish", "TheWeeknd", "Mitski","NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West" , "Coldplay"}

DJs = Kevin, Stuart, Bob, Edith
DJ = "Kevin", "Stuart", "Bob", "Edith"
from itertools import combinations
comb = list(combinations(DJ,2))
combs = list(combinations(DJs,2)) #print(f"{comb} are the total possible combinations")

count=0
DJ_final=[]
overlap=[]
for i in range(0,len(combs)):
    a=combs[i][0].intersection(combs[i][1])
    #print(a)
    if len(a) >=3:
        count +=1
        #print(comb[i])
        DJ_final.append(comb[i])
        #print(len(a)*10)
        overlap.append(len(a)*10)
final = zip(DJ_final,overlap)
final= sorted(final,key = lambda x: -x[1])
print(dict(final))


