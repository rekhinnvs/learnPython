import os, shutil
for root, dirs, files in os.walk('/home/rekhin/Vizio/RegularTesting/M-Upgrade/'):
    testcases = ""
    for name in dirs:
        if name.endswith('testcases'):
            testcases = os.path.join(root, name)
            shutil.rmtree(testcases)



