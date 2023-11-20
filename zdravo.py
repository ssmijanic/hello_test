def factorial(n):
    if n == 0:
    	return 1
    else:
    	return n * factorial(n-1)
    
broj = 5
rezultat= factorial(broj)
print(f"Faktorijal broja {broj} je {rezultat}.")
    
