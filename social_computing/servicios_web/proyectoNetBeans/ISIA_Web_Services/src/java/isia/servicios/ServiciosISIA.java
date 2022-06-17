package isia.servicios;

import java.awt.BorderLayout;
import java.awt.Frame;
import java.awt.Graphics;
import java.io.File;
import java.io.IOException;
import static java.lang.Thread.sleep;
import java.nio.file.Files;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import processing.core.PFont;
import processing.core.PVector;
import wordcram.Colorers;
import wordcram.Word;
import wordcram.WordAngler;
import wordcram.WordCram;
import wordcram.WordPlacer;

/**
 *
 * @author galvez
 */
public class ServiciosISIA {

    public static final String NIF_STRING_ASOCIATION = "TRWAGMYFPDXBNJZSQVHLCKE";

    /**
     * Devuelve un NIF completo a partir de un DNI. Es decir, añade la letra del
     * NIF. Procede de la Wikipedia.
     *
     * @param dni dni al que se quiere añadir la letra del NIF
     * @return NIF completo.
     */
    public static void main(String[] args) {

        File sal = new File("sal.jpg");
        try {
            Files.write(sal.toPath(), nubeEtiquetas("http://es.wikipedia.org/wiki/Lenin"));
        } catch (IOException ex) {
            ex.printStackTrace();
        }

    }

    public static char letraDNI(int dni) {
        return NIF_STRING_ASOCIATION.charAt(dni % 23);
    }

    static MotorDeCloudTag embed = new MotorDeCloudTag();
    public static byte[] nubeEtiquetas(String URL) {
        byte[] fileContent = new byte[100];
        System.out.println("Retornando...\n");
        try {
            File fi = new File(MotorDeCloudTag.fichero);
            if (fi.exists()) Files.delete(fi.toPath());
            embed.setURL(URL);
            embed.draw();
            int i=0;
            while (!fi.canRead()) {
                sleep(1000);
                if (++i == 30) throw new Exception("Tiempo agotado.");
                System.out.println("Durmiendo...\n");
            }
            fileContent = Files.readAllBytes(fi.toPath());
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return fileContent;
    }

}
