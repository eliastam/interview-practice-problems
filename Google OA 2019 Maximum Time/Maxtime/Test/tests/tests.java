package tests;
import Maxtime.src.*;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class tests {
	 @Test
     public void test1() {
		 assertEquals(Main.maxTime("??:??"), "23:59");
       }
	 
	 @Test
     public void test2() {
		 assertEquals(Main.maxTime("1?:19"), "19:19");
       }
	 @Test
     public void test3() {
		 assertEquals(Main.maxTime("0?:20"), "09:20");
       }
	 @Test
     public void test4() {
		 assertEquals(Main.maxTime("2?:30"), "23:30");
       }
	 
	 @Test
     public void test6() {
		 assertEquals(Main.maxTime("?9:40"), "19:40");
       }
	 @Test
     public void test7() {
		 assertEquals(Main.maxTime("?3:40"), "23:40");
       }
	 @Test
     public void test8() {
		 assertEquals(Main.maxTime("?5:40"), "15:40");
       }
	 @Test
     public void test9() {
		 assertEquals(Main.maxTime("?2:40"), "22:40");
       }
	 
	 
	 @Test
     public void test10() {
		 assertEquals(Main.maxTime("12:4?"), "12:49");
       }
	 @Test
     public void test11() {
		 assertEquals(Main.maxTime("12:??"), "12:59");
       }
	 @Test
     public void test12() {
		 assertEquals(Main.maxTime("12:?2"), "12:52");
       }
	 @Test
     public void test13() {
		 assertEquals(Main.maxTime("12:3?"), "12:39");
       }
	 
	 //test errors 
	 
	 @Test
     public void test14() {
		  try {
			  Main.maxTime("1x:?2");
		   }
		   catch(RuntimeException re){
		      String message = "not number nor ?";
		      assertEquals(message, re.getMessage());
		    }
       }
	 @Test
     public void test15() {
		  try {
			  Main.maxTime("");
		   }
		   catch(RuntimeException re){
		      String message = "Illegal input";
		      assertEquals(message, re.getMessage());
		     		    }
       }
	 @Test
     public void test16() {
		  try {
			  Main.maxTime("12:?");
		   }
		   catch(RuntimeException re){
		      String message = "Illegal input";
		      assertEquals(message, re.getMessage());
		    }
       }
	 @Test
     public void test17() {
		  try {
			  Main.maxTime("123?");
		   }
		   catch(RuntimeException re){
		      String message = "Illegal input";
		      assertEquals(message, re.getMessage());
		    }
       }
	 @Test
     public void test18() {
		  try {
			  Main.maxTime("xx:23");
		   }
		   catch(RuntimeException re){
		      String message = "Illegal input";
		      assertEquals(message, re.getMessage());
		    }
       }
	 
}

