package Exercice1;

public class MemoryDice extends Dice {
	private int lastRollScore;
	
	// CONSTRUCTEUR
	
	public MemoryDice() {
		super();
	}

	public MemoryDice(String name, int nbFaces) {
		super(name, nbFaces);
	}
	
	public MemoryDice(int nbFaces) {
		super(nbFaces);
	}


	public MemoryDice(String name) {
		super(name);
	}
	
	/////
	// METHODES

	public int lancer() {
		// on va passer par la boucle while de toute façon
		int rollScore = 0;
		boolean isSameValue = true;
		while (isSameValue) {
			rollScore = super.lancer();
			if (rollScore != lastRollScore) {
				isSameValue = false;
				lastRollScore = rollScore;
			}
		}
		return rollScore;
	}
}
