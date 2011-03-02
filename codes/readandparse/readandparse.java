

import java.io.*;


public class readandparse {



	static long n = 20;
	static long nmin = 10;
	static long res;


	
	public static void  main(String[] argv)
	{
		int i;
		int[] list = new int[0];
		String filename = argv[0];
		String filenameout = argv[1];
		File file = new File(filename);
		FileInputStream fis = null;
		BufferedInputStream bis = null;
		DataInputStream dis = null;

		try {
  
			fis = new FileInputStream(file);
			bis = new BufferedInputStream(fis);
			dis = new DataInputStream(bis);
			BufferedReader br = new BufferedReader(new InputStreamReader(dis));
			String strval ;
			while ((strval = br.readLine()) != null) {
				int [] nlist = new int[list.length +1];
				for (i=0; i < list.length ; i ++)
					nlist[i] = list[i];
				nlist[list.length] = Integer.parseInt(strval); 
				list = nlist;
			}
		} 
		catch (Exception e) {
			e.printStackTrace();
		}		


		try {
			FileWriter fstream = new FileWriter(filenameout);
			BufferedWriter out = new BufferedWriter(fstream);
			for(i=0;i<list.length;i++)
			{
				out.write(String.valueOf( list[i]));
				out.write("\n");
			}
			out.close();
		}
		catch (Exception e) {
			e.printStackTrace();
		}

	}


}



