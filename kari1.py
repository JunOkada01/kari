a = 1
b = 5
for i in range(5):
    a = a + 2
    a = a + a
    a = b
    c = a + b
    print("✕"+ a)
print(a,c)

for g in range(10):
    a = b + a
print(a,b)