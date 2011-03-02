#include <stdio.h>
#include <stdlib.h>

void tri(int* list, int size)
{
	int i,j,c=0;
	for(i = 0 ; i < size; i++)
	{
		c =0;
		for(j = i+1 ; j < size; j++)
		{	
			int t;
			if(list[i]> list[j])
			{	t=list[i];
				list[i] = list[j];
				list[j] = t;
				c=1;
			 }
		}
		if (!c)
			return;
	}


}

int main(int argc , char * argv[])
{
	FILE *fichier;
	FILE *fichierout;

	fichier = fopen(argv[1],"r");
	fichierout = fopen(argv[2],"w");
	int * unsortedlist;
	int size;
	int value = -1;
	char str[20] ;
	int i = 0;
	while(!feof(fichier))
	{
		if( i+1< 20)
			str[i++] = fgetc(fichier);
		else 
			exit(1);
		if(str[i-1] == '\n')
		{
			str[i] = 0;
			unsortedlist = (int*)realloc(unsortedlist,sizeof(int)*(++size));
			unsortedlist[size-1]=atoi(str);
			i = 0;
		}
	}


	for ( i = 0 ; i < size;i++)
		fprintf(fichierout,"%d\n",unsortedlist[i]);
	fclose(fichierout);


	return 0;


}








