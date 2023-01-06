public class day_1 {
    public static void main(String[] args){
        // Read file input
        String[] input = new String[200];
        try {
            File file = new File("2021/day_1_input.txt");
            Scanner scanner = new Scanner(file);
            int i = 0;
            while (scanner.hasNextLine()) {
                input[i] = scanner.nextLine();
                i++;
            }
            scanner.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}