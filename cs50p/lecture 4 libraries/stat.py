from statistics import mean, median, mode
value = []
y = 0
while y < 5 :
    x = int(input("please enter your number :"))
    value.append(x)
    y = y +1


print("mean =",mean(value))
print("median =", median(value))
print("mode =", mode(value))