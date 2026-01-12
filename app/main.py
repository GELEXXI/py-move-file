from os import remove, rename, makedirs, path


def move_file(command: str) -> None:
    command_path = command.split()
    if len(command_path) != 3 or "mv" not in command_path:
        return
    if "/" not in command_path[2]:
        rename(command_path[1], command_path[2])
        return

    directory = path.dirname(command_path[2])

    if directory:
        makedirs(directory, exist_ok=True)

    source_file, destination_file = command_path[1], command_path[2]

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        remove(source_file)
    except Exception:
        pass
