package local.proga.lab2.attacks.status;

import ru.ifmo.se.pokemon.*;

public class RockPolish extends StatusMove{
    public RockPolish(){
        super(Type.ROCK,0,100);
    }

    @Override
    protected void applySelfEffects(Pokemon p){
        p.setMod(Stat.SPEED,+2);
        //System.out.println(p.getStat(Stat.SPEED));
    }

    @Override
    protected String describe(){
        return "использует Status-способность CalmMind";
    }

}

