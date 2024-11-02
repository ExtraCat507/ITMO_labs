package local.proga.lab2.pokemons;

import local.proga.lab2.attacks.physical.PinMissile;
import local.proga.lab2.attacks.status.RockPolish;
import local.proga.lab2.attacks.status.Swagger;
import ru.ifmo.se.pokemon.*;

public class Ferroseed extends Pokemon {
    public Ferroseed(String name, int i){
        super(name,i);
        setStats(
            44,50,91,24,86,10
        );
        setType(Type.GRASS,Type.STEEL);
        setMove(new RockPolish(), new PinMissile(), new Swagger());
    }
}
