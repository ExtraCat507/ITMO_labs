package local.proga.lab2.attacks.special;

import ru.ifmo.se.pokemon.*;

import java.util.concurrent.TransferQueue;

public class MagicalLeaf extends SpecialMove {
    public MagicalLeaf(){
        super(Type.GRASS,60,100);
    }

    @Override
    protected boolean checkAccuracy(Pokemon att, Pokemon def){
        return true;
    }


    @Override
    protected String describe(){
        return "использует атаку Magical Leaf";
    }

}
