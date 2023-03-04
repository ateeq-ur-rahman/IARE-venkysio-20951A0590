import java.util.Scanner;

public class recursion {
    public static String rev(String a) {
        if (a.length() == 0) {
            return "";
        } else {
            return rev(a.substring(1)) + a.charAt(0);
        }
        
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String a = scanner.nextLine();
        System.out.println(rev(a));
    }
}
