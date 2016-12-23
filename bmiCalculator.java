package samples;

import java.util.Scanner;

public class bmiCalculator {

	public static void main(String[] args) {
		double weight;
		double height;
		double bmi;
		System.out.println("To calculate your Body Mass Index (BMI), please enter the following information");
		
		System.out.print("Your weight in pounds: ");
		Scanner sc = new Scanner(System.in);
		weight = sc.nextDouble();
		weight = weight * (0.453592);
		
		System.out.print("Your height in inches: ");
		height = sc.nextDouble();
		sc.close();
		
		height = height * (0.0254);
		height = (height*height);
		bmi = weight/height;
		
		System.out.printf("Your BMI is: " + "%.2f", bmi);
		
		
		
		
		
		
		
		

	}

}
