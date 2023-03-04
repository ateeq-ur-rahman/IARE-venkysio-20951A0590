public class multithread {

    public static void main(String[] args) {
        String originalString = "Hello, world!";
        System.out.println("Original string: " + originalString);

        ReverseStringThread reverseStringThread = new ReverseStringThread(originalString);
        Thread thread = new Thread(reverseStringThread);
        thread.start();
    }

    static class ReverseStringThread implements Runnable {
        String originalString;

        public ReverseStringThread(String originalString) {
            this.originalString = originalString;
        }

        public void run() {
            String reversedString = new StringBuilder(originalString).reverse().toString();
            System.out.println("Reversed string: " + reversedString);
        }
    }
}
