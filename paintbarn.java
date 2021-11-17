// import java.io.BufferedReader;
// import java.io.FileReader;
// import java.io.FileWriter;
// import java.io.IOException;
// import java.io.InputStream;
// import java.io.InputStreamReader;
// import java.io.OutputStream;
// import java.io.PrintWriter;
// import java.util.Arrays;
// import java.util.StringTokenizer;

// //Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=919 


// public class paintbarn {
//     public static void main(String[] args) throws IOException {
//         Kattio reader = new Kattio("paintbarn");
//         int N = reader.nextInt();
//         int K = reader.nextInt();
//         int maxX = 0;
//         int maxY = 0;
//         int[][] rects = new int[N][4];
//         int perfectSquares = 0;

//         for (int i = 0; i < N; i++) {
//             rects[i][0] = reader.nextInt();
//             rects[i][1] = reader.nextInt();
//             rects[i][2] = reader.nextInt() - 1;
//             rects[i][3] = reader.nextInt() - 1;
//             maxX = Math.max(maxX, rects[i][2]);
//             maxY = Math.max(maxY, rects[i][3]);
//         }
//         int[][] coats = new int[maxY + 1][maxX + 1];
//         for ( int i = 0; i < N; i++) {
//             for (int y = maxY - rects[i][1]; y >= maxY - rects[i][3]; y--) {
//                 for (int x = rects[i][0]; x <= rects[i][2]; x++) {
//                     coats[y][x]++;
//                 }
//             }
//             // paintCoats(coats);
//             // System.out.println();
//         }

//         for (int y = 0; y < maxY + 1; y++) {
//             for (int x = 0; x < maxX + 1; x++) {
//                 if (coats[y][x] == K) {
//                     perfectSquares++;
//                 }
//             }
//         }
//         reader.println(perfectSquares);
//         reader.close();
//     }

//     public static void paintCoats(int[][] coats) {
//         for (int i = 0; i < coats.length; i++) {
//             System.out.println(Arrays.toString(coats[i]));
//         }
//     }
//     static class Kattio extends PrintWriter {
//         private BufferedReader r;
//         private StringTokenizer st;
    
//         // standard input
//         public Kattio() { this(System.in, System.out); }
//         public Kattio(InputStream i, OutputStream o) {
//             super(o);
//             r = new BufferedReader(new InputStreamReader(i));
//         }
//         // USACO-style file input
//         public Kattio(String problemName) throws IOException {
//             super(new FileWriter(problemName + ".out"));
//             r = new BufferedReader(new FileReader(problemName + ".in"));
//         }
    
//         // returns null if no more input
//         public String next() {
//             try {
//                 while (st == null || !st.hasMoreTokens())
//                     st = new StringTokenizer(r.readLine());
//                 return st.nextToken();
//             } catch (Exception e) { }
//             return null;
//         }
    
//         public int nextInt() { return Integer.parseInt(next()); }
//         public double nextDouble() { return Double.parseDouble(next()); }
//         public long nextLong() { return Long.parseLong(next()); }
//     }
// }
import java.util.*;
import java.io.*;

public class paintbarn {
	static final int WIDTH = 9;
	public static void main(String[] args) throws IOException {
		Kattio io = new Kattio("paintbarn");
		int rectNum = io.nextInt();
		int paintReq = io.nextInt();
		int[][] barn = new int[WIDTH + 1][WIDTH + 1];

		for (int i = 0; i < rectNum; i++) {
			int start_x = io.nextInt();
			int start_y = io.nextInt();
			int end_x = io.nextInt();
			int end_y = io.nextInt();

			// Set up the prefix sums array with all the corners of the given rectangle
			barn[start_x][start_y]++;
			barn[end_x][end_y]++;
			barn[start_x][end_y]--;
			barn[end_x][start_y]--;
		}

		int valid_area = 0;
		// Run 2D prefix sums on the array
		for (int x = 0; x <= WIDTH; x++) {
			for (int y = 0; y <= WIDTH; y++) {
				if (x > 0) barn[x][y] += barn[x - 1][y];
				if (y > 0) barn[x][y] += barn[x][y - 1];
				if (x > 0 && y > 0) barn[x][y] -= barn[x - 1][y - 1];
				if (barn[x][y] == paintReq) {
					valid_area++;
				}
				paintCoats(barn);
			}
		}
		io.println(valid_area);
		io.close();
	}
    public static void paintCoats(int[][] coats) {
        for (int i = 0; i < coats.length; i++) {
			for (int j = 0; j < coats[i].length; j++) {
				if (coats[i][j] >= 0) {
					System.out.print(' ');
				}
				System.out.print(coats[i][j]);
				System.out.print(',');
			}
			System.out.println();
        }
        System.out.println();
    }

	//BeginCodeSnip{Kattio}
	static class Kattio extends PrintWriter {
		private BufferedReader r;
		private StringTokenizer st;
	
		// standard input
		public Kattio() { this(System.in, System.out); }
		public Kattio(InputStream i, OutputStream o) {
			super(o);
			r = new BufferedReader(new InputStreamReader(i));
		}
		// USACO-style file input
		public Kattio(String problemName) throws IOException {
			super(new FileWriter(problemName + ".out"));
			r = new BufferedReader(new FileReader(problemName + ".in"));
		}
	
		// returns null if no more input
		public String next() {
			try {
				while (st == null || !st.hasMoreTokens())
					st = new StringTokenizer(r.readLine());
				return st.nextToken();
			} catch (Exception e) { }
			return null;
		}
	
		public int nextInt() { return Integer.parseInt(next()); }
		public double nextDouble() { return Double.parseDouble(next()); }
		public long nextLong() { return Long.parseLong(next()); }
	}
	//EndCodeSnip
}