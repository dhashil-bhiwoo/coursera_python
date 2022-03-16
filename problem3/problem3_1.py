def problem3_1(txtfilename):
    cc = 0
    ifh = open(txtfilename)
    for line in ifh.read():
        cc = cc + len(line)
        print(line,end="")
    print("\n\nThere are",cc,"letters in the file.")