import argparse

def parse_args(arguments):
    parser = argparse.ArgumentParser()
    for argument,crit in arguments.items():
        parser.add_argument(f"--{argument}", default=crit)
    return parser.parse_args()


