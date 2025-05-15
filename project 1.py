data= {'mohit':75,'raj':76,'sonam':87,'nitin':54}
name= input("enter student's name=")
if name in data:
    print ("student's marks",data[name])
else :
    print("error name not found")
