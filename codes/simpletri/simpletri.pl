#!/usr/bin/perl

#use File::Slurp (read_file);
#my $filein = read_file();
#my $fileout = write_file($ARGV[1]);


#$fibon =  fibo(int());
#print "fibo $ARGV[0]: $fibon\n" ;

sub tri {
	my(@list) = @_;
	my($n) = scalar(@list);
	for ($i = 0 ; $i < $n ; $i++)
	{
		for ($j = $i+1 ; $j < $n ; $j++)
		{
			if (@list[$i] > @list[$j])
			{
				$t = @list[$j];
				@list[$j] = @list[$i];
				@list[$i] = $t;
			}
		}

	}

	return(@list);

}

open $filein , "<" , $ARGV[0];
open $fileout , ">" , $ARGV[1];
my @lines = <$filein>;
@list = ();
 foreach $l (@lines)
 {
  push (@list,int($l));
 }


@list = tri @list;

 foreach $l (@list)
 {
   print $fileout "$l\n";
 }





