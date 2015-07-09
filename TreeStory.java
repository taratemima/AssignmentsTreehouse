import java.io.Console;
 

public class TreeStory {
    
    
	public static void main(String[] args) {
        
		Console console = System.console();
        
/*  Some terms:
            
noun - Person, place or thing
            
verb - An action
            
adjective - A description used to modify or describe a noun
            
Enter your amazing code here!
        */
   
		String ageAsString = console.readLine("How old are you? ");
		int age = Integer.parseInt(ageAsString);
		if (age < 13){
			/*enter exit code*/
			console.printf("Sorry, you must be at least 13 to play this game\n");
			System.exit(0);
			}     
		String name = console.readLine("Enter your name:  ");
        
		String noun = console.readLine("Enter a noun, a word that means a person, place, or thing:  ");
        
		String adjective = console.readLine("Enter an adjective, a word used to modify or describe a noun:  ");
        
		String verb = console.readLine("Enter a verb, a word that means an action, that ends in -ing, such as 'drawing' or 'coding':  ");
  
		String adverb = console.readLine("Enter an adjective that works with verbs: ");    
        
		console.printf("%s is a %s %s.", name, adjective noun);
		console.printf("They are always %s %s\n", adverb, verb);
    
	}
    

}