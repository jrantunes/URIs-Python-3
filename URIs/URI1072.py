#Interval 2

in_interval = []
out_interval = []

for i in range(int(input())):
    x = int(input())
    if x in range(10, 21):
        in_interval.append(x)
    else:
        out_interval.append(x)
print("{} in\n{} out".format(len(in_interval), len(out_interval)))
