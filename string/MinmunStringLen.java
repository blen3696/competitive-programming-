public class MinmunStringLen {
    public static int max(String str){
        StringBuilder S = new StringBuilder(str);
        int i = 0;
        while (i< S.length()-1) {
            if (S.charAt(i) == 'A' && S.charAt(i + 1) == 'B') {
                S.delete(i, i + 2); //we loop through the entire string and  Remove 'A' and 'B' or 'C' and 'D' if they exist
                i = 0;              // reinitialize i to 0 because there is sifiting occured
                
            }  
            if (S.charAt(i) == 'C' && S.charAt(i + 1) == 'D') {
                S.delete(i, i + 2); // Remove 'A' and 'B'
                i = 0;
                
            }  
            i++;
        }
        int  k = S.length(); // then we return the length of the remaning string
        return k;
    }
    public static void main(String[] args) {
        String  str = "ACBBD";
        System.out.println(max(str));
    }
}
