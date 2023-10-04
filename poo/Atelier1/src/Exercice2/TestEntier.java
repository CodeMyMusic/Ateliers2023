package Exercice2;

public class TestEntier {

	public static void main(String[] args) {
		Entier entier1 = new Entier(5, 10, 20);
		Entier entier2 = new Entier(10, 20);
		Entier entier3 = new Entier(0, 10, 20);
		
		System.out.println("entier 1 : " + entier1);
		System.out.println("entier 2 :" + entier2);
		
		System.out.println("test entier 2 et entier 3 avec equals :" + entier2.equals(entier3));
		System.out.println("test entier 2 et entier 1 avec equals :" + entier2.equals(entier1));
		
		EntierFou entierFou = new EntierFou(0, 300, 10);	
		
		System.out.println(entierFou);
		for (int i = 0; i < 10; i++) {
			entierFou.increment();
			System.out.println(entierFou);
		}
		
		entierFou.increment(10);
		System.out.println("pas pas : " +entierFou);
	}

}
