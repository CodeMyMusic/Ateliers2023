package Exercice1;

import java.util.logging.*;

public class LoadedDice extends Dice {
	final static protected int borneMinimaleDefaut = 4;
	private int borneMinimale;
	
	public int getBorneMinimale() {
		return borneMinimale;
	}

	public LoadedDice(String name, int nbFaces, int borneMinimale) {
		super(name, nbFaces);
		try {
			if (borneMinimale < 1 || borneMinimale > nbFaces) {
				throw new IllegalArgumentException();
			}else {
				this.borneMinimale = borneMinimale;
			}
		}catch(IllegalArgumentException ex) {
	        // Create a Logger
	        Logger logger
	            = Logger.getLogger(
	                LoadedDice.class.getName());
	  
	        // Set Logger level()
	        logger.setLevel(Level.WARNING);  
	        logger.warning("Attention borne minimale invalide. Valeur par defaut affectee.");
			this.borneMinimale = borneMinimaleDefaut;
		}
	}
	
	@Override
	public String toString() {
		return super.toString() + ", borne minimale : " + borneMinimale;
	}
	
	@Override
	public int lancer() {		
		// on va passer par la boucle while de toute façon
		int rollScore = 0;
		boolean valeurMinimale = false;
		while (!valeurMinimale) {
			rollScore = super.lancer();
			if (rollScore >= borneMinimale) {
				valeurMinimale = true;
			}
		}
		return rollScore;
	}
}
