package Exercice1;

public class LoadedDice extends Dice {
	private final int borneMinimale;
	
	public int getBorneMinimale() {
		return borneMinimale;
	}

	public LoadedDice(String name, int nbFaces, int borneMinimale) {
		super(name, nbFaces);
		if (borneMinimale < 1) {
			throw new IllegalArgumentException("La borne minimale ne peut etre nulle");
		}else {
			this.borneMinimale = borneMinimale;
		}
	}
	
	@Override
	public String toString() {
		return super.toString() + ", borne minimale : " + borneMinimale;
	}
	
	@Override
	public int lancer() {
		return super.lancer() + borneMinimale;
	}
}
