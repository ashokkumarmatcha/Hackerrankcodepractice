n = int(input())
arr = map(int, input().split())
z = sorted(list(set(arr)))

print(z[-2])
print(z[-1])


