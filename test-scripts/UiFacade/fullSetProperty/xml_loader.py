import os.path
from string import join

cur_dir = os.path.dirname(os.path.realpath(__file__)) + "/"

def getXML(filename):
    fin = open(cur_dir + filename, "r")
    lines = fin.readlines()
    fin.close()
    return join(lines)
