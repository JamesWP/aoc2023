import contextlib

@contextlib.contextmanager
def input(day):
    with open(f"input/day{day}.txt", "r") as inp:
        yield inp


def lines(day):
    with input(day) as inp:
        for line in inp:
            yield line.strip()

def blocks_of_lines(day):
    with input(day) as inp:
        for part in inp.read().split("\n\n"):
            yield part.split("\n")