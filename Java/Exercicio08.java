package Fundamentos;

public class Exercicio08 {

	public static void main(String[] args) {
		int idade = 15;
		boolean AmigoDoDono = true;
		
		if(idade < 18 && AmigoDoDono == false) {
			System.out.println("Não pode entrar");
		} else {
			System.out.println("Pode entrar");
		}
	}
}
