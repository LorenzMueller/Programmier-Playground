public class Taschenrechner
{
    private int ergebnis = 0;
    
    public Taschenrechner()
    {
        
    }

    void addieren(int x, int y){
        ergebnis = x + y;
    }
    
    void subtrahieren(int x, int y){
        ergebnis = x - y;
    }
    
    void multiplizieren(int x, int y){
        ergebnis = x*y;
    }
    
    boolean istPositiv(int x){
        if(x>0){
        return true;
        }else{
        return false;
        }
    }
    
    boolean istGerade(int x){
        return (x%2 == 0);
    }
    
    int potenz(int basis, int exponent){
        int ergebnis = 1;
        while(exponent > 0){
            ergebnis = ergebnis * basis;
            exponent--;
        }
        return ergebnis;
    }
}
