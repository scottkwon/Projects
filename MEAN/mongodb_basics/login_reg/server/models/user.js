const mongoose = require('mongoose');

const Schema = mongoose.Schema;
const bcrypt = require('bcryptjs');


let UserSchema = new Schema({

    email: {
        type: String,
        unique: [true, "The Email provided is already registered"],
        required: [true, "Please enter your email!"],
        validate:{
            validator: function(value) {
                return 	/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(value)
            },
            message: "Please enter a valid email address"
        }
    },

    first_name: {
        type: String, 
        required:[true, "Please enter your first name!"],
        trim: true,
    },

    last_name: {
        type: String,
        required: [true, "Please enter your last name!"],
        trim: true,
    },

    birthday: {
        type: Date,
        required: [true, "Please enter your birthday!"],
        validate: {
            validator: function(value) {
                return value < new Date();
            },
            message: "You must choose a day prior to today"
        }
    },

    password: {
        type: String,
        required: [true, "Please enter a password!"],
        minlength: [8, "Password must be atleast 8 characters"],
        maxlength: [32, "Password cannot be more than 32 characters"],
        validate: {
            validator: function(value) {
                return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,32}/.test( value );
            },
            message: "Password must contain an uppercase, number and a special character"
        }
    },

    confirm_password: {
        type: String,
        required:[true, "Please confirm your password!"]
    }

}, {timestamps:true});

UserSchema.pre('save',  function(next) {
    if(this.password != this.confirm_password){
        // This line will create an error message that matches the format of our other error messages
        this.invalidate('password', "Password and Password Confirmation do not match");
        // In order for our pre-save method to fail we must pass an err into next()
        let err = new Error("Password and password confirmation do not match");
        next(err);
    }else{
        // remove password_confirmation so we're not storing it
        this.confirm_password = '';
        this.password = bcrypt.hashSync(this.password, bcrypt.genSaltSync(8));
        next();
    }
})
mongoose.model('User', UserSchema);