// The goal is to survive for 30 seconds, and keep the mines intact for at least 30 seconds.

function chooseStrategy() {
    var enemies = hero.findEnemies();
    // If you can summon a griffin-rider, return "griffin-rider"
    if (hero.gold >= hero.costOf("griffin-rider")) {
        return "griffin-rider";
    }
    // If there is a fangrider on your side of the mines, return "fight-back"
    for(let i=0;i<enemies.length;i++){
        let v = enemies[i];
        let p = v.pos;
        
        if(p.x<38){
            return "fight-back";
        }
    }
    // Otherwise, return "collect-coins"
    return "collect-coins";
}

function commandAttack() {
    // Command your griffin riders to attack ogres.
    let friends = hero.findFriends();
    let ogres = hero.findEnemies();//hero.findByType("ogre",hero.findEnemies());
    
    let closest;
    let distance;
    
    for(let i=0;i<ogres.length;i++){
        let v = ogres[i];
        let d = hero.distanceTo(v);
        

        
        if((!distance || d<distance) && v.pos.x>50){
            closest = v;
            distance = d;
        }
    }
    
    if(closest && friends.length>0){
        for(let i=0;i<friends.length;i++){
            let v = friends[i];
            if(v.type == "griffin-rider"){
                hero.command(v,"attack",closest);
            }
        }
    }
}

function pickUpCoin() {
    // Collect coins
    var items = hero.findItems();
    var nearestCoin = hero.findNearest(items);
    if(nearestCoin) {
        hero.move(nearestCoin.pos);
    }
}

function heroAttack() {
    // Your hero should attack fang riders that cross the minefield.
    hero.attack(hero.findNearestEnemy());
}

while(true) {
    commandAttack();
    var strategy = chooseStrategy();
    // Call a function, depending on what the current strategy is.
    if(strategy == "griffin-rider"){
        hero.summon("griffin-rider");
    }else if(strategy=="fight-back"){
        heroAttack();
    }else if(strategy == "collect-coins"){
        pickUpCoin();
    }
}
