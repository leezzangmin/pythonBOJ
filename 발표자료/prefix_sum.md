 
### 누적합
<br>

* 누적합은 DP의 일종
* 연속적으로 나열된 숫자의 합을 구하는 데 효율적
* brute force 식으로 합을 구한다면 O(N*M)
* 누적합으로 합을 구한다면 (전처리 N + 계산횟수 M)  = O(N+M) 단, 메모리 복잡도가 상승

<br><br><br><br>
* * *
<br><br><br>
   
  

![image](https://user-images.githubusercontent.com/64303390/158129456-98ace4be-3053-427d-a357-c9f41f13cfee.png)

<br>

```
temp_list = [10, 20, 30, 40, 50]
prefix_sum = [0] * (len(temp_list) + 1)

for i in range(1, len(temp_list)):
    prefix_sum[i] = temp_list[i-1] + prefix_sum[i-1]

```

```
import java.io.*;
import java.util.Arrays;

public class BOJ_2512_예산 {
    static int N, M;
    static int[] budgets;

    public static void main(String[] args) {
        try {
            input();
            solve();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void solve() {
        int L = 0, R = 1_000_000_000, answer = 0;

        if (Arrays.stream(budgets).sum() <= M) {
            answer = Arrays.stream(budgets).max().getAsInt();
            System.out.println(answer);
            return ;
        }

        Arrays.sort(budgets);
        binarySearch(L, R, answer);
    }

    private static void binarySearch(int L, int R, int answer) {
        while(L <= R) {
            int mid = (L + R) / 2;
            if (determination(mid)) {
                answer = mid;
                L = mid + 1;
            } else {
                R = mid - 1;
            }
        }

        System.out.println(answer);
    }

    private static boolean determination(int value) {
        long sum = 0;

        for (int i = 0; i < N; i++) {
            if (budgets[i] >= value) {
                sum += value;
            } else {
                sum += budgets[i];
            }
        }

        return sum <= M;
    }

    private static void input() throws IOException {
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedReader br = new BufferedReader(new FileReader(new File("/Users/woo-jinpark/Desktop/Park/05_Test/input/input.txt")));

        N = Integer.parseInt(br.readLine());
        budgets = new int[N];

        String[] split = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            budgets[i] = Integer.parseInt(split[i]);
        }

        M = Integer.parseInt(br.readLine());
    }
}
```