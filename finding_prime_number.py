#Take input from user and store this as upper bound
#Goal is to find all the prime numbers below this value

upper_bound = int(input("Enter upper range within which you want prime numbers: "))

# Function to return prime numbers

def prime_num(upper_bound):
    
    number_range = set(range(2, upper_bound+1,)) 
    prime_list = []
    
    while number_range:
        
        prime = number_range.pop() #Will remove and store the current element
        prime_list.append(prime)    #append this number to prime number list
        multiples_of_primes = set(range(prime*2, upper_bound+1, prime)) #remove all multiples of current element
        number_range.difference_update(multiples_of_primes)  #will update the number_range with only those elements in number_range and not in multiples  
     
    print(prime_list)
    
    prime_count = len(prime_list)
    
    largest_prime = max(prime_list)
    
    #Summary
    print(f"There are {prime_count} prime numbers below {upper_bound}, the largest being {largest_prime}")

prime_num(upper_bound)