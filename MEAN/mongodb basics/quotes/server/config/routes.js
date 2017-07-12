var mongoose = require('mongoose');

var Quote = mongoose.model('Quote');

module.exports = app => {

    app.get('/', (req,res) => {
        res.render('index');
    });

    app.post('/process', (req,res)=>{
        let quote = new Quote(req.body);
        quote.save( (err,savedQuote) => {
            if(err){
                console.log(quote.errors);
                res.render('index', {errors: quote.errors})
            } else {
                console.log("succesfully created quote")
                res.redirect('/quotes')
            }
        })
    })

    app.get('/quotes', (req,res) => {
        Quote.find({}, null, {sort: {'_id': -1}}, (err, quotes)=>{
            if(err){
                console.log(err);
                res.render('quotes', {errors: quote.errors})
            } else {
                res.render('quotes', {quotes: quotes});
            }
        })
    })
}