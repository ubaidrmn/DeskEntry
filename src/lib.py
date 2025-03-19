import typing
import os
import settings


class PrintLog:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def success(self, message: str):
        print(f"{self.OKGREEN}{message}")

    def error(self, message: str):
        raise Exception(f"{self.FAIL}{message}")

    def warning(self, message: str):
        print(f"{self.WARNING}{message}")

    def cyan(self, message: str):
        print(f"{self.OKCYAN}{message}")


def create_desktop_entry(
    name: str,
    exec: str,
    path: str,
    icon: str,
    entry_filename: str = "",
    version: str = "1.0",
    terminal: bool = False,
    type: str = "Application",
    categories: typing.List[str] = ["Utility"],
):
    log = PrintLog()

    if entry_filename == "":
        entry_filename = f"{name.replace(" ", "_").lower()}.desktop"
        log.warning(
            f"No filename provided, generated from program name: {entry_filename}"
        )

    if entry_filename in os.listdir(settings.DESKTOP_ENTRY_LOCATION):
        log.error(f"An entry with the same file name already exists: {entry_filename}")

    terminal = "true" if terminal else "false"

    entry = f"""[Desktop Entry]
    Version={version}
    Name={name}
    Exec={exec}
    Path={path}
    Icon={icon}
    Terminal={terminal}
    Type={type}
    Categories={create_categories_string(categories)}
    """

    with open(os.path.join(settings.DESKTOP_ENTRY_LOCATION, entry_filename), "w") as f:
        f.write(entry)

    log.success("Desktop entry created successfully!")


def create_categories_string(categories: typing.List[str]):
    categories_string = ";".join(categories)
    return categories_string


def list_all_entries(starts_with: str = ""):
    log = PrintLog()

    entries = os.listdir(settings.DESKTOP_ENTRY_LOCATION)

    for entry in entries:
        if entry.startswith(starts_with):
            log.cyan(entry)


def remove_desktop_entry(filename: str):
    log = PrintLog()

    os.remove(os.path.join(settings.DESKTOP_ENTRY_LOCATION, filename))

    log.success(f"Desktop entry {filename} removed successfuly!")
