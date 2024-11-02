package local.proga.lab2.pokemons;

import local.proga.lab2.attacks.physical.RockBlast;
import local.proga.lab2.attacks.physical.simpltac;
import local.proga.lab2.attacks.status.CalmMind;
import local.proga.lab2.attacks.status.Rest;
import local.proga.lab2.attacks.status.RockPolish;
import ru.ifmo.se.pokemon.*;

public class Corsola extends Pokemon {

    public static int a;
    static {
        System.out.println("static init");
        a = 3;
    }



    public Corsola(String name, int i){
        super(name,i);
        System.out.println("222222");
        setStats(
                65,55,95,65,95,35
        );
        setType(Type.WATER,Type.ROCK);
        setMove(new RockBlast(),new RockPolish(),new Rest(),new CalmMind());
    }
}
