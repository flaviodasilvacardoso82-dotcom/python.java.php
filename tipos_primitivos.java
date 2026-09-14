import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class tipos_em_java {
    public static void main(String[] args) {

        System.out.println("ola mundo ");

       
        List<Object> lista = new ArrayList<>();

        lista.add(1);       
        lista.add("e");     
        lista.add(null);    
        lista.add(0.0);     
        lista.add(true);    
        System.out.println(lista)
        for (Object valor : lista) {
            if (valor == null) {
                System.out.println("null");
            } else {
                // Equivalente aproximado a type() do Python
                System.out.println(valor.getClass().getSimpleName());
            }
        }


        Boolean v = null;
        if (Boolean.TRUE.equals(v)) {
            System.out.println("True");
        } else {
            System.out.println("false");
        }

        List<Integer> lis = new ArrayList<>();

        for (int numero = 0; numero <= 10; numero++) {
            lis.add(numero);
        }

        System.out.println(lis);
    }
}