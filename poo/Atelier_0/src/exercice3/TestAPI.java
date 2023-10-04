package exercice3;
import java.math.*;
import java.lang.String;

public class TestAPI {

	public static void main(String[] args) {
		System.out.println(Math.PI);
		System.out.println(Math.random());
		System.out.println((int) Math.random()*3 + 1);
		
		int x1 = 5;
		int x2 = 7;	
		
		System.out.println(Math.max(x1, x2));
		
		String n1 = "totp";
		String n2 = "totp";

		int comparaison_alpha = n1.compareTo(n2);
		if (comparaison_alpha <= 0) {
			System.out.println(n1);
		}else {
			System.out.println(n2);
		}
	}

}
