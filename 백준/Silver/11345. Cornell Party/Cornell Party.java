import java.util.Scanner;

class Main { // 클래스 이름을 Solution에서 Main으로 변경
    private static int[] classifyGuestsByIdFrequency(int numberOfGuests, Scanner scanner) {
        int[] idFrequency = new int[1000001];
        for (int i = 0; i < numberOfGuests; ++i) {
            idFrequency[scanner.nextInt()]++;
        }
        int[] frequencyCount = new int[numberOfGuests + 1];
        for (int i = 0; i < 1000001; ++i) {
            if (idFrequency[i] != 0) frequencyCount[idFrequency[i]]++;
        }
        return frequencyCount;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberOfTestCases = scanner.nextInt();
        for (int testCaseIndex = 0; testCaseIndex < numberOfTestCases; ++testCaseIndex) {
            int numberOfGuests = scanner.nextInt();
            int[] cornellGuestFrequency = classifyGuestsByIdFrequency(numberOfGuests, scanner);
            int[] whiteGuestFrequency = classifyGuestsByIdFrequency(numberOfGuests, scanner);
            boolean frequenciesMatch = true;
            for (int i = 0; i < numberOfGuests + 1; ++i) {
                if (cornellGuestFrequency[i] != whiteGuestFrequency[i]) frequenciesMatch = false;
            }
            if (frequenciesMatch) System.out.println("what a lovely party");
            else System.out.println("you've messed up, Cornell");
        }
    }
}