import os
import argparse
import settings

from lib import create_desktop_entry


def run():
    parser = argparse.ArgumentParser(
        prog=settings.PROGRAM_NAME,
        description=settings.DESCRIPTION,
        epilog=settings.EPILOG,
    )

    subparsers = parser.add_subparsers(
        help="Choose the action you want to perform.", dest="command"
    )

    # Adding entry

    add_parser = subparsers.add_parser("add", help="Add a new desktop entry")
    add_parser.add_argument("-n", "--name", required=True)
    add_parser.add_argument("-p", "--path", required=True)
    add_parser.add_argument("-e", "--exec", required=True)
    add_parser.add_argument("-i", "--icon", required=True)

    # Removing entry

    remove_parser = subparsers.add_parser(
        "remove", help="Remove an existing desktop entry"
    )

    args = parser.parse_args()

    if args.command == "add":
        create_desktop_entry(args.name, args.exec, args.path, args.icon)


if __name__ == "__main__":
    run()
