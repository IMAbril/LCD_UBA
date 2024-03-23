package aed;

class Funciones {
    int cuadrado(int x) {
        // COMPLETAR
        int res;
        res = x*x ;
        return res;
    }

    double distancia(double x, double y) {
        // COMPLETAR
        double res; 
        res = Math.sqrt(x*x + y*y) ;
        return res;
    }

    boolean esPar(int n) {
        // COMPLETAR
        boolean par ;
        if (n%2 == 0) {
            par = true;
        } else {
            par = false;
        }
        return par;
    }

    boolean esBisiesto(int n) {
        // COMPLETAR
        boolean bisiesto;
        if ((n%4==0 && n%100 != 0) || (n%400==0)) {
            bisiesto = true;
        } else {
            bisiesto = false;
        }
        return bisiesto;
    }

    int factorialIterativo(int n) {
        // COMPLETAR
        int fact=1;
        for (int i = 1; i <= n; i++ ){
            fact *= i;
        } 
        return fact;
    }

    int factorialRecursivo(int n) {
        // COMPLETAR
        int fact;
        if (n > 0) {
            fact = n * factorialRecursivo(n-1);
        } else {
            fact = 1;
        }

        return fact;
    }

    boolean esPrimo(int n) {
        // COMPLETAR
        int cantDiv = 0;
        for (int i = 0; i<=n+1; i++){
            if (cantDiv > 2 || n == 0 || n==1){
                return false;
            }
            if (i!=0 && n%i == 0) {
                cantDiv += 1;
            }
        }
        return true;
    }

    int sumatoria(int[] numeros) {
        // COMPLETAR
        int res = 0;
        for (int x : numeros) {
            res += x;
        }
        return res;
    }

    int busqueda(int[] numeros, int buscado) {
        // COMPLETAR
        for (int i = 0; i < numeros.length; i++){
            if (numeros[i] == buscado) {
                return i;
            }
        }
        return 0;
    }

    boolean tienePrimo(int[] numeros) {
        // COMPLETAR
        for (int x : numeros) {
            if (esPrimo(x)) {
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        // COMPLETAR
        for (int x: numeros) {
            if (x%2 != 0) {
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        // COMPLETAR
        if (s1.length() > s2.length()){
            return false;
        }
        for (int i=0; i < Math.min(s1.length(), s2.length());i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                return false;
            } 
        }
        return true;
    }

    boolean esSufijo(String s1, String s2) {
        // COMPLETAR
        if (s1.length() > s2.length()){
            return false;
        }

        int diff = s2.length() - s1.length();
        for (int i= s1.length()-1 ; i >= 0 ; i--){
            if (s1.charAt(i) != s2.charAt(i+diff)) {
                return false;
            }
        }             
        return true;
    }
}
