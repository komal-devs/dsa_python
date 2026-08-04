class Node :
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None

# traversing double linked list
def traverse(Head):
  if Head is None:
    print("None")
  temp = Head
  while temp :
    print(temp.data,end = "")
      
    if temp.next is not None:
      print("<->",end = "")
    temp = temp.next
  print()
  
# inserting a node at beginning
def insert_at_beg(Head,data):
  newnode = Node(data)
  temp = Head
  newnode.next = Head
  if Head is not None :
    Head.prev = newnode
    
  return newnode

# inserting node in end
def insert_at_end(Head,data):
  newnode = Node(data)
  if Head is None:
    Head = newnode
  else:
    temp = Head
    while temp.next is not  None:
      temp = temp.next
    temp.next = newnode
    newnode.prev = temp
  return Head

# insert a node in given position
def insert_at_pos(Head,data,pos):
  newnode = Node(data)
  
  if pos > get_length(Head):
    print("index out of length")
  elif Head is None :
    Head = insert_at_beg(Head,data)
  else :
    count= 1
    temp = Head
    while temp and count < pos - 1:
      temp = temp.next
      count += 1
    newnode.prev = temp
    newnode.next = temp.next
    temp.next = newnode
    return Head

# print length of linked list 
def get_length(Head):
  count = 0
  if Head is None:
    return 0
  else :
    temp = Head
    while temp :
      temp = temp.next
      count += 1
    return count

def delete_Head(Head):
  # deleting empty list
  if Head is None :
    return None
  else :
    
    Head = Head.next
    if Head is not None :
      Head.prev = None
    return Head  

def delete_by_value(key,Head):
  if Head is None:
    return None
  temp = Head
  while temp:
    if temp.data == key:
      break
    temp = temp.next
  # value not Found
  if temp is None:
    print("value not found  ")
    return Head
  # if deleting the first node
  if temp.prev == None:
    Head = temp.next
    if Head is not None :
      Head.prev = None
  else :
    temp.prev.next = temp.next
    if temp.next is not None:
      temp.next.prev = temp.prev
  return Head
  
    
    
  

if __name__ == "__main__" :
  # creating first node
  Head = Node(78)
  # creating second node
  Head.next = Node(20)
  Head.next.prev = Head
  # creating 3 node
  Head.next.next = Node(50)
  Head.next.next.prev = Head.next

  traverse(Head)
  # insert a node in beginning
  Head = insert_at_beg(Head,56)
  traverse(Head)
  # insert a node in the last
  Head = insert_at_end(Head,89)
  traverse(Head)
  # insert a node in specific position 
  Head = insert_at_pos(Head,"komal",2)
  traverse(Head)
 
  print("Length of double linked list : ", get_length(Head))
print("Linked list after deleting Head : ")
Head = delete_Head(Head)
traverse(Head)
Head = delete_by_value(78,Head)
traverse(Head)






