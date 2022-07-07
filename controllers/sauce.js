const Sauce = require('../models/Sauce');
const fs = require('fs');

exports.createSauce = (req, res, next) => {
    const sauceObject = JSON.parse(req.body.sauce);
    delete sauceObject._id;
    delete sauceObject._userId;
    const sauce = new Sauce({
        ...sauceObject,
        userId: req.auth.userId,
        imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
    });
    sauce.save()
    .then(() => { res.status(201).json({message: 'Objet enregistré !'})})
    .catch(error => { res.status(400).json( { error })})
 };

 exports.findOneSauce = (req, res, next) => {
    Sauce.findOne({
      _id: req.params.id
    }).then(
      (sauce) => {
        res.status(200).json(sauce);
      }
    ).catch(
      (error) => {
        res.status(404).json({
          error: error
        });
      }
    );
  }

 exports.modifySauce = (req, res, next) => {
    const sauceObject = req.file ? {
        ...JSON.parse(req.body.sauce),
        imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
    } : { ...req.body };
  
    // delete sauceObject._userId;
    Sauce.findOne({_id: req.params.id})
        .then((sauce) => {
            // if (sauce.userId != req.auth.userId) {
            //     res.status(401).json({ message : 'Not authorized'});
            // } else {
                Sauce.updateOne({ _id: req.params.id}, { ...sauceObject, _id: req.params.id})
                .then(() => res.status(200).json({message : 'Objet modifié!'}))
                .catch(error => res.status(401).json({ error }));
            }
          )
        .catch((error) => {
            res.status(400).json({ error });
        });
 };


exports.deleteSauce = (req, res, next) => {
  Sauce.findOne({ _id: req.params.id})
      .then((sauce) => {
          // if (sauce.userId != req.auth.userId) {
          //     res.status(401).json({message: 'Not authorized'});
          // } else {
              const filename = sauce.imageUrl.split('/images/')[1];
              fs.unlink(`images/${filename}`, () => {
                  Sauce.deleteOne({_id: req.params.id})
                      .then(() =>  res.status(200).json({message: 'Objet supprimé !'}))
                      .catch(error => res.status(401).json({ error }));
              });
          }
      )
      .catch( error => {
          res.status(500).json({ error });
      });
};

exports.getAllSauces = (req, res, next) => {
    Sauce.find()
    .then(
      (sauces) => {
        res.status(200).json(sauces);
      })
    .catch(
      (error) => {
        res.status(400).json({
          error: error
        });
      }
    );
  }
  
  exports.likeDislike = (req, res, next) => {
  const sauceObject = { ...req.body};
    let like = req.body.like;
    let userId = req.body.userId;
    let sauceId = req.params.id;
    Sauce.findOne({ _id: sauceId })
          .then((sauce) => {
                const countUsers = {
                      usersLiked: sauce.usersLiked,
                      usersDisliked: sauce.usersDisliked,
                      likes: 0,
                      dislikes: 0,
                };
                if (like == 1) {
                      if (!sauce.usersLiked.includes(userId) && !sauce.usersDisliked.includes(userId)) {
                            countUsers.usersLiked.push(userId);
                      }
                } else if (like == -1) {
                      if (!sauce.usersLiked.includes(userId) && !sauce.usersDisliked.includes(userId)) {
                            countUsers.usersDisliked.push(userId);
                      }
                } else {
                      if (sauce.usersLiked.includes(userId)) {
                            const index = countUsers.usersLiked.indexOf(userId);
                            countUsers.usersLiked.splice(index, 1);
                      } else if (sauce.usersDisliked.includes(userId)) {
                            const index = countUsers.usersDisliked.indexOf(userId);
                            countUsers.usersDisliked.splice(index, 1);
                      }
                }

                countUsers.likes = countUsers.usersLiked.length;
                countUsers.dislikes = countUsers.usersDisliked.length;

                Sauce.updateOne({ _id: sauceId }, countUsers)
                      .then(() => res.status(201).json({ message: "Action sur le like ou dislike prise en compte !" }))
                      .catch((error) => res.status(400).json({ error }));
          })

          .catch((error) => res.status(500).json({ error }));
};

