from subprocess import call
import os

def main():

    createGitRepository()
    createGitIgnore()
    createFileDirectory()
    startSbt()
    createReadme()
    print("DONE!")


def createFileDirectory():
    shell("mkdir", "src")
    changeDirectory("src/")
    shell("mkdir", "main")
    shell("mkdir", "test")
    changeDirectory("main/")
    shell("mkdir", "scala")
    changeDirectory("scala/")
    os.system("echo > Main.scala")
    createBasicMainFile()
    changeDirectory("../../..")



def createGitIgnore():
    os.system("""echo >> .gitignore""")

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



def createBasicMainFile():
    main = open("Main.scala","w")
    main.write("object Main\n")
    main.write("""\tdef main(args: Array[String]) {\n""")
    main.write("""\t}\n""")
    main.write("""}""")
    main.close()


main()
