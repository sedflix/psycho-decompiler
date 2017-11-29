filename="2016017_1_Arnav.s"
checkswi="swi"
inputcode="0x6c"
outputcode="0x6b"
exitcode="0x11"
code=[]
detectMov=""
converted=[]
usedVariables={}
convertedCodeVariable="a1"
pseudoVariableCount=0
inputcounter=0
outputcounter=0
tempCounter=0
with open(filename) as lines:
    for line in lines:
        code.append(line)
        if checkswi in line:
            io=line.split()
            if io[1]==inputcode:
                # tempCounter=0;
                for index,val in enumerate(code):
                    if val==line:
                        tempCounter=index
                        flag='y'
                        inputcounter+=1
                        detectMov=code[index-1]
                        detectMov=detectMov.replace("\t","")

                        toAppend='scanf("%d",&'+str(convertedCodeVariable)+');\nint var'+str(pseudoVariableCount)+'='+str(convertedCodeVariable)+';\n'
                        pseudoVariableCount+=1

                        converted.append(toAppend)
                        print(detectMov)
                        print(converted)

            if io[1]==outputcode:

                toAppend='int output='+str(convertedCodeVariable)+';\n'+'printf("%d",&output);\n'
                converted.append(toAppend)

            if io[1]==exitcode:
                toAppend='exit(0);'
                converted.append(toAppend)
                break
newFile=open("converted.txt","w")
for content in converted:
    newFile.write(content)
