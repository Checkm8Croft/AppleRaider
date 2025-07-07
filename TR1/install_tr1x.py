import os
import subprocess

def install_ub():
    print("You have to install the Unfinished Business expansion.")
    input("Press enter to continue: ")
    print("1. Fan-made UB (with music triggers)")
    print("2. Original UB (without music triggers)")
    ub_type = input("Select UB type: ")
    ub_type = int(ub_type)
    if ub_type == 1:
        ub_url = "https://lostartefacts.dev/aux/tr1x/trub-music.zip"
    elif ub_type == 2:
        ub_url = "https://lostartefacts.dev/aux/tr1x/trub-vanilla.zip"
    else:
        print("Invalid selection")
        return
    os.chdir(os.path.expanduser("~/Downloads"))
    subprocess.run(f"curl -L {ub_url} -o trub.zip", shell=True)
    subprocess.run("unzip trub.zip", shell=True)
    dest_path = os.path.expanduser("/Applications/TR1X.app/Contents/Resources/")
    subprocess.run(f"mv -R data {dest_path}", shell=True)
    print("Unfinished Business files copied successfully!")

def copy_music():
    print("You now have to copy MUSIC files, you can download them from the TR1X's developer's website.")
    input("Press enter to continue: ")
    music_url = "https://lostartefacts.dev/aux/tr1x/music.zip"
    os.chdir(os.path.expanduser("~/Downloads"))
    subprocess.run(f"curl -L {music_url} -o music.zip", shell=True)
    subprocess.run("unzip music.zip", shell=True)
    dest_path = os.path.expanduser("/Applications/TR1X.app/Contents/Resources/")
    subprocess.run(f"mv -R music {dest_path}", shell=True)
    print("Music files copied successfully!")
    install_ub()

def copy_data():
    print("You now have to copy DATA files from an original copy of TR1")
    data_path = input("If you have CD or a path with DATA files, type it here (leave blank for exit): ")
    if data_path:
        if not os.path.exists(data_path):
            print(f"❌ Path {data_path} does not exist!")
        else:
            dest_path = os.path.expanduser("/Applications/TR1X.app/Contents/Resources/")
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            subprocess.run(f"mv -R {data_path}/DATA {dest_path}", shell=True)
            print("DATA files copied successfully!")

def install_tr1x():
    print("Downloading TR1X...")
    url = "https://github.com/LostArtefacts/TRX/releases/download/tr1-4.12.3/TR1X-4.12.3-Installer.dmg"
    os.chdir(os.path.expanduser("~/Downloads"))
    if os.path.exists("TR1X-Installer.dmg"):
        print("Already downloaded TR1X-Installer.dmg, skipping download.")
    else:
        subprocess.run(f"curl -L {url} -o TR1X-Installer.dmg", shell=True)
    print("Mounting TR1X Installer...")
    if not os.path.exists("/Volumes/TR1X\\ Installer"):
        subprocess.run("hdiutil attach TR1X-Installer.dmg")
    else:
        print("TR1X Installer already mounted.")
    print("Installing TR1X...")
    subprocess.run("cp -R /Volumes/TR1X\\ Installer/TR1X.app /Applications/", shell=True)
    subprocess.run("xattr -cr /Applications/TR1X.app", shell=True)
    print("TR1X copied successfully! Unmounting TR1X Installer...")
    subprocess.run("hdiutil detach /Volumes/TR1X\\ Installer", shell=True)
    print("TR1X Installer unmounted successfully! Cleaning up...")
    subprocess.run("rm TR1X-Installer.dmg", shell=True)
    print("TR1X installed successfully!")
    copy_data()

def check_tr1x():
    if os.path.exists("/Applications/TR1X.app"):
        print("TR1X is already installed.")
        if input("Do you want to reinstall it? This will remove your current TR1X Installation (yes/no): ").strip().lower() == "yes":
            subprocess.run("rm -rf /Applications/TR1X.app", shell=True)
            install_tr1x()
        else:
            exit(0)
    else:
        install_tr1x() 

if __name__ == "__main__":
    check_tr1x()
    print("You can now run TR1X from your Applications folder.")
    print("Enjoy the game!")