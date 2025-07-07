import os
import subprocess

def check_pm():
    brew = '/usr/local/Homebrew/bin/brew'
    port = '/opt/local/bin/port'
    if os.path.exists(brew):
        print("Homebrew found")
        subprocess.run("brew install --cask wine-stable", shell=True)
        print("Wine installed")
    elif os.path.exists(port):
        print("MacPorts found")
        subprocess.run("sudo port install wine-stable", shell=True)
        print("Wine Installed")
    elif os.path.exists(brew) and os.path.exists(port):
        print("Both macports and homebrew found")
        pm = input("Since you have both MacPorts and Hombrew type (h/m) for select a package manager to use: ").strip().lower()
        if pm == "h":
            subprocess.run("brew install --cask wine-stable", shell=True)
        elif pm == "m":
            subprocess.run("sudo port install wine-stable", shell=True)
        else:
            print("Please enter (h/m)")
            return
        print("Wine installed")
    else:
        print("There's no macports or homebrew installed, yould you like to install one of them?")
        input("Press ENTER to continue")

def check_wine():
    wine_dirs = {
        "/Applications/Wine.app"
        "/usr/local/bin/wine"
        "/opt/local/bin/wine"
    }
    if os.path.exists(wine_dirs):
        print("Wine already found, exiting...")
        exit(0)
    check_pm()

if __name__ == "__main__":
    check_wine()
    exit(0)