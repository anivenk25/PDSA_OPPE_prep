#code to take space separated input from user and print the sum of the numbers
'''a = set(map(int, input().split()))
print ( "Output Linked List :",end = " ")
for i in range (len(a)):
    print (a.pop(), end = " ")'''

def removeDuplicate(head) :
    current = head 

    while (current.next != None) : 
        if current.data == current.next.data : 
            current.next=current.next.next 
        else : 
            current = current.next 

    
