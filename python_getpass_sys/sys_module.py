import sys
import os

if not os.path.exists("/etc/hosts"):
    print("Directory does NOT exist")
elif os.path.exists("/etc/hosts"):
    print("Directory exists")
else :
    sys.exit()


print('Hello World!')
print(sys.argv)
print(sys.argv[0])