import math

def main():
    print("--- Python Math Library Exploration ---")
    
    # 1. Constants
    print("\n[Constants]")
    print(f"Pi (math.pi): {math.pi}")
    print(f"Euler's number (math.e): {math.e}")
    
    # 2. Power and Logarithmic functions
    print("\n[Power and Logarithmic]")
    print(f"2 to the power of 3 (math.pow(2, 3)): {math.pow(2, 3)}")
    print(f"Square root of 25 (math.sqrt(25)): {math.sqrt(25)}")
    print(f"Natural log of e (math.log(math.e)): {math.log(math.e)}")
    print(f"Base 10 log of 100 (math.log10(100)): {math.log10(100)}")
    
    # 3. Number-theoretic and representation functions (Rounding)
    print("\n[Rounding and Absolute Value]")
    num = 4.7
    neg_num = -5.3
    print(f"Original numbers: {num}, {neg_num}")
    print(f"Ceiling of {num} (math.ceil({num})): {math.ceil(num)}")
    print(f"Floor of {num} (math.floor({num})): {math.floor(num)}")
    print(f"Truncate {num} (math.trunc({num})): {math.trunc(num)}")
    print(f"Absolute value of {neg_num} (math.fabs({neg_num})): {math.fabs(neg_num)}")
    
    # 4. Trigonometric and Angular conversion functions
    print("\n[Trigonometric Functions]")
    degrees = 90
    radians = math.radians(degrees)
    print(f"Convert {degrees} degrees to radians (math.radians): {radians}")
    print(f"Sine of 90 degrees (math.sin(radians)): {math.sin(radians)}")
    print(f"Cosine of 90 degrees (math.cos(radians)): {math.cos(radians):.2f} (Note: floating point precision)")
    
    # 5. Combinatorics
    print("\n[Combinatorics]")
    n = 5
    print(f"Factorial of {n}! (math.factorial({n})): {math.factorial(n)}")
    print(f"Combinations of 5 choose 2 (math.comb(5, 2)): {math.comb(5, 2)}")

if __name__ == "__main__":
    main()
