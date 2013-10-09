# encoding=utf-8

pi = float(3.141592653589)
e = float(2.711828182845)

l = []
task = raw_input("Please, enter <const:rang>\n")
task.split(":")
for w in task.split(":"):
   l.append(w)

if len(l)== 2:
   num = int(l[1])
   if l[0] == "pi":
      print round(pi,num)
   elif l[0] == "e":
      print round(e,num)
   else:
      print "Not found constant"
else:
   print "incorrect data"