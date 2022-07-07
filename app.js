//importer le package HTTP de node.js pour créerserveur
const express = require("express");
const mongoose = require("mongoose");

//importer variable environnement
const dotenv = require("dotenv");
dotenv.config();
//importer les routes
const sauceRoutes = require('./routes/sauce');
const userRoutes = require('./routes/user');
const path = require('path');

//importer HELMET
const helmet = require("helmet");

//utilisation de framework node "express"
const app = express();
app.use(express.json());
//utilisation helmet
app.use(helmet());



//connexion à la base de donnée du serveur
mongoose.connect(`mongodb+srv://${process.env.DB_NAME}:${process.env.DB_PASSWORD}@${process.env.DB_USERNAME}.${process.env.DB_CLUSTER}.mongodb.net/?retryWrites=true&w=majority`,
  { useNewUrlParser: true,
    useUnifiedTopology: true })
  .then(() => console.log('Connexion à MongoDB réussie !'))
  .catch(() => console.log('Connexion à MongoDB échouée !'));

// Configurer CORS: permettre l'utilisation même si un agent utilisateur réalise une requête HTTP multi-origine, 
// cad lorsqu'il demande une ressource provenant d'un domaine, d'un protocole, d'un port différent 
// de celui utilisé sur la page courante

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

