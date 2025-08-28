
farms = []


farmlist = input()
days = int(input())

for farm in farmlist.split(' '):
    print(farm)
    farms.append(int(farm))
    
farms = sorted(farms)

total = 0

for i in range(days):
    total += farms[-1]
    farms.pop()
print(farms)
print(total)

