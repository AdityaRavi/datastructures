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
        n = self.Node(item)
        self.add(n)
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
    self.head = None
    self.tail = None
    self.pointer = None
    self.length = 0
  
  def clone(self):
    """Returns a shallow copy of this list.

    Returns
    -------
    object
          A shallow copy of this list.
    """
    new_list = LinkedList()
    self.pointer = self.head
    while self.pointer != None:
      new_list.add(self.pointer.element)
      self.pointer = self.pointer.next
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
    self.pointer = self.head
    while(self.pointer != None):
      if(self.pointer.element == element):
        return True
      self.pointer = self.pointer.next
    return False

  def descendingIterator(self):
    """Returns an iterator over the elements in this deque in reverse sequential order.

    Returns
    -------
    iterator
            An iterator that iterates this list in reverse order.
    """
    return

  def element(self):
    """Retrieves, but does not remove, the head (first element) of this list.

    Returns
    -------
    E
      Element at head of this list.
    """
    return self.head.element
  
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
    if(self.length - 1 < index):
      return None
    self.pointer = self.head
    pointer_index = 0
    while(pointer_index != index):
      self.pointer = self.pointer.next
      pointer_index += 1
    return self.pointer.element

  def getFirst(self):
    """Returns the first element in this list.

    Returns
    -------
    E
      Element at the beginning of this list.
    """
    return self.head.element

  def getLast(self):
    """Returns the last element in this list.

    Returns
    -------
    E
      Element at the end of this list.
    """
    return self.tail.element

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
    self.pointer = self.head
    pointer_index = 0
    while(self.pointer != None):
      if(self.pointer.element == element):
        return pointer_index
      self.pointer = self.pointer.next
      pointer_index += 1
    return -1

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
    self.pointer = self.tail
    pointer_index = self.length - 1
    while(self.pointer != None):
      if(self.pointer.element == element):
        return pointer_index
      self.pointer = self.pointer.prev
      pointer_index -= 1
    return -1

  def listIterator(self): # Don't need this in python
    """Returns a list-iterator of the elements in this list (in proper sequence), starting at the specified position in the list.
    Skip this
    """
    return
  
  def poll(self):
    """Retrieves and removes the head (first element) of this list.
    
    Returns
    -------
    E
     The element polled.
    """
    if(self.length == 0):
      return None
    element = self.head.element
    self.head = self.head.next
    self.head.prev = None
    self.length -= 1
    return element

  def pollFirst(self):
    """Retrieves and removes the first element of this list, or returns null if this list is empty.
    
    Returns
    -------
    E
     The element polled. None if this list is empty.
    """
    return self.poll()

  def pollLast(self):
    """Retrieves and removes the last element of this list, or returns null if this list is empty.

    Returns
    -------
    E
     The element polled. None if this list is empty.
    """
    if(self.length == 0):
      return None
    element = self.tail.element
    self.tail = self.tail.prev
    self.tail.next = None
    self.length -= 1
    return element

  def remove(self, index=None, element=None):
    """Retrieves an element of this list.

    If no parameters provided, removed the element at the head of this list
    If index provided, removes the element at the index
    If element provided, searches for and removes the element from the list if it exists
    If index andd element are provided, removes element from index if and only if it matches element

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
    return

  def removeFirst(self):
    """Removes and returns the first element from this list.

    Returns
    -------
    E
     The element removed. None if this list is empty.
    """
    return

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
    return

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
    return

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
    []
      An array of the elements in this list.
    """
    return

  def __iter__(self):
    """
    """
    return self

  def __next__(self):
    """
    """
    return

  def __eq__(self, element):
    """
    """
    return

  def __repr__(self):
    """
    """
    return

  def __str__(self):
    """
    """
    return

  def __hash__(self):
    """
    """
    return

  class Node:

    def __init__(self, element, next=None, prev=None):
      self.element = element
      self.next = next
      self.prev = prev

