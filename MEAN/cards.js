class Deck {
    constructor(){
        var cards = 52
        var suit = ['Diamonds', 'Hearts', 'Clovers', 'Spades']
        var number = ['- A', '- K', '- Q', '- J', '- 10', '- 9', '- 8', '- 7', '- 6', '- 5','- 4','- 3','- 2','- 1']
        var deck =[]
        this.create = function(){
            for(var i = 0; i < suit.length; i++){
                for(var j = 0; j < number.length; j++){
                    deck.push(suit[i]+number[j]);
                }
            }
            console.log(deck)
            return this;
        }
        this.shuffle = function(){

        }
    }
}

deck1 = new Deck();
deck1.create();
