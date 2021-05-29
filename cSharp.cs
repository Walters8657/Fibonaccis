using System;

class Test
{
	public static void Main(string[] args)
	{
		Console.Write("How many numbers do you want? ");
		int num = Convert.ToInt32(Console.ReadLine());
		fib(num);
	}

	static void fib(int n) {
		int f1 = 0, f2 = 1, i;

		if (n < 1 )
			return;
		Console.WriteLine(f1);

		for (i = 1; i < n; i++) {
			Console.WriteLine(f2);
			int next = f1 + f2;
			f1 = f2;
			f2 = next;
		}
	}
}