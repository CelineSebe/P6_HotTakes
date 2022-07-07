const Sauce = require('../models/Sauce');
const fs = require('fs');

//Controller POST pour créer une nouvelle sauce
exports.createSauce = (req, res, next) => 
{
    const sauceObject = JSON.parse(req.body.sauce);
    delete sauceObject._id;
    const sauce = new Sauce
    ({
        ...sauceObject,
        userId: req.auth.userId,
        imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
    });
    sauce.save()
    .then(() => { res.status(201).json({message: 'Objet enregistré !'})})
    .catch(error => { res.status(400).json( { error })})
 };

//Controller GET renvoie la sauce selon l'_id
 exports.findOneSauce = (req, res, next) => 
 {
    Sauce.findOne
    ({
      _id: req.params.id
    })
      .then(
      (sauce) => 
      {
        res.status(200).json(sauce);
      }
    ).catch
    ((error) => 
      {
        res.status(404).json({
          error: error
        });
      });
  }

//Controller PUT modifie la sauce selon l'_id.
// Une image est chargée vers la chaîne de caractères (req.body.sauce), 
//sinon vers req.param.id

 exports.modifySauce = (req, res, next) => 
 {
    const sauceObject = req.file ? 
    {
        ...JSON.parse(req.body.sauce),
        imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
    } : { ...req.body };
  
    // delete sauceObject._userId;
    Sauce.findOne({_id: req.params.id})
      .then ((sauce) => 
        {
          Sauce.updateOne({ _id: req.params.id}, { ...sauceObject, _id: req.params.id})
            .then(() => res.status(200).json({message : 'Objet modifié!'}))
            .catch(error => res.status(401).json({ error }));
        }
      )
      .catch((error) => 
        {
            res.status(400).json({ error });
        });
  };

//Controller DELETE supprime la sauce selon _l'id
exports.deleteSauce = (req, res, next) => 
{
  Sauce.findOne({_id: req.params.id})
    .then((sauce) => 
      {
      const filename = sauce.imageUrl.split('/images/')[1];
      fs.unlink(`images/${filename}`, () => 
        {
          Sauce.deleteOne({_id: req.params.id})
            .then(() =>  res.status(200).json({message: 'Objet supprimé !'}))
            .catch(error => res.status(401).json({ error }));
        });
      }
    )
    .catch( error => 
      {
      res.status(500).json({ error });
      });
};

//Controller GET renvoi tous les articles
exports.getAllSauces = (req, res, next) => 
{
  Sauce.find()
    .then((sauces) => 
      {
        res.status(200).json(sauces);
      })
    .catch((error) => 
    {
      res.status(400).json
      ({
          error: error
      });
    });
}
  
  //Controller POST définit le statut like, propre à chaque userId.
  //Like= 0 par défaut et quand l'userId annule son like/dislike.
  //Le nombre de like/dislikes total est mis à jour.

  exports.likeDislike = (req, res, next) => 
  {
  const sauceObject = { ...req.body};
    let like = req.body.like;
    let userId = req.body.userId;
    let sauceId = req.params.id;
    Sauce.findOne({ _id: sauceId })
      .then((sauce) => 
        {
          const countUsers = 
            {
              usersLiked: sauce.usersLiked,
              usersDisliked: sauce.usersDisliked,
              likes: 0,
              dislikes: 0,
            };
            if (like == 1) 
              {
                if (!sauce.usersLiked.includes(userId) && !sauce.usersDisliked.includes(userId)) 
                {
                    countUsers.usersLiked.push(userId);
                }
              } 
              else if (like == -1) 
              {
                if (!sauce.usersLiked.includes(userId) && !sauce.usersDisliked.includes(userId)) 
                {
                  countUsers.usersDisliked.push(userId);
                }
              } else 
              {
                if (sauce.usersLiked.includes(userId)) 
                {
                  const index = countUsers.usersLiked.indexOf(userId);
                  countUsers.usersLiked.splice(index, 1);
                } 
                else if (sauce.usersDisliked.includes(userId)) 
                {
                  const index = countUsers.usersDisliked.indexOf(userId);
                  countUsers.usersDisliked.splice(index, 1);
                }
              }
              countUsers.likes = countUsers.usersLiked.length;
              countUsers.dislikes = countUsers.usersDisliked.length;

              Sauce.updateOne({ _id: sauceId }, countUsers)
                .then(() => res.status(201)
                  .json({ message: "Action sur le like ou dislike prise en compte !" }))
                .catch((error) => res.status(400)
                  .json({ error }));
          })

          .catch((error) => res.status(500).json({ error }));
};

