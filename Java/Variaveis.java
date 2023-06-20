package Fundamentos;

public class Variaveis {
	
	public static void main(String[] args) {
		int x = 10;
		//Primeiro print o valor depois soma
		System.out.println(x++); // 10(11)
		//Primeiro soma depois print
		System.out.println(++x); // 12
		System.out.println(x--); // 12(11)
		System.out.println(--x); // 10
	}
}
