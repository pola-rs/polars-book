from .example1 import create_dataset, test_sub_process
import multiprocessing


def main():
    test_df = create_dataset()

    for i in range(0, 5):
        proc = multiprocessing.get_context("fork").Process(target=test_sub_process, args=(test_df, i))
        proc.start()
        proc.join()

        print(f"Executed sub process {i}")


if __name__ == "__main__":
    main()
