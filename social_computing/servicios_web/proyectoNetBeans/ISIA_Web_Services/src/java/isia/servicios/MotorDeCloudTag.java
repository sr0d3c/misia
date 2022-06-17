package isia.servicios;


import java.awt.Color;
import java.awt.Frame;
import java.awt.Graphics2D;
import java.awt.GraphicsEnvironment;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.OpenOption;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import static principal.Driver.fichero;
import processing.core.PApplet;
import processing.core.PFont;
import processing.core.PVector;
import wordcram.*;

public class MotorDeCloudTag {
    public static final String fichero = System.getProperty("java.io.tmpdir")+"mio.jpg";
    String URL = "http://en.wikipedia.org/wiki/Barcamp";
    public void setURL(String s){
        URL = s;
    }
    public void draw() {
        BufferedImage image = new BufferedImage(500, 500, BufferedImage.TYPE_INT_RGB); 
        Graphics2D g = ((Graphics2D)image.getGraphics());
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, (int)image.getWidth(), (int)image.getHeight());
        new WordCram(image)
                .fromWebPage(URL)
                .withColors(new Color(255, 255, 255),
                            new Color(255, 0, 0),
                            new Color(0, 255, 0)) // mustard, red)
                .withFonts(GraphicsEnvironment.getLocalGraphicsEnvironment().getAvailableFontFamilyNames())
                .withAngler(moreRandomByWeight())
                .withPlacer(crazyPlacer())
                .sizedByWeight(8, 100)
                .maxNumberOfWordsToDraw(300)
                .drawAll();
        File outputfile = new File(fichero);
        try {
            ImageIO.write(image, "jpg", outputfile);
        } catch (IOException ex) {
            Logger.getLogger(MotorDeCloudTag.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println(outputfile);
    }

    WordAngler moreRandomByWeight() {
        return new WordAngler() {
            @Override public float angleFor(Word w) {
                float range = (1 - w.weight) * (float)Math.PI;
                return randomize(-range, range);
            }
        };
    }
    private static Random rnd = new Random();
    private static float randomize(float init, float end){
        return rnd.nextFloat()*(end-init)+init;
    }
    WordPlacer crazyPlacer() {
        return new WordPlacer() {
            @Override public PVector place(Word w, int rank, int words,
                    int ww, int wh, int fw, int fh) {
                float x = (fw - ww) * (1 - w.weight);
                float y = randomize(0, fh - wh);
                return new PVector(x, y);
            }
        };
    }

}
