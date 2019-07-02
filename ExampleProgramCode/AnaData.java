import java.io.*;

public class AnaData implements Visitable<AnaData>{
  private static boolean firstAnaData = true; //Use this so every line is followed by \n except the last line
  private String key;
  private GList<String> list;
  private BufferedWriter bw;
  
  public AnaData(String key, GList list, BufferedWriter bw) {
    this.key = key; //The key allows AnaData objects to know if they are anagrams
    this.list = list; //This lists all the words in the AnaData class, which should all be anagrams
    this.bw = bw; //Writer passes here so I only have to initialize it once
  }
  
  //Prints out all elements of the AnaData's list if it contains anagrams
  @Override
  public void visit() {
    list.startTraverse();
    try {
      list.getNext(); //getNext() before checking for next to see if a list has anagrams
      if (list.hasNext()) {
        if (firstAnaData) firstAnaData = false;
        else bw.newLine();
        list.startTraverse();
        boolean firstElement = true; //Use this so every element has a space after it except for the last one
        while (list.hasNext()) {
          if (firstElement) firstElement = false;
          else bw.write(" ");
          bw.write(list.getNext());
        }
      }
      else return;
    }
    catch (IOException ioe) {
      return; //This shouldn't ever happen but the catch is here so it can be compiled
    }
  }
  
  public void addData(AnaData a) {
    list.setNext(a.getFirst()); //Be careful with order, the parameter should only have one GList element
  }
  
  public String getFirst() {
    return list.getFirst();
  }
  
  public String getKey() {
    return key;
  }
  
  //Because firstAnaData is static, it doesn't change between running the program, 
  //so always call resetNewLine() before traverse()
  public static void resetNewLine() {
    firstAnaData = true;
  }
  
  //Checks every word in the GList, return true if none are the same, this makes repeating anagrams impossible
  public boolean hasUnique(AnaData a) {
    list.startTraverse();
    while (list.hasNext()) if (a.getFirst().equals(list.getNext())) return false;
    return true;
  }
  
  //Returns a negative number if this key precedes a's key, positive if a's key precedes this key, 0 if equal
  @Override
  public int compareTo(AnaData a) {
    return key.compareTo(a.getKey());
  }
  
}