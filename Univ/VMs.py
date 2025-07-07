import subprocess
import os

def qemu_install():
    print("Installing QEMU ")
    brew_path = "/usr/local/Homebrew/bin/brew"
    port_path = "/opt/local/bin/port"
    if os.path.exists(brew_path):
        print("with Homebrew")
        subprocess.run(["brew", "install", "qemu"], check=True)
    elif os.path.exists(port_path):
        print("with MacPorts")
        subprocess.run(["sudo", "port", "install", "qemu"], check=True)
    else:
        print("Please install Homebrew or MacPorts to continue.")

def main():
    print("This script helps you to automatically download and install the best free VM software for your system.")
    print("1. VMWare Fusion Pro")
    print("2. VirtualBox")
    print("3. Parallels Desktop (redirect tio official site, since it is not free)")
    print("4. QEMU")
    print("5. UTM")
    choice = input("Enter the number of your choice: ")
    choice = int(choice)
    os.chdir(os.path.expanduser("~/Downloads"))
    if choice == 1:
        print("Downloading VMWare Fusion Pro...")
        subprocess.run(["curl", "-O", "https://archive.org/download/vmware-fusion-13.5.2-23775688-universal_202406/VMware-Fusion-13.5.2-23775688_universal.dmg"], shell=True)
        print("VMWare Fusion Pro downloaded. You can find it on your Downloads folder.")
    elif choice == 2:
        vbox_choice = input("Type 1 to install Intel VirtualBox or 2 to install Apple Silicon VirtualBox: ")
        if vbox_choice == "1":
            print("Downloading Intel VirtualBox...")
            subprocess.run(["curl", "-O", "https://download.virtualbox.org/virtualbox/7.1.10/VirtualBox-7.1.10-169112-OSX.dmg"], shell=True)
        elif vbox_choice == "2":
            print("Downloading Apple Silicon VirtualBox...")
            subprocess.run(["curl", "-O", "https://download.virtualbox.org/virtualbox/7.1.10/VirtualBox-7.1.10-169112-macOSArm64.dmg"], shell=True)
        else:
            print("Invalid choice")
            return
        print("VirtualBox downloaded. You can find it on your Downloads folder.")
    elif choice == 3:
        print("Please visit the official Parallels Desktop website to download the software.")
    elif choice == 4:
        qemu_install()
    elif choice == 5:
        print("Installing UTM...")
        subprocess.run("curl -O https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg", shell=True)
        print("UTM downloaded. You can find it on your Downloads folder.")
    else:
        print("Invalid choice")
        return