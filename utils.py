import glob
import resource
import time
from typing import Callable, List


def gb_data_files() -> List[str]:
    """
    Get the groupby data in increasing order
    """
    files = glob.glob("data/1*.csv")
    files.sort()
    return files


def peak_memory() -> float:
    """
    Peak memory in GB
    """
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)


def simple_bench(func: Callable, unit: str = "ms", n_runs: int = 3) -> float:
    t0 = time.time()
    for _ in range(n_runs):
        func()
    duration = (time.time() - t0) / n_runs
    if unit == "ms":
        return duration * 1000
    if unit == "s":
        return duration
