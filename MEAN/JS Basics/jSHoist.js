console.log(hello);
var hello = ‘world’;
// und

var needle = ‘haystack’;
test();

function test(){
	var needle = ‘magnet’;
	console.log(needle);
}
// magnet

var brendan = ‘super cool’;
function print(){
	brendan = ‘only okay’;
	console.log(brendan);
}
console.log(brendan);
// only okay

var food = ‘chicken’;
console.log(food);
eat();
function eat(){
	food = ‘half-chicken’;
	console.log(food);
	var food = ‘gone’;
}
// food, half-chicken

mean();
console.log(food);
var mean = function() {
	food = "chicken";
	console.log(food);
	var food = "fish";
	console.log(food);
}
console.log(food);
// chicken, fish, undef, undef

console.log(genre);
var genre = "disco";
rewind();
function rewind() {
	genre = "rock";
	console.log(genre);
	var genre = “r&b";
	console.log(genre);
}
console.log(genre);
// undef, rock, r&b

dojo = “san jose";
console.log(dojo);
learn();
function learn() {
	dojo = "seattle";
	console.log(dojo);
	var dojo = "burbank";
	console.log(dojo);
}
console.log(dojo);
//seattle, burbank, san jose