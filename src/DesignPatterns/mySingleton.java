package DesignPatterns;

public class mySingleton {

	private static mySingleton myObject; //PRIVATE OBJECT
	
	private  mySingleton(){
		// PRIVATE CONSTRUCTOR
	}
	
	public static mySingleton getInstance(){
		if(myObject == null){
			myObject = new mySingleton();
			return myObject;
		}
		else{
			System.out.println("Only One Instance is allowed !!");
		}
		
		return null;
	}
	
	public void forExample(){
		System.out.println("This is just an example of the singleton class !!");
	}
	
	public static void main(String[] args){
		
		mySingleton singleton = mySingleton.getInstance();
		singleton.forExample();
		mySingleton singleton1 = mySingleton.getInstance();
		//singleton1.forExample();
	}
}
