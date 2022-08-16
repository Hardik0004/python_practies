import imp
from telnetlib import PRAGMA_HEARTBEAT


print("Number Pattern")

row=5
import pdb
pdb.set_trace()
for i in range(1,row+1,1):
  for j in range(1,i+1,1):
     print(j,end="")
  print("")