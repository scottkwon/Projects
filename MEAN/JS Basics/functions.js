function runningLogger (){
    console.log('I am running!');
};
runningLogger();

function multiplyByTen(num){
    return console.log(num*10);
}
multiplyByTen(5);

function stringReturnOne(){
    return console.log('I am a beautiful string');
}
stringReturnOne();

function stringReturnTwo(){
    return console.log('I am a very pretty string');
}
stringReturnTwo();

function caller(param){
    if (typeof(param) === 'function') {
        param();
    } else {
        return console.log('Argument is not a function!');
    }
}
caller(stringReturnTwo);

function myDoubleConsoleLog (param1, param2) {
    if (typeof(param1) === 'function' && typeof(param2) === 'function') {
        console.log(param1());
        console.log(param2());
}
}
myDoubleConsoleLog(stringReturnOne(), stringReturnTwo());

function caller2(param){
    console.log('starting..')
    setTimeout(function(){
    if (typeof(param) == 'function') {
        console.log(param());
    }
    }, 2000);
}

caller2(stringReturnOne);
