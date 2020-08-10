from core.helper_core._core import notify


def create_file(file: str):
    """
    Creates A New file if a file is on the given path if exists asks for overwrite permission
    if yes clears file data then closes it if no asks for another file path

    Arguments:
        file (str) : Path to File to create if exists asks for overwriting permission

    Returns A Path if file created returns file path if not returns asked file path
    or returns none if got wrong answer at the YES or NO overwrite permission ask
    """
    notify("notify", "Creating File...", "")
    try:
        _ = open(file, "x").close()
    except FileExistsError:
        notify(
            "problem", "Creating File...Failed \n" +
            "File Already Exists Confirm Overwrite : (N or Y) ", "", True
        )
        while True:
            choice = str(input("")).upper()

            if choice == "Y":
                break
            elif choice == "N":
                file = os.path.dirname(
                    file) + "\\" + str(input("Write Down new file name here : ")) + ".pyw"
            else:
                notify("problem", "\nInvalid Input Try Again")

    else:
        print("Done")
    return file


def open_file(path: str):
    notify("notify", "Opening File To Write Data On It...", "")
    try:
        file = open(path, "w+")
    except Exception:  # pylint: disable=W0703; # noqa
        notify(
            "problem", "Opening File To Write Data On It...Failed \n Cannnot Open File", "\n", True)
        return

    else:
        print("Done")
    return file


def write_file(file, data: str):
    if file.writable():
        file.write(data)

    else:
        notify('problem', "The file is not writable please try again . "
               "if the problem presists please report it")
    file.close()
