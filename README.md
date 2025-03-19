# DeskEntry

**DeskEntry** is a simple command-line tool for creating and managing desktop entries on Linux. Easily create or remove application entries with a single command.

## Features
- Add new desktop entries with a custom name and icon.
- Remove existing desktop entries.

## Installation
Clone the repository and navigate to the project folder:
```sh
git clone https://github.com/ubaidrmn/DeskEntry.git
cd DeskEntry
```

## Usage
Run the script using Python:
```sh
python3 cli.py <command> [options]
```

## Add a Desktop Entry
```sh
python3 cli.py add --name "MyApp" --icon /path/to/icon.png --exec /path/to/executable --path /path/to/working/directory
```
