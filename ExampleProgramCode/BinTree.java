  public class BinTree<T extends Visitable> {
  
  private class BNode<T extends Visitable> {
    T data;
    BNode left;
    BNode right;
  
    public BNode(T val) {
      data = val;
      left = null;
      right = null;
    }
  
  }
  
  private BNode root;
  
  public BinTree() {
    root = null;
  }
  
  //Inserts a new node into the BST, or if a node with the same key exists, replace the node with a new
  //node that contains a list of multiple anagrams
  public boolean insert(T t) {
    BNode node = root;
    while (node != null) {
      if (t.compareTo(node.data) == 0) {
        node.data = t;
        return true;
      }
      else if (t.compareTo(node.data) < 0) {
        if (node.left == null) {
          node.left = new BNode<>(t);
          return true;
        }
        else node = node.left;
      }
      else {
        if (node.right == null) {
          node.right = new BNode<>(t);
          return true;
        }
        else node = node.right;
      }
    }
    return true;
  }
  
  //This method is funky and not described well by "find" but it is essential. If the root is null, 
  //it replaces the root with a node containing data. If no nodes exists with the same key as t, 
  //insert() is called to create a new node. If a node with the same key as t exists, node.data
  //is returned so the main Anagram class can do something with that information after casting it.
  public Visitable<AnaData> find(T t) {
    if (root == null) {
      root = new BNode<>(t);
      return null;
    }
    BNode node = root;
    while (node != null && node.data.compareTo(t) != 0) {
      if (t.compareTo(node.data) < 0) node = node.left;
      else node = node.right;
    }
    if (node == null) {
      insert(t);
      return null;
    }
    return node.data;
  }
  
  //Starts calling visit() on every node, begins with the root then does a call on every other node
  //by using nodes as arguments. If a node is null, return is used to prevent errors or endless running.
  public void traverse() {
    if (root == null) return;
    traverse(root.left);
    root.data.visit();
    traverse(root.right);
  }
  
  public void traverse(BNode node) {
    if (node == null) return;
    traverse(node.left);
    node.data.visit();
    traverse(node.right);
  }
  
}