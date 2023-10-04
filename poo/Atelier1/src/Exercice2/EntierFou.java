package Exercice2;

import java.util.Random;

public class EntierFou extends Entier {
	private int niveauDeFolie;
	
	private Random r = new Random();

	public EntierFou(int valeur, int borneMin, int borneMax, int niveauDeFolie) {
		super(valeur, borneMin, borneMax);
		this.niveauDeFolie = niveauDeFolie;
	}

	public EntierFou(int borneMin, int borneMax, int niveauDeFolie) {
		super(borneMin, borneMax);
		this.niveauDeFolie = niveauDeFolie;
	}

	@Override
	public void increment() {
		int n = r.nextInt(niveauDeFolie) + 1;
		super.increment(n);
	}
	

	@Override
	public String toString() {
		return super.toString() + ", niveau de folie : " + niveauDeFolie;
	}

	
	
}
