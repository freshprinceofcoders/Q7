def is_prime(previous_primes, primte_candidate):
    for previous_prime in previous_primes:
        if primte_candidate < previous_prime:
            return False
        if primte_candidate %  previous_prime == 0:
            return False

    return True



primes = []
primte_candidate = 2
counter = 0
primes.append(2)
while len(primes) < 10001:
    primte_candidate += 1
    if is_prime(primes, primte_candidate):
        primes.append(primte_candidate)

print(primes[len(primes) -1])
