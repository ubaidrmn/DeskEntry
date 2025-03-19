import os
import argparse
import settings

from lib import *


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
    add_parser.add_argument("-n", "--name", required=True, help="Program name.")
    add_parser.add_argument(
        "-p",
        "--path",
        required=True,
        help="Working directory where the program will run.",
    )
    add_parser.add_argument(
        "-e",
        "--exec",
        required=True,
        help="Full path to the executable.",
    )
    add_parser.add_argument(
        "-i", "--icon", required=True, help="Full path to the icon."
    )

    # Removing entry

    remove_parser = subparsers.add_parser(
        "remove", help="Remove an existing desktop entry"
    )
    remove_parser.add_argument(
        "-f",
        "--file-name",
        required=True,
        help="Name of the desktop entry you want to remove. This is not the program name, "
        "instead the actual file name of the desktop entry ending with `.desktop`. "
        "You can see all available names using the list command.",
    )

    # Listing entries

    list_parser = subparsers.add_parser(
        "list", help="List all existing desktop entries"
    )
    list_parser.add_argument("-s", "--starts-with", required=False)

    args = parser.parse_args()

    if args.command == "add":
        create_desktop_entry(args.name, args.exec, args.path, args.icon)
    elif args.command == "remove":
        remove_desktop_entry(args.file_name)
    elif args.command == "list":
        starts_with = args.starts_with if args.starts_with else ""
        list_all_entries(starts_with=starts_with)


if __name__ == "__main__":
    run()
