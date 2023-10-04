package Exercice2;


public class Entier {
	private int valeur;
	private int borneMin;
	private int borneMax;

	public int getBorneMin() {
		return borneMin;
	}

	public int getBorneMax() {
		return borneMax;
	}

	public Entier(int valeur, int borneMin, int borneMax) {
		this.valeur = valeur;
		this.borneMin = borneMin;
		this.borneMax = borneMax;
	}
	
	public Entier(int borneMin, int borneMax) {
		this(0, borneMin, borneMax);
	}
	
	public void increment() {
		if (valeur < borneMax - 1) {
			valeur++;
		}
	}
	
	public void increment(int n) {
		for (int i = 0; i < n; i++) {
			increment();
		}
	}

	@Override
	public boolean equals(Object obj) {
		boolean equals = false; 
		 
        // Si l'objet est comparé avec lui-même 
        if (obj == this) {
            equals = true;
        }else {
            // On regarde si l'objet est instance de Dice
            if ((obj instanceof Entier)) {
                // on caste vers Dice pour comparer
                Entier entier = (Entier) obj;
                 
                equals = (valeur == entier.valeur) && 
                (borneMin == entier.borneMin) 
                && (borneMax == entier.borneMax);
            }
        }
         
        return equals;
	}

	@Override
	public String toString() {
		return "Valeur : " + valeur + ", borneMin : " 
	+ borneMin + ", borne max :" + borneMax;
	}
	
	
}
