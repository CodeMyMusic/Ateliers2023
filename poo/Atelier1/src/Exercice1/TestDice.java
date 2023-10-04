package Exercice1;
import java.util.ArrayList;

public class TestDice {

	public static void main(String[] args) {
		int nbDices = Dice.getNbDices();
		System.out.println("Nombre total de des : " + nbDices);
		
		Dice de1 = new Dice();
		Dice de2 = new Dice(119);
		
		nbDices = Dice.getNbDices();
		System.out.println("Nombre total de des : " + nbDices);
		
		System.out.println("lance de numero 1: " + de1.lancer());
		System.out.println("lance de numero 2: " + de2.lancer(3));

		
		// GESTION ERREURS
		Dice diceNotValid = new Dice("jon", 2);
		
		//l'erreur a été gérée si le nombre de faces passe à 6
		System.out.println("nb faces passe a 6 pour nb faces non valide : " + diceNotValid);
		
		//DE PIPE
		
		LoadedDice depipe = new LoadedDice("Jacques", 15, 1);
		System.out.println("de pipe description: " + depipe);
		System.out.println("de pipe lance : " + depipe.lancer());
		
		depipe = new LoadedDice("Jean", 15, 14);
		
		System.out.println("de pipe v2, lance : " + depipe.lancer());
		
		LoadedDice depipe2 = new LoadedDice("Jean", 15, 16);
		
		System.out.println("de pipe non valide :" + depipe2);
		
		LoadedDice depipe3 = new LoadedDice("Joseph", 15, 0);
		
		System.out.println("de pipe non valide v2 :" + depipe3);
		
		/////
		
		MemoryDice deMemoire = new MemoryDice();
		System.out.println("De memoire description :" + deMemoire);
		
		ArrayList<Integer> scoresDeMemoire = new ArrayList<Integer>();
		ArrayList<Integer> scoresDeNormal = new ArrayList<Integer>();
		for (int i = 0; i < 30; i++) {
			scoresDeMemoire.add(deMemoire.lancer());
			scoresDeNormal.add(de1.lancer());
		}
		System.out.println("de memoire multiples lances : " + scoresDeMemoire);
		System.out.println("de normal multiples lances : " + scoresDeNormal);
		
		// TEST EGAL ET EQUALS (MEMES VALEURS)
		
		Dice deSame = new Dice("Jean", 10);
		Dice deSame2 = new Dice("Jean", 10);
		
		System.out.println("memes valeurs test equals : " + deSame.equals(deSame2));
		System.out.println("memes valeurs test equals (inverse) : " + deSame2.equals(deSame));
		
		System.out.println("memes valeurs test avec egal :" + (deSame == deSame2));
		
		////
		// TEST NOMS DIFFERENTS EQUALS
		
		deSame = new Dice("Jeam", 10);
		deSame2 = new Dice("Jean", 10);
		
		System.out.println("pas meme nom test equals : " + deSame.equals(deSame2));
		System.out.println("pas meme nom test equals (inverse) : " + deSame2.equals(deSame));
		
		// TEST NB FACES DIFFERENTES EQUALS
		
		deSame = new Dice("Jean", 11);
		deSame2 = new Dice("Jean", 10);
		
		System.out.println("pas meme nb faces test equals : " + deSame.equals(deSame2));
		System.out.println("pas meme nb faces equals (inverse) : " + deSame2.equals(deSame));
		
		// DÉS AUTRES FACES
		ArrayList<Object> mesFaces = new ArrayList<Object>();
		for (int i = 0; i < 100; i++) {
			mesFaces.add(i * 2);
			mesFaces.add("coucou");
		}
		PolymorphDice polyDe = new PolymorphDice(mesFaces);
		System.out.println(polyDe);

	}

}
