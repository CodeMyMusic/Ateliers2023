package exercice1;
import java.util.Random;

public class ManipRob {

	public static void main(String[] args) {
		Robot toto = new Robot("Toto", 10, 20, 3);
		Robot titi = new Robot("Titi");
		
		Random r = new Random();
		
		for (int i = 0; i < 5; i++) {
			toto.modifierOrientation(r.nextInt(4)+1);
			for (int j = 0; j < 5; j++) {
				toto.deplacer();
				System.out.println(toto);
			}
		}
		for (int i = 0; i < 5; i++) {
			titi.modifierOrientation(r.nextInt(4)+1);
			for (int j = 0; j < 5; j++) {
				titi.deplacer();
				System.out.println(titi);
			}
		}

	}

}
