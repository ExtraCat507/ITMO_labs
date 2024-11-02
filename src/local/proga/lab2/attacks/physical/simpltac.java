package local.proga.lab2.attacks.physical;

import ru.ifmo.se.pokemon.*;
import java.util.Random;
public class simpltac extends PhysicalMove{
    public simpltac() {
        super(Type.ROCK, 25, 90);
        this.hits = 6;
    }

    @Override
    protected String describe(){
        return "использует атаку . ударив " + this.hits + " раз!";
    }
}


