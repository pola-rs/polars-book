from multiprocessing import get_context


def my_fun(s):
    print(s)


with get_context("spawn").Pool() as pool:
    pool.map(my_fun, ["input1", "input2", ...])
