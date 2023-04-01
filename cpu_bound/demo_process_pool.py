from concurrent import futures

from tqdm import tqdm

from cpu_bound.common import NUMBERS, is_prime_slow, timeit


@timeit
def find_primes_with_map() -> None:
    with futures.ProcessPoolExecutor(max_workers=8) as executor:
        result = executor.map(is_prime_slow, tqdm(NUMBERS))


# %%
@timeit
def find_primes_with_submit() -> None:
    results = []
    with futures.ProcessPoolExecutor(max_workers=8) as executor:
        tasks = [executor.submit(is_prime_slow, number) for number in NUMBERS]

        for future in tqdm(futures.as_completed(tasks), total=len(NUMBERS)):
            results.append(future.result())


find_primes_with_submit()
