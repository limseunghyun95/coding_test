import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.stream.Collectors;

public class p11866 {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int k = scan.nextInt();

        Queue<Integer> queue = new LinkedList<>();

        // Queue 초기화
        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }

        // 순회
        int cnt = 0;
        ArrayList<Integer> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            int value = queue.poll();
            cnt += 1;
            if (cnt == k) {
                cnt = 0;
                result.add(value);
                continue;
            }
            queue.add(value);
        }

        String stringResult = result.stream().map(Object::toString).collect(Collectors.joining(", "));
        System.out.printf("<%s>", stringResult);

    }
}
