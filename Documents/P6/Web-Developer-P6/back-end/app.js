//importer le package HTTP de node.js pour créerserveur
const express = require("express");
const mongoose = require("mongoose");

//utilisation de framework node "express"
const app = express();
const sauceRoutes = require('./routes/sauce');
const userRoutes = require('./routes/user');
const path = require('path');


app.use(express.json());

//connexion à la base de donnée du serveur
mongoose.connect('mongodb+srv://Piquant:o8x2Oqkr7WCZ1A55@piquantcluster.hctoax3.mongodb.net/?retryWrites=true&w=majority',
  { useNewUrlParser: true,
    useUnifiedTopology: true })
  .then(() => console.log('Connexion à MongoDB réussie !'))
  .catch(() => console.log('Connexion à MongoDB échouée !'));

// Configurer CROS: permettre l'utilisation même si origine différentes
  app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content, Accept, Content-Type, Authorization");
    res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, PATCH, OPTIONS");
    next();
});

//Execution des routes
app.use("/images", express.static(path.join(__dirname, 'images'))); 

app.use("/api/sauces", sauceRoutes);

app.use("/api/auth", userRoutes);

//Exportation vers les autres fichiers
module.exports = app;