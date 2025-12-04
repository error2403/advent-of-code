/*
The newly-improved calibration document consists of lines of text; each
line originally contained a specific calibration value that the Elves now
need to recover. On each line, the calibration value can be found by
combining the first digit and the last digit (in that order) to form a
single two-digit number.
*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class day_1_trebuchet {

    public static void main (String[] args) {
        try {
            int sum = 0;
            Scanner scanner = new Scanner(new File("calibration_document.txt"));

            while (scanner.hasNextLine()) {
                    int temp = getCalibrationValue(scanner.nextLine());
                    //System.out.println(temp);
                    sum += temp;
            }

            System.out.println(sum);
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }


    public static ArrayList<Integer> extractDigits(String line) {
        ArrayList<Integer> calibrationValues = new ArrayList<Integer>();

        for (char c : line.toCharArray()) {
            if (Character.isDigit(c)) {
                calibrationValues.add(Integer.parseInt(Character.toString(c)));
            }
        }

        return calibrationValues;
    }

    public static int getCalibrationValue(String line) {
        ArrayList<Integer> temp = extractDigits(line);

        int first = temp.get(0);
        int last = temp.get(temp.size() - 1);

        String firstChar = Integer.toString(first);
        String lastChar = Integer.toString(last);

        return Integer.parseInt(firstChar + lastChar);
    }
}