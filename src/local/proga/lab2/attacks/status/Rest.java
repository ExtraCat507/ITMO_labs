package local.proga.lab2.attacks.status;

import ru.ifmo.se.pokemon.*;

public class Rest extends StatusMove {
    public Rest(){
        super(Type.PSYCHIC,0,100);
    }

    @Override
    protected void applySelfEffects(Pokemon p){
        p.setCondition(new Effect().turns(2).condition(Status.SLEEP));
        p.restore();
    }


    @Override
    protected String describe(){
        return "отдыхает (Rest) и восстанавливает все здоровье ";
    }
}
