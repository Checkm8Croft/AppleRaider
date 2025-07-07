import subprocess
import platform

def main():
    print("Welcome to Apple Raider! All stuff you need for Tomb Raider for your mac")
    print("Choose what you'd like to install")
    print("1. TR1X (Tomb Raider 1 and UB natively)")
    print("2. TR2X (Tomb Raider 2 and GM natively)")
    print("3. Wine (for excuting windows apps and for install all TRs)")
    print("4. Bootcamp (for booting Windows natively on your Intel Mac)")
    print("5. VMs (for choose a VM software)")
    choice = input("Type a number to select")
    choice = int(choice)
    if choice == 1:
        subprocess.run("TR1/install_tr1x.py")
    elif choice == 2:
        subprocess.run("TR2/install_tr2x.py")
    elif choice == 3:
        subprocess.run("Univ/Wine.py")
    elif choice == 4:
        subprocess.run("Univ/Bootcamp.py")
    elif choice == 5:
        subprocess.run("Univ/VMs.py")
    else:
        print("Not a valid choice")
        return

if __name__ == "__main__":
    if platform.system() == "Darwin":
        main()
    elif platform.system() == "Linux":
        print("You can't run this script on Linux")
    elif platform.system() == "Windows":
        print("Are you seriosly trying to run this on Windows?")
    exit(0)