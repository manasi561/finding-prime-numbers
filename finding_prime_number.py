# Select upper bound

def prime_num(upper_bound):
    
    number_range = set(range(2, upper_bound+1,))
    prime_list = []
    
    while number_range:
        
        prime = number_range.pop()
        prime_list.append(prime)
        multiples_of_primes = set(range(prime*2, upper_bound+1, prime))
        number_range.difference_update(multiples_of_primes)
    
    print(prime_list)
    
    prime_count = len(prime_list)
    
    largest_prime = max(prime_list)
    
    #Summary
    print(f"There are {prime_count} prime numbers below {upper_bound}, the largest being {largest_prime}")

upper_bound = int(input("Enter upper range within which you want prime numbers: "))

prime_num(upper_bound)