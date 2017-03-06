Group  members:
  Cecilia Berg, 478713
  Alexia Leimu, 474500
  Ilona Rahnasto, 480727

Link to our game store: http://limitless-cliffs-43418.herokuapp.com/

Implemented features:

Authentication, 200p
- Authorization as a user and a developer. All users can add games when they want to, or they can just play games.
- Email validation, the activation link is printed and must be accessed or the user can't log in

Basic player functionalities, 300p
- Payment is handled by the mockup
- All users can play games they have developed or bought
- Players can't access games they haven't bought even through url-paths
- Users can search for games according to their name, description and genre
- All games are displayed according to the date they have been uploaded
- Users own games and the games they've bought are in a separate section in alphabetical order

Basic developer functionalities, 200p
- All users can add games via the add game form, incorrect inputs are not accepted
- Users can see stats (times bought and times played) in the view of their own game (games/detail.html)
- Users can also delete their game in the game view
- Other user can not see the sats or delete the game, even through url-paths

Quality of Work, 100p
- Quality of code is good, necessary comments are added
- There is no repetitiveness
- Layout is modular
- Reusability is good, e.g. building absolute urls according to the server
- User experience is good, the game's are in an intuitive order and you don't have to choose to be a developer or a gamer in the registration. There is also a keep me logged in -feature.

Game/service interaction, 200p
- The platform supports a simple message system, messages are sent from game to the game service
- The game sends a postMessage to the parent window containing the current score
- Games store high scores, one player can not dominate the high score lists, only one score per player is shown

The site is mobile friendly, 50p


Most successful features:
All basic functionalities
Search-feature
Layout
User friendliness

Problematic features:
Heroku, the submission proved to be very hard. 
Security
Testing

Division of work:
Alexia: front-end, some back-end functionalities (e.g. game/service interaction)
Cecilia: several important back-end functionalities (e.g. authentication, payment)
Ilona: Git, Heroku, back-end (e.g. search, high scores)

We had our responsibilities, but helped each other when needed. Everyone was an expert in their own tasks and we explained the features we implemented to each other, so everyone learned something.

Instructions:
You can register from the register link in the top-right corner.
For testing the generated activation link is printed on the thank you for registering -page.
You can add games via the add game form that will be appear to the /games/ -page.
Buy the game by following the steps when clicking on the game's price
Play the game via clicking the game's name or the play-button
