
#include <stdio.h>
#include <stdlib.h>


int fibo(long n)
{
	if (n <= 1) 
		return n;
	else 
		return fibo(n-1)+fibo(n-2);


}

/*int fibo2(long n){*/

/*deb:*/
/*	if( n<=1 )*/
/*	{*/
/*		r = n;*/
/*		goto ret;*/
/*	}*/
/*	else*/
/*	{*/
/*		c = n-1;*/
/*		goto deb;*/
/*		g*/
/*	}*/


/*}*/

int main(int argc, char * argv[])
{
	long n=0;
	if (argc >1) 
		n = atoi(argv[1]);
	printf("fibo %d: %d\n",n,fibo(n));

}




