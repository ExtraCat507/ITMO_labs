package local.proga.lab2.pokemons;

import local.proga.lab2.attacks.status.PlayNice;


public class Steenee extends Bounsweet {
    public Steenee(String name, int i){
        super(name,i);
        setStats(
                52,40,48,40,48,62
        );
        addMove(new PlayNice());
    }
}
