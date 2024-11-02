package local.proga.lab2.pokemons;

import local.proga.lab2.attacks.special.MagicalLeaf;
import local.proga.lab2.attacks.status.SweetScent;
import ru.ifmo.se.pokemon.*;

public class Bounsweet extends Pokemon {
    public Bounsweet(String name, int i){
        super(name,i);
        setStats(
                42,30,38,30,38,32
        );
        setType(Type.GRASS);
        setMove(new SweetScent(),new MagicalLeaf());
    }
}
