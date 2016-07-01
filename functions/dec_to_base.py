# Convert a decimal to limited bases
# 1 - Decimal
# 2 - Binary
# 8 - Octal

def decToBase(dec, base):
    val = "0123456789ABCDEF"
    if dec < base:
        return val[dec]
    else:
        return decToBase(dec//base, base) + val[dec % base]

