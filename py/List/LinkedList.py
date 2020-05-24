"""Implements a LinkedList data-structure
"""
class LinkedList:
  """Creates a LinkedList

  LinkedList created containing the elements specified in collection, in the order returned by the collection iterator.
  Empty LinkedList created if collection is not specified.

  Parameters
  ----------
  collection : collections
               A collection of items.
  """


  def __init__(self, collection=None):
    self.head = None
    self.tail = None
    self.pointer = None
    self.length = 0
    if(collection):
      self.addAll(collection=collection)

  def add(self, element, index=None):
    """Inserts the specified element to the list.

    Inserts the specified element at the specified index in this list.
    Appends the specified element to the end of this list, if index not provided.

    Parameters
    ----------
    element : object
              The element to be insertedd.
    index : int
            Index to insert element at. (optional)
    
    Returns
    -------
    boolean
          True if succesful insertion. False otherwise.
    """
    node = self.Node(element)

    if(self.length == 0 and not index):
      #add to emply linked list
      self.head = node
      self.tail = node
      self.length = 1
      return True
    
    if(not index):
      #add to end
      self.tail.next = node
      node.prev = self.tail
      self.tail = node
      self.length += 1
      return True

    if(index <= self.length - 1):
      #add without creating intermediate None nodes
      self.pointer = self.head
      pointer_index = 0
      while(pointer_index != index):
        self.pointer = self.pointer.next
        pointer_index += 1
      self.pointer.prev.next = node
      node.prev = self.pointer.prev
      self.pointer.prev = node
      node.next = self.pointer
      self.length += 1
      return True
    
    #add with creating intermediate None nodes -> self.
    self.pointer = self.tail
    pointer_index = self.length
    while(pointer_index != index):
      m = self.Node(None)
      self.pointer.next = m
      m.prev = self.pointer
      self.pointer = self.pointer.next
      pointer_index += 1
    self.pointer.next = node
    node.prev = self.pointer
    self.tail = node
    self.length = index + 1
    return True

  def addAll(self, collection, index=None):
    """Inserts all the elements in the specified collection to the list in the order specified by the iterator of collection.

    Inserts the elements starting at the specified index.
    Appends the elements to the end of this list, if index not provided.

    Parameters
    ----------
    elements : collections
              The collection of elements to be inserted.
    index : int
            Index to insert the collection at. (optional)

    Returns
    -------
    boolean
           True if succesful insertion. False otherwise.
    """
    if(not index):
      #add collection to the end of list
      for item in collection:
        self.add(item)
      return True
    
    #add collection to the specified index
    index_cpy = index
    for item in collection:
      self.add(item, index_cpy)
      index_cpy += 1
    return True

  def addFirst(self, element):
    """Inserts the specified element at the beginning of this list.

    Parameters
    ----------
    element : object
              The element to be inserted.

    Returns
    -------
    boolean
           True if succesfull insertion. False otherwise.
    """
    return self.add(element, 0)

  def addLast(self, element):
    """Appends the specified element to the end of this list.

    Parameters
    ----------
    element : object
              The element to be appended.

    Returns
    -------
    boolean
           True if succesfull insertion. False otherwise.
    """
    return self.add(element)

  def clear(self):
    """Removes all of the elements from this list.

    Returns
    -------
    void
    """
    self.__init__()
  
  def clone(self):
    """Returns a shallow copy of this list.

    Returns
    -------
    object
          A shallow copy of this list.
    """
    new_list = LinkedList()
    for element in self:
      new_list.add(element)
    return new_list

  def contains(self, element):
    """Returns true if this list contains the specified element.

    Parameters
    ----------
    element : object
              The element to check for.
    
    Returns
    -------
    boolean
           True if element exists. False otherwise.
    """
    for e in self:
      if(e == element):
        return True
    return False

  def descendingIterator(self):
    """Returns an iterator over the elements in this deque in reverse sequential order.

    Returns
    -------
    iterator
            An iterator that iterates this list in reverse order.
    """
    return

  def _getNodeFromIndex(self, index):
    # Empty list or invalid index
    if(self.length - 1 < index or index < 0):
      return None
    # Search from head
    if(index <= self.length / 2):
      return self._getNodeFromHead(index)
    # Search from tail
    return self._getNodeFromTail(index)

  def _getNodeFromHead(self, index):
    pointer = self.head
    pointer_index = 0
    while(pointer_index != index and pointer_index < self.length):
      pointer = pointer.next
      pointer_index += 1
    return pointer

  def _getNodeFromTail(self, index):
    pointer = self.tail
    pointer_index = self.length - 1
    while(pointer_index != index and pointer_index >= 0):
      pointer = pointer.prev
      pointer_index -= 1
    return pointer
  
  def _getNodeFromElement(self, element):
    pointer = self.head
    pointer_index = 0
    while(pointer_index < self.length):
      if(pointer.element == element):
        return pointer
      pointer = pointer.next
      pointer_index += 1
    return None

  def _getElementIndexFromHead(self, element):
    pointer = self.head
    pointer_index = 0
    while(pointer_index < self.length):
      if(pointer.element == element):
        return pointer_index
      pointer = pointer.next
      pointer_index += 1
    return -1

  def _getElementIndexFromTail(self, element):
    pointer = self.tail
    pointer_index = self.length - 1
    while(pointer_index >= 0):
      if(pointer.element == element):
        return pointer_index
      pointer = pointer.prev
      pointer_index -= 1
    return -1
  
  def get(self, index):
    """Returns the element at the specified position in this list.
    Returns None if the element does not exist

    Parameters
    ----------
    index : int
            The index of the element to be returned.

    Returns
    -------
    E
      Element at index.
    """
    node = self._getNodeFromIndex(index)
    if(not node):
      return None
    return node.element

  def getFirst(self):
    """Returns the first element in this list.

    Returns
    -------
    E
      Element at the beginning of this list.
    """
    return self.get(0)

  def getLast(self):
    """Returns the last element in this list.

    Returns
    -------
    E
      Element at the end of this list.
    """
    return self.get(self.length - 1)

  def indexOf(self, element):
    """Returns the index of the first occurrence of the specified element in this list, or -1 if this list does not contain the element.

    Parameters
    ----------
    element : object
              Element whose index is desired.

    Returns
    -------
    int
       Index of element.
    """
    return self._getElementIndexFromHead(element)

  def lastIndexOf(self, element):
    """Returns the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element.
    
    Parameters
    ----------
    element : object
              Element whose last index is desired.

    Returns
    -------
    int
       Last index of element.
    """
    return self._getElementIndexFromTail(element)

  def listIterator(self): # Don't need this in python
    """Returns a list-iterator of the elements in this list (in proper sequence), starting at the specified position in the list.
    Skip this
    """
    return

  def _removeNode(self, node):
    if(node.next):
      node.next.prev = node.prev
    else:
      self.tail = node.prev
    if(node.prev):
      node.prev.next = node.next
    else:
      self.head = node.next

  def remove(self, index=None, element=None):
    """Retrieves an element of this list.

    If no parameters provided, removed the element at the head of this list
    If index provided, removes the element at the index
    If element provided, searches for and removes the element from the list if it exists
    If index and element are provided, removes element from index if and only if it matches element

    Parameters
    ----------
    index : int (optional)
            The index of the element to be removed
    element : object (optional)
              The element to be removed

    Returns
    -------
    E
     The element removed. None if the element or index is invalid of if this list is empty.
    """
    removedElement = None
    # element and index not defined
    if((not index) and (not element)):
      node = self._getNodeFromIndex(0)
    
    #element and index both defined
    elif (index and element):
      node1 = self._getNodeFromIndex(index)
      node2 = self._getNodeFromElement(element)
      if(node1 == node2 or node1.element == node2.element):
        node = node1
    
    # only index provided
    elif(index):
      node = self._getNodeFromIndex(index)

    # only element provided
    else:
      node = self._getNodeFromElement(element)

    if(node):
      removedElement = node.element
      self._removeNode(node)
    
    return removedElement

  def removeFirst(self):
    """Removes and returns the first element from this list.

    Returns
    -------
    E
     The element removed. None if this list is empty.
    """
    return self.remove(0)

  def removeFirstOccurrence(self, element):
    """Removes the first occurrence of the specified element in this list (when traversing the list from head to tail).
    
    Returns
    -------
    E
     The element removed. None if element does not exist or this list is empty.
    """
    return

  def removeLast(self):
    """Removes and returns the last element from this list.

    Returns
    -------
    E
     The element removed. None if element does not exist or this list is empty.
    """
    return self.remove(self.length - 1)

  def removeLastOccurrence(self, element):
    """Removes the last occurrence of the specified element in this list (when traversing the list from head to tail).
    
    Returns
    -------
    E
     The element removed. None if element does not exist or this list is empty.
    """
    return

  def setIndex(self, index, element):
    """Replaces the element at the specified position in this list with the specified element.
    
    Returns
    -------
    E
     The element previously at that position.
    """
    newNode = self.Node(element)
    oldNode = self._getNodeFromIndex(index)

    newNode.next = oldNode.next
    newNode.prev = oldNode.prev

    if(newNode.next):
      newNode.next.prev = newNode
    else:
      self.tail = newNode
    if(newNode.prev):
      newNode.prev.next = newNode
    else:
      self.head = newNode

    oldNode.next = None
    oldNode.prev = None

    return oldNode.element

  def size(self):
    """Returns the number of elements in this list.

    Returns
    -------
    int
     The size of this list.
    """
    return self.length

  def toArray(self):
    """Returns an array containing all of the elements in this list in proper sequence (from first to last element).
    
    Returns
    -------
    list
      An array of the elements in this list.
    """
    arr = []
    for element in self:
      arr.append(element)
    return arr

  def __iter__(self):
    """
    """
    self.pointer = self.head
    return self

  def __next__(self):
    """
    """
    if(self.pointer == None):
      raise StopIteration
    element = self.pointer.element
    self.pointer = self.pointer.next
    return element

  def __eq__(self, anotherList):
    """
    What do you define as equal? Just contents or type as well?
    - Have the same type
    - Have the same length
    - Have the same content
    - Each element can be compared using == 
    """
    result = True
    result = result and isinstance(anotherList, LinkedList)
    result = result and (self.size() == anotherList.size())

    if(result):
      lst1 = self.toArray()
      lst2 = anotherList.toArray()

      for i in range(0, self.size()):
        if(lst1[i] != lst2[i]):
          result = False
          break

    return result


  def __repr__(self):
    """String representation of this LinkedList
    """
    return str(self.toArray())

  def __hash__(self):
    """
    """
    return

  class Node:

    def __init__(self, element, next=None, prev=None):
      self.element = element
      self.next = next
      self.prev = prev

