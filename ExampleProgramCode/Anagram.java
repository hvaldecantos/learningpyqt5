import java.io.*;
import java.util.*;

public class Anagram {
  
  //Returns a String in which every character is a lowercase letter
  public static String clean(String s) {
    char[] ch = s.toLowerCase().toCharArray();
    int i = 0;
    for (char c : ch) if (Character.isLetter(c)) i++;
    char[] cleaned = new char[i];
    i = 0;
    for (char c : ch) if (Character.isLetter(c)) cleaned[i++] = c;
    return String.valueOf(cleaned);
  }
  
  //Returns a String in which every character is a lowercase letter and every letter is in alphabetical order
  public static String createKey(String s) {
    char[] ch = s.toLowerCase().toCharArray();
    int i = 0;
    for (char c : ch) if (Character.isLetter(c)) i++;
    char[] cleaned = new char[i];
    i = 0;
    for (char c : ch) if (Character.isLetter(c)) cleaned[i++] = c;
    Arrays.sort(cleaned);
    return String.valueOf(cleaned);
  }
  
  public static void main(String[] args) {
    try {
      //The first argument is the file to be read from, the second argument is the file to be wrote to
      BufferedReader br = new BufferedReader(new FileReader(args[0]));
      BufferedWriter bw = new BufferedWriter(new FileWriter(args[1]));
      Scanner input = new Scanner(br);
      BinTree<AnaData> binTree = new BinTree<>();
      while (input.hasNext()) {
        String word = input.next();
        String cleanWord = clean(word);
        if (!cleanWord.equals("")) {
          String key = createKey(word);
          AnaData anaData = new AnaData(key, new GList<String>(cleanWord), bw);
          AnaData foundData = (AnaData)binTree.find(anaData);
          //If find() find a node that has a same key and no same words within the list, add the word to that list
          if (foundData != null)
            if (foundData.hasUnique(anaData)) {
              foundData.addData(anaData);
              binTree.insert(foundData);
          }
        }
      }
      //Print all the anagram groups on different lines then close both files
      AnaData.resetNewLine();
      binTree.traverse();
      br.close();
      bw.close();
    }
    catch (Exception e) {
      System.exit(0); //If arguments aren't provided when the program is run, the program will exit
    }
  }
  
}