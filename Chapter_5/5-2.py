"""
Given a real number between 0 and 1 (e.g., 0.72) that is passed 
in as a double, print the binary representation. If the number 
cannot be represented accurately in binary with at most 32 
characters, print "ERROR"

"""

def binToString(num):
    if num <= 0 or num >= 1:
        return "ERROR"

    bin = "0."
    while num > 0:
        if len(bin) >= 32:
            return "ERROR"

        r = num * 2
        if r >= 1:
            bin += '1'
            num = r - 1
        else:
            bin += '0'
            num = r

    return bin

def binToString2(num):
    if num <= 0 or num >= 1:
        return "ERROR"

    bin = "0."
    frac = 0.5
    while num > 0:
        if len(bin) >= 32:
            return "ERROR"

        if num >= frac:
            bin += '1'
            num -=  frac
        else:
            bin += '0'

        frac /= 2

    return bin

if __name__ == "__main__":
    print ( binToString ( 0.3 ) )
    print ( binToString ( 0.75 ) )
    print ( binToString ( 0.625 ) )

    print ( binToString2 ( 0.3 ) )
    print ( binToString2 ( 0.75 ) )
    print ( binToString2 ( 0.625 ) )