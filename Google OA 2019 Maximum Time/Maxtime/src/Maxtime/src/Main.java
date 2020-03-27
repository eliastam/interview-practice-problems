package Maxtime.src;
public class Main {
public static void main(String[] args) {
System.out.println(maxTime("??:?4"));
    
}
public static String maxTime(String time) {
	String max1 = maxHour(time);
	if(max1.charAt(3) == '?') {
		String s = "";
		max1 = max1.substring(0,3) + "5" + String.valueOf(time.charAt(4));
	}
	if(max1.charAt(4) == '?') {
		String s = "";
		max1 = max1.substring(0,4) + "9";
	}
	
	return max1;
	
}
public static String maxHour(String time) {
	if (time == null) {
		throw new IllegalArgumentException("Illegal input");
	}
	if(time.length() < 5) {
		throw new IllegalArgumentException("Illegal input");
	}
	if(time.charAt(2)!= ':') {
		throw new IllegalArgumentException("Illegal input");
	}
	if(time.charAt(0) == '?' && time.charAt(1)=='?') {
		String s = "";
		s += "23" + time.substring(2);
		return s;
	}
	if(time.charAt(0) == '?') {
		if(time.charAt(1) > '9' || time.charAt(1) < '0' ) {
			  throw new IllegalArgumentException("not number nor ?");
		}
		int x =Integer.parseInt(String.valueOf( time.charAt(1)) );
		if (x > 3) { //? = 1
			String s = "1" + time.substring(1);
			return s;
		}else { // ? = 2
			String s = "2" + time.substring(1);
			return s;
		}
	}
	if(time.charAt(1) == '?') {
		if(time.charAt(0) > '9' || time.charAt(0) < '0' ) {
			  throw new IllegalArgumentException("not number nor ?");
		}
		int x =Integer.parseInt(String.valueOf( time.charAt(0)) );
		if (x < 2) { //? = 9
			String s = String.valueOf(time.charAt(0))+"9" + time.substring(2);
			return s;
		}else { // ? = 3
			String s = String.valueOf(time.charAt(0))+"3" + time.substring(2);
			return s;
		}
	}
	return time;
	
}
}
