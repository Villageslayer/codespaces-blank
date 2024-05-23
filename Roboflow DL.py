
from roboflow import Roboflow
import os



os.chdir("Datasets")


api_key = "gN8RE4eJC99iXRoUT8JI"
rf = Roboflow(api_key)
project = rf.workspace("worky").project("rrrr-0sbnp")
versions = 8 # number of versions to download
versionnr = 0
for versionnr in range(versions):
    versionnr = versionnr + 1
    version = project.version(versionnr)
    dataset = version.download("yolov8")
