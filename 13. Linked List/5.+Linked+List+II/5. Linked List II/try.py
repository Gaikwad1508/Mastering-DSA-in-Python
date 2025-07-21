from common import take_input_better, Node, createLLFromList, print_LL

def lenOfLL(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count

def midOfLL(head):
    if head is None or head.next is None:
        return head
    size = lenOfLL(head)
    mid = size //2
    count = 0
    temp = head
    while count < mid:
        temp = temp.next
        count += 1
    return temp

def middleOfLLUsingSlowAndFast(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def MergeTwoSortedLL(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    finalHead = None
    finalTail = None

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            if finalHead is None:
                finalHead = head1
                finalTail = head1
            else:
                finalTail.next = head1
                finalTail = head1
            head1 = head1.next
        else:
            if finalHead is None:
                finalHead = head2
                finalTail = head2
            else:
                finalTail.next = head2
                finalTail = head2
            head2 = head2.next
    
    if head1 is not None:
        finalTail.next = head1

    if head2 is not None:
        finalTail.next = head2

    return finalHead
        

odd_list = [1, 7, 12, 20, 32]
even_list = [8, 22, 33, 42, 51, 60]
head1 = createLLFromList(odd_list)
head2 = createLLFromList(even_list)

print("first linked list before merge:")
print_LL(head1)
print("second linked list before merge:")
print_LL(head2)

head3 = MergeTwoSortedLL(head1, head2)

print("merged linked list:")
print_LL(head3)

print("first linked list after merge:")
print_LL(head1)
print("second linked list after merge:")
print_LL(head2)

'''
first linked list before merge:
1->7->12->20->32->
second linked list before merge:
8->22->33->42->51->60->
merged linked list:
1->7->8->12->20->22->32->33->42->51->60->
first linked list after merge:
1->7->8->12->20->22->32->33->42->51->60->
second linked list after merge:
8->12->20->22->32->33->42->51->60->

by analyzin above output we can see that the original linked lists are modified.
'''
# The above approach modifies the original linked lists.

def reverseLL(head):
    if not head or not head.next:
        return head
    
    smallLLHead = reverseLL(head.next)

    temp = smallLLHead
    while temp.next:
        temp = temp.next

    temp.next = head
    head.next = None
    return smallLLHead

def reverseLLOptimized(head):
    if not head or not head.next:
        return head
    
    smallLLHead = reverseLLOptimized(head.next)

    TailOfReverseLL = head.next
    TailOfReverseLL.next = head
    head.next = None
    return smallLLHead

def reverseLLIterative(head):
    if not head or not head.next:
        return head
    
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

odd_list = [1, 7, 12, 20, 32]
head1 = createLLFromList(odd_list)
head2 = reverseLLIterative(head1)
print("after reversing the LL")
print_LL(head2)
