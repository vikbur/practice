# encoding:utf-8
import math
consts = {"pi": math.pi, "e":math.e}

task = raw_input("Please, enter <const:rang>\n")
w = task.split(":")

if len(w)== 2:
print round(consts[w[0]],int(w[1]))
else:
print "incorrect data"