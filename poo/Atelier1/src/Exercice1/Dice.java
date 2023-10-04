package Exercice1;

import java.util.logging.*;
import java.lang.String;
import java.util.*;

public class Dice {
	final static protected int minFaces = 3;
	final static protected int maxFaces = 120;
	
	final static protected int nbFacesDefaut = 6;
	
	private static int nbDices = 0;
	
	public static int getNbDices() {
		return nbDices;
	}
	
	private String name;
	private int nbFaces;
	
	private static Random r = new Random();
	
	// CONSTRUCTEUR 
	
	public Dice(String name, int nbFaces) {
		setNbFaces(nbFaces);
		setName(name);
		nbDices++;
	}
	
	public Dice(int nbFaces){
		this(null, nbFaces);
	}
	
	public Dice(String name) {
		this(name, nbFacesDefaut);
	}
	
	public Dice() {
		this(null, nbFacesDefaut);
	}
	
	////
	
	// GETTERS SETTERS
	
	public int getNbFaces() {
		return nbFaces;
	}
	
	public void setNbFaces(int nbFaces) {
		try {
			testNbFaces(nbFaces);
		}catch(IllegalArgumentException ex){
			
	        // Create a Logger
	        Logger logger
	            = Logger.getLogger(
	                Dice.class.getName());
	  
	        // Set Logger level()
	        logger.setLevel(Level.WARNING);       
	  
	        // Call warning method
	        logger.warning("Valeur invalide pour nombre de faces = " 
	        + nbFaces + ". Ce nombre doit etre compris entre 3 et 120" + 
	        		" exclus. Nombre de faces" + " affecte a defaut (6).");

			this.nbFaces = nbFacesDefaut;
		}
	}
	
	protected void testNbFaces(int nbFaces) {
		if (nbFaces >= minFaces && nbFaces <= maxFaces) {
			this.nbFaces = nbFaces;
		}else {
			throw new IllegalArgumentException();
		}
	}

	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		if (name == null || name == "") {
			this.name = "De numero " + (nbDices + 1);
		}else {
			this.name = name;
		}
	}
	
	////
	
	// METHODES

	public int lancer() {
		int nbAleatoire = r.nextInt(nbFaces) + 1;
		return nbAleatoire;
	}
	
	public int lancer(int nbLances) {
		int meilleurLance = 1;
		for (int i =0; i < nbLances; i++) {
			int nouveauLance = lancer();
			if (meilleurLance < nouveauLance) {
				meilleurLance = nouveauLance;
			}
		}
		return meilleurLance;
	}
	
	// AFFICHAGE
	@Override
	public String toString() {
		return "Nom : " + name + ", NbFaces : " + nbFaces;
	}
	
	//EQUALS
	@Override
	public boolean equals(Object obj) {
		boolean equals = false; 
		 
        // Si l'objet est comparé avec lui-même 
        if (obj == this) {
            equals = true;
        }else {
            // On regarde si l'objet est instance de Dice
            if ((obj instanceof Dice)) {
                // on caste vers Dice pour comparer
                Dice dice = (Dice) obj;
                 
                // on compare toutes les propriétés
//                equals = Integer.compare(nbFaces, dice.nbFaces) == 0
//                        && name.compareTo(dice.name) == 0;
                equals = ((nbFaces == dice.nbFaces)&& (name.equals(dice.name)));
            }
        }
        return equals;
	}
}
