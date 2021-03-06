from release import __version__,files,dirs
import requests
import os
import sys
import shutil
LATEST_VERSION_URL = "https://github.com/000Zer000/ZKit-Framework/releases/latest"
DOWNLOAD_URL = "https://codeload.github.com/000Zer000/ZKit-Framework/zip/{version}"
PATH = '\\'.join(__file__.replace("/", '\\').split("\\")[:-3])
"""
Thanking Teraskull . He have helped me a lot in here 
"""
class API:
    def __init__(self):
        print("Initalizing updater")
        self.version = __version__

    def get_latest_release(self):
        try:
            resp = requests.get(LATEST_VERSION_URL)
            return resp.history[0].headers['location'].split("/")[-1]
        except:  # noqa
            print("Failed")
        else :
            print("Done")

    def check_for_updates(self):
        print("Checking for updates...", end="")
        self.latest_release = self.get_latest_release()
        if self.latest_release is None:
            # Using ZKit Offline
            print("Using ZKit-Framework Offline . Ignoring Updater")

        elif str(self.latest_release) > str(__version__):
            print("you are using zkit-framework version {} however zkit-framework {} is available for download.\
                  please update your framework with command : \
                  python updater.py update".format(self.latest_release, __version__))
        else:
            print(f"Your are using the latest version ({__version__})")

    def _download_version(self, version):
        print("Downloading version {} from github...".format(version), end="")
        resp = requests.get(DOWNLOAD_URL.format(version=version))
        print("Done")
        self.sourcepath = BACKUP_FOLDER + \
            "\\ZKit-Framework-{}.zip".format(version)

        with open(sourcepath, 'wb') as f:
            f.write(resp.content)

    def update(self):
        self.deleverything()
        self.check_for_updates()
        self._download_version(self.latest_release)
        print("Extracting {} to retreive source code...".format(
            self.sourcepath), end="")
        self._extract(self.sourcepath, PATH)
        print("Done")
        print(f"Successfully updated ZKit-Framework v{__version__} to v{self.latest_release}")

    def repair(self):
        self.check_for_updates()
        try:
            input("This operation will delete everything in dir ZKit-FrameworkTake your time for ba\
                  cking up your user-payloads or any data you want in this directory (if any)Press \
                  enter when you are ready for repair or press Ctrl + C or Ctrl + Z(nix Ctrl + D) f\
                  or canceling this operation")

        except (KeyboardInterrupt, EOFError):
            print("User requested exit\ncanceling repair operation")
            raise SystemExit
        self.deleverything()
        if self.latest_release != __version__:
            version = self.latest_release if input(
                "Do you want to update your framework instead of repairing it \
                (does the same but addes more features) (Y/N) ?").lower() \
                == "Y" else __version__
            self._download_version(version)
            print(f"Extracting {self.sourcepath} to retrieve source code...", end="")
            self._extract(self.sourcepath, PATH)
            print("Done")
            print("Your ZKit-Framework was successfully repaired")
            
    def deleverything(self):
        # thanking Teraskull for his help here
        for file in files:
            os.remove(file)
        for dir_ in dirs:
            os.rmdir(dir_)

    @staticmethod
    def _extract(file: str, where_to_extract: str):
        from zipfile import ZipFile
        with ZipFile(file, 'r') as zip_:
            zip_.extractall(where_to_extract)
        os.remove(file)


if len(sys.argv) != 1:
    api = API()
    if sys.argv[1].lower() in ("-u", "update"):
        api.update()
    elif sys.argv[1].lower() in ("-r", "repair"):
        api.repair()
    else:
        print("Invalid Input Please run it with '-h' for getting help")
