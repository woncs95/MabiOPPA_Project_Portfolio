public class chess {
    static boolean changeTurn(boolean Turn) {
        Turn = !Turn;
        return (Turn);
    }

    public static void main(String[] args) {
        boolean currentTurn = false;
        for (int i = 0; i < 10; i++) {
            currentTurn = changeTurn(currentTurn);
            System.out.println(currentTurn);
        }
    }
}