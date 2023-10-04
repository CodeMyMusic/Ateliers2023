package Exercice1;

import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class PolymorphDice extends Dice {
	ArrayList<Object> faces;

	public PolymorphDice(String name, ArrayList<Object> faces) {
		super(name);
		setFaces(faces);
	}

	public PolymorphDice(ArrayList<Object> faces) {
		this(null, faces);
	}
	
	public ArrayList<Object> getFaces(){
		return this.faces;
	}
	
	public void setFaces(ArrayList<Object> faces) {
		int nbFaces = faces.size();
		try {
			super.testNbFaces(nbFaces);
		}catch(IllegalArgumentException ex){
	        // Create a Logger
	        Logger logger
	            = Logger.getLogger(
	                PolymorphDice.class.getName());
	  
	        // Set Logger level()
	        logger.setLevel(Level.WARNING);       
	  
	        // Call warning method
	        logger.warning("Le nombre de faces total n'est pas valide. Les elements en trop sont retires pour "
	        		+ "que la taille de liste soit valide.");

	        this.faces = new ArrayList<Object>(faces.subList(0, maxFaces));
		}
	}
	
	@Override
	public String toString() {
		return super.toString() + ", liste de faces : " + faces;
	}
}
