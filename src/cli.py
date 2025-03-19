import os
import argparse
import settings

def run():
    parser = argparse.ArgumentParser(
        prog=settings.PROGRAM_NAME,
        description=settings.DESCRIPTION,
        epilog=settings.EPILOG
    )

    parser.add_argument("add")
    
    args = parser.parse_args()
    print(args.add)

if __name__ == "__main__":
    run()
