import java.util.*;
import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Busqueda_Genoma {
    public static void buscar(File file, String txt) throws IOException{

        File[] tab = file.listFiles();
        List lines = new ArrayList();
        boolean result, show;

        for(File current : tab){
            if(current.isFile()) {
                show = false;
                String cadena;
                String fileName = current.getAbsolutePath();
                FileReader f = new FileReader(fileName);
                BufferedReader b = new BufferedReader(f);
                while((cadena = b.readLine())!=null){
                    result = cadena.contains(txt);
                    if(result){
                        lines.add(cadena);
                        show = true;
                    }
                }
                b.close();
                if(show){
                    System.out.println(fileName);
                    for(Object line : lines){
                        System.out.println(line);
                    }
                }
                }
            else if(current.isDirectory()){
                buscar(current, txt);
            }
        }
    }

    public static void main(String[] argv) throws IOException{
        File file = new File("C:/Users/sergi/Desktop/misia/social_computing/genomas/genomas");
        String txt = "wax synthase";
        buscar(file, txt);
    }
}