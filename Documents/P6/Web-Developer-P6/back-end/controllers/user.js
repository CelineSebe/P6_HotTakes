
//importation models de la BD User.js
const User = require('../models/User');

//importation de bcrypt pour hasher le mot de passe
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

//importation crypto-js: chiffrement de l'email
// const cryptoJS = require("crypto-js");
//importation des variables d'environnement
// const dotenv = require("dotenv");
// dotenv.config();

exports.signup = (req, res, next) => {
    // const email_cryptoJS = cryptoJS.HmacSHA256(req.body.email, `${process.env.cryptoJS_email}`).toString();
    bcrypt.hash(req.body.password, 10)
      .then(hash => {
        const user = new User({
          email: req.body.email,
          password: hash
        });
        user
            .save()
            .then(() => res.status(201).json({ message: 'Utilisateur créé !' }))
            .catch(error => res.status(400).json({ error }));
      })
      .catch(error => res.status(500).json({ error }));
  };

  exports.login = (req, res, next) => {
    User.findOne({ email: req.body.email })
        .then(user => {
            if (user === null) {
                res.status(401).json({ message: 'Paire login/mot de passe incorrecte'});
            }else 
            {
                bcrypt.compare(req.body.password, user.password)
                .then(valid => {
                        if (!valid) {
                            res.status(401).json({ message: 'Paire login/mot de passe incorrecte' });
                        }else
                        {
                            res.status(200).json
                            ({
                                userId: user._id,
                                token: jwt.sign(
                                    { userId: user.id },
                                    `${process.env.APP_SECRET}`,
                                    { expiresIn: '24H' }
                                )
                            });
                        }
                })
                .catch(error => {
                    res.status(500).json( { error } );
                })
            }
        })
        .catch(error => {
            res.status(500).json({ error })
        });
 };