#  Check if a number is a prime number.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False  # Any even number other than 2 is not a prime
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Find all prime numbers up to a given limit.

def find_primes_up_to(limit):
    primes = []
    for num in range(1, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Save the list of prime numbers to a file.

def save_primes_to_file(primes, filename):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(f"{prime}\n")

if __name__ == "__main__":
    # Store all prime numbers between 1 to 250 in results.txt
    primes_250 = find_primes_up_to(250)
    save_primes_to_file(primes_250, "results.txt")
    print(f"Prime numbers between 1 and 250 have been saved to results.txt")

    # Store all prime numbers between 1 to 2500 in results2500.txt
    primes_2500 = find_primes_up_to(2500)
    save_primes_to_file(primes_2500, "results2500.txt")
    print(f"Prime numbers between 1 and 2500 have been saved to results2500.txt")

    # Display and store all prime numbers between 1 to 250000 in results250000.txt
    primes_250000 = find_primes_up_to(250000)
    save_primes_to_file(primes_250000, "results250000.txt")
    print(f"Prime numbers between 1 and 250000 have been saved to results250000.txt")

