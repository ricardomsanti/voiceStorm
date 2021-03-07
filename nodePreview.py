import math
import subprocess as s
#Understanding the screen as a graphic,

yMax = 200

#The y axis grow varies as the number of directories present in the same level


#The x axis varies as the number of subdirectories grow, as well as the number of subdirectories of it's previe level

class Line:
    def __init__(self):
        self.limit = 200
        self.text = ""
        self.level = 0
        self.newSide = ""
        self.sideDict = {}
        self.sideLevel = 0
        self.previewLine = ""
        self.finalLine = ""
        self.line = ""


    def h_line(self, num=0):
        line = ""
        underline = "_"
        for x in range(num):
            line += underline
        return line


    def sideBuild(self):
        level = 0
        finalLine = ""
        while len(finalLine) <= self.limit:
            text = input("Label text> \n")
            finalLine += "|" + text + "|" + str(self.h_line(num=8))
            s.run(("cls"), shell=True)
            print(finalLine)
            newSide = input("Create sideLabel?> [y/n]")
            if newSide == "n":
                print()
                print()
                print("Finished Map----------------------------------------------")
                break
            else:
                continue

l = Line()
l.sideBuild()