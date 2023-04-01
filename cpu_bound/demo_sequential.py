from tqdm import tqdm

from cpu_bound.common import NUMBERS, is_prime_slow, timeit


@timeit
def check_some_numbers_are_prime():
    for number in tqdm(NUMBERS):
        result = is_prime_slow(number)


check_some_numbers_are_prime()
