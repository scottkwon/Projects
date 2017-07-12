const mongoose = require('mongoose');

const Post = mongoose.model('Post');
const Comment = mongoose.model('Comment');

module.exports = {
    index: (req,res) => {
        Post.find().sort({_id: -1}).populate('comments').exec( (err,foundPosts) => {
            if(err){
                console.log(err);
            } else {
                res.render('index', {posts:foundPosts})
            }
        })
    },

    createPost: (req,res) => {
        let post = new Post(req.body);
        post.save( (err,savedPost) => {
            if(err){
                console.log(err);
            } else {
                res.redirect('/');
            };
        });
    },

    createComment: (req,res) => {
        Post.findOne({_id: req.params.post_id}, (err, foundPost) => {
            if(err){
                console.log("Cannot find post");
            } else {
                // found the post and create new comment
                let comment = new Comment(req.body);
                console.log("New comment");
                // save comment to post
                comment._post = foundPost._id
                comment.save( (err, savedComment) => {
                    if(err){
                        console.log("Cannot save comment");
                    } else {
                        //add savedcomment to array of comments in post
                        foundPost.comments.push(savedComment);
                        foundPost.save( (err, savedPost) => {
                            if(err){
                                console.log("Cannot push comment into post array");
                            } else {
                                res.redirect('/');
                            };
                        });
                    };
                });
            };
        });
    }
};




