package ArraysAndString;

import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

import javax.print.attribute.standard.RequestingUserName;

public class ParenthesisMatching {
	
	public static boolean compareParenthesis(String input){
		
		Stack<Character> parenthesis = new Stack<Character>();
		for(int i=0 ; i<input.length() ; i++){
			if(input.charAt(i) == '('){
				parenthesis.push('(');
			}
			else if(input.charAt(i) == '{'){
				parenthesis.push('{');
			}
			else if(input.charAt(i) == '['){
				parenthesis.push('{');
			}
			else if(input.charAt(i) == ')'){
				if(parenthesis.isEmpty()){
					return false;
				}
				else if(parenthesis.pop() != '('){
					return false;
				}
			}
			else if(input.charAt(i) == '}'){
				if(parenthesis.isEmpty()){
					return false;
				}
				else if(parenthesis.pop() != '{'){
					return false;
				}
			}
			else if(input.charAt(i) == ']'){
				if(parenthesis.isEmpty()){
					return false;
				}
				else if(parenthesis.pop() != ']'){
					return false;
				}
			}
		}
		return parenthesis.isEmpty();
	}
	
	
	
	public static void main (String[] args){
		Scanner scanInput = new Scanner(System.in);
		String scanIn = scanInput.next();
		boolean value = compareParenthesis(scanIn);
		System.out.println(value);
	}
}
