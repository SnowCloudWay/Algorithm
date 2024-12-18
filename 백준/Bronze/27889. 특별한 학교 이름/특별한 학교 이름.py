import sys
input = sys.stdin.readline

name = input().strip()

if name == "NLCS":
    sys.stdout.write("North London Collegiate School")
elif name == "BHA":
    sys.stdout.write("Branksome Hall Asia")
elif name == "KIS":
    sys.stdout.write("Korea International School")
elif name == "SJA":
    sys.stdout.write("St. Johnsbury Academy")