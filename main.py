four_by_four = 30.54
two_by_eight = 41.99
print("1. 4x4 bed\n2. 2x8 bed")
bedType = input("Would you like to make 4x4 or 2x8 beds? (Enter 1/2): ")
x = 0
class Beds:
    def fourbyfouramt(a,b):
        a = b * four_by_four
        return a
    def twobyeightamt(a,b):
        a = b * two_by_eight
        return a
        
b = Beds()

if bedType in ('1','2'):
    bedAmt = int(input("How many garden beds would you like to build? "))
    fbf = b.fourbyfouramt(bedAmt)
    print("The price of what you want to purchase is " + "${:,.2f}". format(fbf))
        
else:
    print("Invalid input")
