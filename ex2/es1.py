import sys

if len(sys.argv) < 3:
  print('error!')

p1 = sys.argv[1]
p2 = sys.argv[2]

print("parametri: ", p1, p2)

#---------------

print("inserire parametro: ")
P1 = int(input())
if (P1 == 0):
  print("inserire secondo parametro: ")
  P2 = input()
else:
  print("inserire nuovamente primo parametro: ")
  P1 = int(input())
  P2 = 1-P1

print("parametri: ", P1, P2)

#----------------

infile = 'ex2/mydata.dat'
indata = open(infile, "r")

print("scegli set di parametri: ")
inp = int(input())
linee = indata.readlines(inp)
indata.close()
print(linee)