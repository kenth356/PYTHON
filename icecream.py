Price1 = 1.49
Price2 = 2.49
Price3 = 3.49

print("\n=========================================")
print ("\n          The DeLIGHTful Ices      \n")
print("=========================================\n")
print("DeLIGHTful        (1 scoop)          1.49\n")
print("Double DeLIGHT    (2 scoops)         2.49\n")
print("Triple DeLIGHT    (3 scoops)         3.49\n")

numCONES1 = float(input("\nEnter number of single scoop cones sold: "))
numCONES2 = float(input("\nEnter number of double scoop cones sold: "))
numCONES3 = float(input("\nEnter number of triple scoop cones sold: "))

eachSALES1 = numCONES1 * Price1
eachSALES2 = numCONES2 * Price2
eachSALES3 = numCONES3 * Price3

totalCONES = numCONES1 + numCONES2 + numCONES3
totalSALES = eachSALES1 + eachSALES2 + eachSALES3

print("\n" + "=========================================".rjust(75))
print ("\n" + "          The DeLIGHTful Ices Sales       ".rjust(74))
print("\n" + "=========================================".rjust(75))

print(f"\nDeLIGHTful cones{"":>12}{numCONES1:>7}{"$":>7}{eachSALES1:>7.2f}")
print(f"\nDouble DeLIGHT cones{"":>8}{numCONES2:>7}{"$":>7}{eachSALES2:>6.2f}")
print(f"\nTriple DeLIGHT cones{"":>8}{numCONES3:>7}{"$":>7}{eachSALES3:>7.2f}")
print("-" * 49)
print(f"\nTOTAL{"":>23}{totalCONES:>7}{"$":>7}{totalSALES:>7.2f}")