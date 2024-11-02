import local.proga.lab2.pokemons.*;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();
        System.out.println("111111");
        Pokemon p1 = new Corsola("", 100);
        Pokemon p2 = new Ferroseed("", 100);
        Pokemon p3 = new Ferrothorn("", 100);
        Pokemon p4 = new Bounsweet("", 100);
        Pokemon p5 = new Steenee("", 100);
        Pokemon p6 = new Tsareena("", 100);
        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);
        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);

        b.go();
    }
}