package local.proga.lab2.pokemons;

import local.proga.lab2.attacks.physical.DoubleSlap;

public class Tsareena extends Steenee{
    public Tsareena(String name,int i){
        super(name,i);
        setStats(
                72,120,98,50,98,72
        );
        addMove(new DoubleSlap());
    }
}
