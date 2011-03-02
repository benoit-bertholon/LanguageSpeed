public class fibo
{


	static long n = 20;
	static long nmin = 10;
	static long res;


	static  long fibo(long n)
	{
		if (n <= 1) 
			return n;
		return fibo(n-1)+fibo(n-2);
	}
	
	public static void  main(String[] argv)
	{
		n = new Long(argv[0]);
		long t1=0,t2=0;
		double times = 20;
		int i;
		System.out.printf("fibo %d: %d\n",n,fibo(n));
	}


}



