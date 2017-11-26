from multiprocessing import Pool, cpu_count
import time

def parallelize(f, sequence):
    pool = Pool(processes=cpu_count())
    result = pool.map(f, sequence)
    cleaned = [x for x in result if not x is None]
    cleaned = list(cleaned)

    pool.close()
    pool.join()

    return cleaned