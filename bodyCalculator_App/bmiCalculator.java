package samples;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Hashtable;
import java.util.Scanner;

public class bmiCalculator {

	public static void main(String[] args) {
		double waist;
		double weight;
		double height;
		int option;
		
		System.out.println("Main Menu");
		System.out.println();
			
		
		System.out.println("1. Body Mass Index");
		System.out.println("2. Body Fat Percentage");
		System.out.println();
		
		System.out.println("Select an option: ");
		Scanner sc = new Scanner(System.in);
		option = sc.nextInt();
		
		
		if(option == 1) {
			
			System.out.println("To calculate your Body Mass Index (BMI), enter the following information");
			
			System.out.print("Your weight in pounds: ");
			weight = sc.nextDouble();
			
			System.out.print("Your height in inches: ");
			height = sc.nextDouble();

			System.out.printf("Your BMI is: " + "%.2f", bodyMassIndex(weight, height));
		}
		if(option == 2) {
			
			int gender;
			System.out.println("Select your gender");
			System.out.println("1. Male");
			System.out.println("2. Female");
			gender = sc.nextInt();
			
			
			if(gender == 1) {

				System.out.println("To calculate your Body Fat Percentage, enter the following information");
				System.out.println("Your weight in pounds: ");
				weight = sc.nextDouble();
				
				System.out.println("Your waist measurement in inches: ");
				waist = sc.nextDouble();
				
				System.out.println("Your estimated Body Fat Percentage is: " + maleFat(weight, waist) + "%");
			}
			if(gender == 2){
				
				double bodyweight;
				double wristCircumference;
				double waistCircumference;
				double hipCircumference;
				double forearmCircumference;
				
				System.out.println("Enter your bodyweight in pounds: ");
				bodyweight = sc.nextDouble();

				System.out.println("Enter your wrist circumference in inches: ");
				wristCircumference = sc.nextDouble();
				
				System.out.println("Enter your waist circumference in inches: ");
				waistCircumference = sc.nextDouble();
				
				System.out.println("Enter your hip circumference in inches: ");
				hipCircumference = sc.nextDouble();
				
				System.out.println("Enter your forearm circumference in inches: ");
				forearmCircumference = sc.nextDouble();
				
				System.out.println("Your estimated Body Fat Percentage is: " + femaleFat(bodyweight, wristCircumference, waistCircumference, hipCircumference, forearmCircumference) + "%");

			}
			
			else
				System.out.println("You have entered an invalid option");				
			
			sc.close();
		}
		
		else 
			System.out.println("You have entered an invalid option");
	}



	public static double bodyMassIndex(double yourWeight, double yourHeight) {
		
		double bmi;

		yourWeight = yourWeight * (0.453592);
		yourHeight = yourHeight * (0.0254);
		yourHeight = (yourHeight*yourHeight);
		bmi = yourWeight/yourHeight;
		
		return bmi;	
	}
	
	public static double maleFat(double yourWeight, double yourWaist) {
		
		double weight2;
		double leanBodyMass;
		double bodyFatWeight;
		double bodyFatPercentage;
		
		weight2 = (yourWeight * 1.082) + 94.42;
		yourWaist = yourWaist * 4.15;
		
		leanBodyMass = weight2 - yourWaist;
		bodyFatWeight = yourWeight - leanBodyMass;
		bodyFatPercentage = (bodyFatWeight * 100)/yourWeight;
		BigDecimal bd = new BigDecimal(bodyFatPercentage);
		bd = bd.setScale(1, RoundingMode.HALF_UP);
		bodyFatPercentage = bd.doubleValue();
		
		return bodyFatPercentage;
		
	}
	
	public static double femaleFat(double bodyWeight, double yourWrist, double yourWaist, double yourHip, double yourForearm) {
		
		double bodyweight2;
		bodyweight2 = (bodyWeight * 0.732) + 8.987;
		
		yourWrist = yourWrist/3.14;
		yourWaist = yourWaist * 0.157;
		yourHip = yourHip * 0.249;
		yourForearm = yourForearm * 0.434;
		
		double x = bodyweight2 + yourWrist;
		double y = x - yourWaist;
		double z = y - yourHip;
		double leanBodyMass = yourForearm + z;
		double bodyFatPercentage = ((bodyWeight-leanBodyMass)*100)/bodyWeight;
		
		BigDecimal bd = new BigDecimal(bodyFatPercentage);
		bd = bd.setScale(1, RoundingMode.HALF_UP);
		bodyFatPercentage = bd.doubleValue();
		
		return bodyFatPercentage;
		
	}
	
}


