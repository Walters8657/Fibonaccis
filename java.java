import java.util.Scanner; //Import for user import int

class java {
    public static void fib(int n) {
        int f1 = 0;
        int f2 = 1;
        int i = 1;

        if (n < 1) {
            return;
        }

        System.out.println(f1);

        while (i < n) {
            System.out.println(f2);
            int next = f1 + f2;
            f1 = f2;
            f2 = next;
            i++;
        }
    }

    public static void main(String[] args) {

        System.out.print("How many numbers do you want? ");

        Scanner in = new Scanner(System.in); //User input variable
        int num = in.nextInt();

        fib(num);
    }
}