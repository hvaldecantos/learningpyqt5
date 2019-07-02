public class GList<T> {
  
  private class GNode<T> {
    T data;
    GNode next;
  
    public GNode(T val) {
      data = val;
      next = null;
    }
  
  }
  
  private GNode<T> cursor;
  private GNode<T> head;
  
  public GList(T t) {
    head = new GNode<>(t);
    cursor = null;
  }
  
  //Gets the first element in the list (this will only ever be called when the list has only one element)
  public T getFirst() {
    if (head == null) return null;
    return head.data;
  }
  
  //Resets the pointer to pointing at the lists first element
  public void startTraverse() {
    cursor = head;
  }
  
  public boolean hasNext() {
    return cursor != null;
  }
  
  //Returns the next value in the list and advances the cursor to the next value
  public T getNext() {
    T retval = cursor.data;
    cursor = cursor.next;
    return retval;
  }
  
  //Makes the current last element in the list point to the new element t
  public void setNext(T t) {
    GNode node = head;
    while (node.next != null) node = node.next;
    node.next = new GNode<>(t);
  }
  
}