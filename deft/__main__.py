import time
import argparse
from client import Client
from tweets import sentiment_analysis


def main():
    client = Client()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--run", help="run the program, making real trades", action="store_true"
    )
    parser.add_argument(
        "--test", help="run the program in test mode", action="store_true"
    )

    args = parser.parse_args()

    if args.test:
        print("test")

    if args.run:
        print("run")


if __name__ == "__main__":
    main()
