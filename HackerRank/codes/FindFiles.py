import os, shutil
for root, dirs, files in os.walk('E:/'):
    testcases = ""
    lists = []
    for name in dirs:
        if name.endswith('lop'):
            testcases = os.path.join(root, name)
            #shutil.rmtree(testcases)
            lists.append(testcases)
    print lists