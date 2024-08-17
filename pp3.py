def mergeSortedList(head1,head2):
    #traverse the list 1 till the end 
    current1 = head1
    while ( current1.next != None):
        current1 = current1.next 
    current1.next = head2
    current2 = head1 
    alist = []
    while (current2 != None):
        alist.append(int(current2.data))
        current2 = current2.next 
    alist.sort()
    current3 = head1
    count= 0
    while (current3 != None):
        current3.data = alist[count]
        count += 1
        current3 = current3.next 
    return head1 

