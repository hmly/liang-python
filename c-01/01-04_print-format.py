MAX = 4

print("%-10s %-10s %-10s" % ("a", "a^2", "a^3"))
for i in range(MAX):
    print("%-10d %-10d %-10d" % (i, i*i, i**3))
