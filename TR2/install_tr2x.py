import os
import subprocess

def install_ub():
    print("You have to install the Unfinished Business expansion.")
    input("Press Enter to cintinue")
    gm_url = "https://lostartefacts.dev/aux/tr2x/trgm.zip"
    os.chdir(os.path.expanduser("~/Downloads"))
    subprocess.run(f"curl -L {gm_url} -o trgm.zip", shell=True)
    subprocess.run("unzip trgm.zip", shell=True)
    dest_path = os.path.expanduser("/Applications/TR2X.app/Contents/Resources/")
    subprocess.run(f"mv -R data {dest_path}", shell=True)
    print("Unfinished Business files copied successfully!")

def copy_music():
    print("You now have to copy MUSIC files, you can download them from the TR2X's developer's website.")
    input("Press enter to continue: ")
    music_url = "https://lostartefacts.dev/aux/tr2x/music.zip"
    os.chdir(os.path.expanduser("~/Downloads"))
    subprocess.run(f"curl -L {music_url} -o music.zip", shell=True)
    subprocess.run("unzip music.zip", shell=True)
    dest_path = os.path.expanduser("/Applications/TR2X.app/Contents/Resources/")
    subprocess.run(f"mv -R music {dest_path}", shell=True)
    print("Music files copied successfully!")
    install_ub()

def copy_data():
    print("You now have to copy DATA files from an original copy of TR2")
    data_path = input("If you have CD or a path with DATA files, type it here (leave blank for exit): ")
    if data_path:
        if not os.path.exists(data_path):
            print(f"❌ Path {data_path} does not exist!")
        else:
            dest_path = os.path.expanduser("/Applications/TR2X.app/Contents/Resources/")
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            subprocess.run(f"mv -R {data_path}/DATA {dest_path}", shell=True)
            print("DATA files copied successfully!")
            copy_music()

def install_tr2x():
    print("Downloading TR2X...")
    url = "https://github.com/LostArtefacts/TRX/releases/download/tr1-4.12.3/TR2X-4.12.3-Installer.dmg"
    os.chdir(os.path.expanduser("~/Downloads"))
    if os.path.exists("TR2X-Installer.dmg"):
        print("Already downloaded TR2X-Installer.dmg, skipping download.")
    else:
        subprocess.run(f"curl -L {url} -o TR2X-Installer.dmg", shell=True)
    print("Mounting TR2X Installer...")
    if not os.path.exists("/Volumes/TR2X\\ Installer"):
        subprocess.run("hdiutil attach TR2X-Installer.dmg")
    else:
        print("TR2X Installer already mounted.")
    print("Installing TR2X...")
    subprocess.run("cp -R /Volumes/TR2X\\ Installer/TR2X.app /Applications/", shell=True)
    subprocess.run("xattr -cr /Applications/TR2X.app", shell=True)
    print("TR2X copied successfully! Unmounting TR2X Installer...")
    subprocess.run("hdiutil detach /Volumes/TR2X\\ Installer", shell=True)
    print("TR2X Installer unmounted successfully! Cleaning up...")
    subprocess.run("rm TR2X-Installer.dmg", shell=True)
    print("TR2X installed successfully!")
    copy_data()

def check_tr2x():
    if os.path.exists("/Applications/TR2X.app"):
        print("TR2X is already installed.")
        if input("Do you want to reinstall it? This will remove your current TR2X Installation (yes/no): ").strip().lower() == "yes":
            subprocess.run("rm -rf /Applications/TR2X.app", shell=True)
            install_tr2x()
        else:
            exit(0)
    else:
        install_tr2x() 

if __name__ == "__main__":
    check_tr2x()
    print("You can now run TR2X from your Applications folder.")
    print("Enjoy the game!")