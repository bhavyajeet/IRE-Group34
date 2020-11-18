template = open('./temp.txt','r')

curr = template.readline()

while curr :
    curr = template.readline()
    curr1 = curr.split('^^') 
    print (curr1)
