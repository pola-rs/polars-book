import os

DATA_DIR = "data"
EXAMPLE_BASE_DIR = "user_guide/src/examples"
OUTPUT_BASE_DIR = "user_guide/src/outputs"


def create_if_not_exists(path: str) -> str:
    """Create path if it does not exists. Return the path regardless."""

    if not os.path.exists(path):
        os.makedirs(path)

    return path
