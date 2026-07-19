class SinglyNode :
  def __init__(self,data,next= None):
    self.data = data
    self.next = next

# function for displaying content of linked list
def display(Head):
  temp = Head
  while temp :
    print(temp.data)
    temp = temp.next

# function for printing linked list
def traverse(Head):
  temp = Head
  llist = []
  while temp :
    llist.append(str(temp.data))
    temp = temp.next
  print(' -> '.join(llist))

# function for inserting node at begining
def ins_at_beg(Head,data):
  newnode = SinglyNode(data)
  newnode.next = Head
  return newnode
  
# function for inserting node in last
def ins_at_end(Head,data):
  newnode = SinglyNode(data)
  temp = Head
  while temp.next:
    temp = temp.next
  temp.next = newnode
  return Head

# function for inserting in position
def ins_at_pos(Head,data,pos):
  newnode = SinglyNode(data)
  if pos == 0:
    newnode.next = Head
    return newnode
  temp = Head
  for i in range(pos-1):
    temp= temp.next
  
  newnode.next = temp.next
  temp.next = newnode
  return Head

 
# function for searching specific value in a linked list
def search(Head,value):
   temp = Head
   while temp:
     if temp.data == value:
       return True
     temp = temp.next  
   return False

# function for deleting a node in linked list
def delete(Head,pos):
  if Head ==  None:
    return None
  # delete first node
  if pos == 0:
    Head = Head.next
    return Head
    # delete node by position
  temp = Head
  for i in range(pos-1):
    temp= temp.next
  temp.next = temp.next.next
  return Head

# function for updating a value in linked list
def update(Head,pos,data):
  temp = Head
  for i in range(pos):
    if temp is None:
      return Head
    temp = temp.next
  temp.data = data
  return Head

# function : deleting by value
def remove_by_value(Head,data):
  if Head is None:
    return Head
  # if head contain value then
  if Head.data == data:
    return Head.next
  temp = Head
  while temp and temp.next.data != data:
    temp = temp.next
  temp.next = temp.next.next
  return Head

# function : insert after value
def insert_after_value(Head,value,data):
  newnode = SinglyNode(data)
  if Head is None:
    return newnode
  temp = Head
  while temp and temp.data != value:
    temp= temp.next
  newnode.next = temp.next
  temp.next = newnode
  return Head
  
  

# creating first node
Head = SinglyNode(10)
A = SinglyNode("Jan")
Head.next = A
B = SinglyNode(20)
A.next = B
C = SinglyNode("Feb")
B.next = C


display(Head)
traverse(Head)
Head = ins_at_beg(Head,5)
print("After inserting at begining linked list is ")
traverse(Head)
print("After inserting at end linked list is ")
Head = ins_at_end(Head,30)
traverse(Head)
print("After inserting at position - ")
Head = ins_at_pos(Head,"abc",2)
traverse(Head)
print(search(Head,"abc"))
print("After deleting node of 2nd position linked list is --" )
Head = delete(Head,2)
traverse(Head)
Head = update(Head,0,"xxxx")
traverse(Head)
Head = remove_by_value(Head,"Jan")
traverse(Head)
Head = insert_after_value(Head,"xxxx","yyyy")
traverse(Head)