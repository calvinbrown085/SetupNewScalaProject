from subprocess import call
import os

def main():
    print("Creating Empty git repository")
    createGitRepository()
    print("Creating a git ignore")
    createGitIgnore()
    print("Creating your file directory with a test directory")
    createFileDirectory()
    print("Starting SBT")
    startSbt()
    print("Creating a readme")
    createReadme()

    print("DONE!")


def createFileDirectory():
    shell("mkdir", "src")
    changeDirectory("src/")
    shell("mkdir", "main")
    shell("mkdir", "test")
    changeDirectory("main/")
    shell("mkdir", "scala")
    changeDirectory("../..")



def createGitIgnore():
    os.system("""echo > .gitignore""")

def createGitRepository():
    shell("git", "init")

def startSbt():
    shell("sbt", "")

def createReadme():
    os.system("echo > readme.md")

def changeDirectory(location):
    os.chdir(location)



def shell(first, second):
    call([first, second])

main()
