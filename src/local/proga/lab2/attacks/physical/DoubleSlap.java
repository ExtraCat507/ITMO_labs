package local.proga.lab2.attacks.physical;

import ru.ifmo.se.pokemon.*;
import java.util.Random;
public class DoubleSlap extends PhysicalMove{
    private int serialCounter;

    public DoubleSlap(){
        super(Type.NORMAL,15,85);
        this.hits = 1;
        this.serialCounter = 0;
    }

    protected int setHits(){
        Random rand = new Random();
        int determinant = rand.nextInt(8);
        return switch (determinant) {
            case 0, 1, 2 -> 2;
            case 3, 4, 5 -> 3;
            case 6 -> 4;
            default -> 5;
        };
    }

    @Override
    protected void applySelfEffects(Pokemon p){
        super.applySelfEffects(p);
        if(this.serialCounter == 0){
            this.hits = setHits();
        }
        this.serialCounter++;
        if(this.serialCounter == this.hits){
            System.out.println("Серия ударов завершена! Всего ударов было: " + this.serialCounter);
            this.serialCounter=0;
        }
    }




    @Override
    protected String describe(){
        return "использует атаку Double Slap: " + (this.serialCounter+1) + " удар!";
    }
}


