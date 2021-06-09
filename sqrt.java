public class Main {

    public static final int precision = 10; // how many decimal points

    public static void main(String[] args){
        System.out.println(sqrt(13));
    }

    public static double sqrt(int number){
        int start = 0;
        int end = number;

        double result = 0; // it wants me to initialize it

        // we first need to find roughly what number it is
        // (i adapted this binary search a bit to work with square roots
        while(start<=end){
            int midpoint = (start+end)/2;

            int squared = midpoint*midpoint; // there probably is a better way to square it but whatever

            if(squared == number){
                // we found it!
                return(midpoint);
            }
            else if(squared<number){
                start = midpoint+1;
                result = midpoint; // just in case it doesn't run again (considering we increment up when doing precision)
            }
            else{
                end = midpoint-1;
                // don't change result here
            }
        }

        // now we add with precision (decimal places)
        double increment = 0.1;

        for(int i=0;i<precision;i++){
            while(result*result<number){
                result += increment; // keep incrementing the decimal point until it can't anymore
            }
            // currently, result^2 WILL BE greater than number, since it checks, then increments. to fix this, we subtract the result with increment
            result -= increment;
            // as we prepare to go to the next decimal point, we have to divide increment by 10 so it can work correctly with the next decimal point
            increment /= 10;
        }
        // there are some issues with java automatically rounding my number due to like floating point issues, so i just round it rq

        int multiplier;

        multiplier = (int) Math.pow(10,precision); // intelij added the (int) for me (which i also learned with some reading) which apparently converts it into an integer so the ide wont throw a fit :|

        result = Math.floor(result*multiplier)/multiplier;

        return (result);
    }
}
