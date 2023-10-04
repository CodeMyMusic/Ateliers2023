package exercice2;

public class Test {

	public static void main(String[] args) {
		Vecteur3D v1 = new Vecteur3D(6, 2, 1);
		Vecteur3D v2 = new Vecteur3D(1, 8, 2);
		
		System.out.println("v1 " + v1);
		float res = v1.calculNorme();
		System.out.println("norme " + res);
		System.out.println("v2" + v2);
		res = v2.calculNorme();
		System.out.println("norme " + res);
		
		res = v1.produitScalaire(v2);
		System.out.println("produit scalaire instance v1 v2 " + res);
		res = Vecteur3D.produitScalaire(v1, v2);
		System.out.println("produit scalaire statique v1 v2 " + res);
		Vecteur3D resultat = v1.somme(v2);
		System.out.println("somme instance v1 v2 " + resultat);
		resultat = Vecteur3D.somme(v1, v2);
		System.out.println("somme statique v1 v2 " + resultat);
	}

}
