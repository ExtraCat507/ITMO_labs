package local.proga.lab2.pokemons;

import local.proga.lab2.attacks.physical.Bulldoze;
import local.proga.lab2.attacks.physical.PinMissile;
import local.proga.lab2.attacks.status.RockPolish;
import local.proga.lab2.attacks.status.Swagger;
import ru.ifmo.se.pokemon.*;

public class Ferrothorn extends Ferroseed {
    public Ferrothorn(String name, int i){
        super(name,i);
        setStats(
                74,94,131,54,116,20
        );
        addMove(new Bulldoze());
    }
}
