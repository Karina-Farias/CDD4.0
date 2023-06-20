package Fundamentos;

import java.util.Scanner;

public class Exercicio10_PositivoOuNegativo {

	public static void main(String[] args) {
		Scanner Numero = new Scanner(System.in);
		System.out.println("Digite um numero:");
		int resp = Numero.nextInt();
		
		if (resp >= 0) {
			System.out.println("Positivo");
		} else {
			System.out.println("Negativo");
		}
	}
}
