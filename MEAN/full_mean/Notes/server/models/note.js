const mongoose = require('mongoose');

const Schema = mongoose.Schema;

let NoteSchema = new Schema({
    content: {type: String, required:true}
}, {timestamps:true});

mongoose.model('Note', NoteSchema);