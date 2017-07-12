const mongoose = require('mongoose');

const Schema = mongoose.Schema;

let commentSchema = new Schema({
    name: {type: String , required: true},
    content: {type: String, required: true},
    _post: {type: Schema.Types.ObjectId, ref:'Post'},
}, {timestamps: true})

mongoose.model('Comment', commentSchema);