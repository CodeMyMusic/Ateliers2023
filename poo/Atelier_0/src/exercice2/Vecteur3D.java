package exercice2;
import java.text.DecimalFormat;

public class Vecteur3D {
	private int x;
	private int y;
	private int z;
	public Vecteur3D(int x, int y, int z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	public Vecteur3D() {
		this(0, 0, 0);
	}
	
	@Override
	public String toString() {
		DecimalFormat df = new DecimalFormat("#0.00");
		return "<"+df.format(x) + " " + df.format(y) + ", " + df.format(z) + ">";
	}
	
	public float calculNorme() {
		return (float) Math.sqrt(x*x + y*y + z*z);
	}
	
	public float produitScalaire(Vecteur3D v) {
		return x*v.x + y*v.y + z*v.z;
	}
	
	public static float produitScalaire(Vecteur3D a, Vecteur3D b) {
		return a.produitScalaire(b);
	}
	
	public Vecteur3D somme(Vecteur3D v) {
		return new Vecteur3D(x + v.x, y + v.y, z + v.z);
	}
	
	public static Vecteur3D somme(Vecteur3D a, Vecteur3D b) {
		return a.somme(b);
	}
	
	
}
