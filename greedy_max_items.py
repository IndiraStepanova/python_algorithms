n = int(input())
items = []
for i in range(1, n+1):
    if (n - i) > i:
        items.append(i)
        n = n - i
        i+=1
    elif (n - i) <= i:
        items.append(n)
        break


print(len(items))
for item in items:
    print(item, end = ' ')


        
