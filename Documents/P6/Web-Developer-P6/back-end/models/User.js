
//importation de mongoose
const mongoose = require('mongoose');
const uniqueValidator = require('mongoose-unique-validator');

//Création du modèle User à envoyer au serveur
const userSchema = mongoose.Schema({
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true },
});
//pour que l'email utilisé ne soit utilisé une seule fois
userSchema.plugin(uniqueValidator);

module.exports = mongoose.model('User', userSchema);