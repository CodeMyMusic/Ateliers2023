package exercice1;

public class Robot {
	private String ref;
	private String nom;
	
	private int x;
	private int y;
	
	private static final int NORD = 1;
	private static final int EST = 2;
	private static final int SUD = 3;
	private static final int OUEST = 4;
	
	private int orientation;
	
	public static int nbRobots = 1;
	
	public Robot(String nom, int x, int y, int orientation) {
		this.ref = "ROB" + nbRobots;
		this.nom = nom;
		this.x = x;
		this.y = y;
		this.orientation = orientation;
		
		nbRobots++;
	}
	public Robot(String nom) {
		this(nom, 0, 0, NORD);
		
	}
	public void modifierOrientation(int orientation) {
		this.orientation = orientation;
	}
	
	public void deplacer() {
		if (orientation == SUD && y > 0) {
			y --;
		}else if (orientation == OUEST && x > 0){
			x --;
		}else if (orientation == EST) {
			x ++;
		}else {
			y ++;
		}
	}
	
	@Override
	public String toString() {
		return "nom "+ nom + " ref " 
				+ ref + " coordonnees " + x + " " 
				+ y + " direction " 
				+ orientationToString(orientation);
	}
	
	// OULALA c koa ça ?
	private static String orientationToString(int nbOrientation) {
		String orientationString;
		switch (nbOrientation) {
			case 1:
				orientationString = "nord";
				break;
			case 2:
				orientationString = "est";
				break;
			case 3:
				orientationString = "sud";
				break;
			case 4:
				orientationString = "ouest";
				break;
			default:
				orientationString = "5ème dimension no way";
		}
				
		return orientationString;
	}
	
}
