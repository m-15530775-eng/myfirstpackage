import subprocess

def commands(word:str,pig:str):
    if word.lower() == "install":
            subprocess.run(f"python -m pip install {pig}")
    elif word.lower() == "uninstall":
            subprocess.run(f"python -m pip uninstall {pig}")
    elif word.lower() == "upgrade":
            subprocess.run(f"python -m pip install --upgrade {pig}")
    elif word.lower() == "list":
            if pig.lower() == "-u":
                subprocess.run("python -m pip list --uptodate")
            elif pig.lower() == "-o":
                subprocess.run("python -m pip list --outdated")

