class Deck {
    constructor(){
        var cards = 52
        var suit = ['Diamonds', 'Hearts', 'Clovers', 'Spades']
        var number = ['- A', '- K', '- Q', '- J', '- 10', '- 9', '- 8', '- 7', '- 6', '- 5','- 4','- 3','- 2','- 1']
        var self = this



        this.create = function(){
            var deck =[]
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

        this.reset = function(){
            var deck = [];
            this.create();
            return this;
        }

        this.deal = function(){
            var num = Math.floor(Math.random() *  this.deck.length);
            var card = this.deck[num];
            return card;
        }

    }
}

class Card {
    constructor(value,suit){
            var suit = suit;
            var value = value;
            return this;
        }
    }
}

class Player {
    constructor(name){
        var name=name;
        var hand=[];
        this.takeCard = function(){
        }


    }
}

deck1 = new Deck();
deck1.deal();
