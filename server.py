import random
from flask import (Flask, request, render_template)

app = Flask(__name__)


quotes = {"I like the wine, and not the label. -David Rose",
          "I do not have a lot to my name right now, but I do have one thing: taste. -David Rose",
          "I have never heard someone say so many wrong things, one after the other, consecutively, in a row. -David Rose",
          "I could not be more at one with nature. I do Coachella every year. -David Rose",
          "Congratulations on your ongoing love for one another. You did it. -David Rose",
          "I’m starting to feel like I’m trapped in an Avril Lavigne lyric here. -David Rose",
          "Excuse me, I haven’t bedazzled anything since I was 22. -David Rose",
          "The internet is a breeding ground for freaks. -David Rose",
          "I’m trying very hard not to connect with people right now. -David Rose",
          "Like Beyonce, I excel as a solo artist and my mom dressed me well into my teens. -David Rose",
          "Very uninterested in that opinion. -David Rose",
          "I would hardly call myself an expert on this subject. And by subject, I mean genuine human emotion. -David Rose",
          "I’ve been burned so many times I’m like the human equivalent of the inside of a roasted marshmallow. -David Rose",
          "You know what, David, you get murdered first for once. -Alexis Rose",
          "I don’t skate through life. I walk through life in really nice shoes. -Alexis Rose",
          "What now? Do I leave everything behind and move to some random island to be with the love of my life? Because I did that with Harry Styles in England and it was, like, too rainy. -Alexis Rose",
          "I miss being surrounded by loose acquaintances who think I’m funny and smart and charming. -Alexis Rose",
          "Yeah, no. I know composting. Gwyneth Paltrow does a compost gift exchange. -Alexis Rose",
          "Love that journey for me. -Alexis Rose",
          "There is nothing wrong with asking for what you deserve. -Alexis Rose",
          "Ew, David! -Alexis Rose",
          "Fold in the cheese! -Moira Rose",
          "Fear not, she hath risen! -Moira Rose",
          "There’s nothing here but hot singles in my area. -Moira Rose",
          "This wine is awful. Get me another glass. -Moira Rose",
          "Allow me to offer you some advice. Take a thousand naked pictures of yourself now. You may currently think, “Oh, I’m too spooky,” or “Nobody wants to see these tiny boobies,” but believe me: one day you will look at those photos with much kinder eyes and say, ‘Dear God, I was a beautiful thing!’ -Moira Rose",
          "Let’s go. I’ve had enough waking hours for one day. -Moira Rose",
          "You must prepare for life, and whatever it will throw at you. The opportunities will diminish, and the ass will get bigger. Oh, you can bet your bottom dollar it will! Especially yours. You’re going to have a huge ass. -Moira Rose",
          "We’re all pitching in these days, dear. Like communists or non-union actors. -Moira Rose",
          "What you did was impulsive, capricious and melodramatic, but it was also wrong. -Moira Rose",
          "If airplane safety videos have taught me anything, David, it’s that a mother puts her own mask on first. -Moira Rose",
          "I can’t believe it. He’s managed to create something in this town that’s truly winsome. I would shop here, John, even without the nagging sense of obligation. -Moira Rose",
          "Our director appears to be on a kamikaze mission to sink this ship, and I refuse to be the goddess on its prow! -Moira Rose",
          "Gossip is the devil’s telephone. Best to just hang up. -Moira Rose",
          "Where is bébé’s chamber? -Moira Rose",
          "David, stop acting like a disgruntled penguin. -Moira Rose",
          "Oh, it’s always just a cold, John—until it’s full-blown typhoid! -Moira Rose",
          "Oh, I’d kill for a good coma right now. -Moira Rose",
          "It’s probably nothing, but I think I’ve killed a MAN! -Moira Rose",
          "Why should I be the only one encumbered with this emotional cargo? -Moira Rose",
          "I have my own holiday tradition. It’s like the 12 Days of Christmas, but it’s one day with 12 bottles of wine. -Steve Budd",
          "When you kissed me, that felt like my first time. All the things that you’re supposed to feel, I felt them last night. -Patrick Brewer",
          "Well, if I find out that you’re accusing me of doing something I didn’t do, then I’m going to accuse you of making false accusations. -Roland Schitt",
          "This isn’t “Say Yes to the Dress”, princess. Orange is the new orange. -Ronnie",
          "A hashtag? Is that two words? -Johnny Rose",
          "If you’re looking for an ass to kiss, it’s mine. -Roland Schitt",
          "There’s something wrong with your face. -Steve Budd",
          "You strike me as the sort of person that had a hard time in high school. -Jocelyn Schitt",
          "You better remember which nails you pulled those wigs from because your mother keeps a spreadsheet. -Johnny Rose",
          "Well, David, these kids of parties take time and planning. Now, when I planned that Casablanca-themed party for your mother’s 40th, I had to quarantine the camels for a month. -Johnny Rose",
          "My car is worth less than your pants. -Steve Budd",
          "David, I’ve spent most of my life not knowing what right was supposed to feel like, and then I met you. And everything changed. You make me feel right, David. -Patrick Brewer",
          "You’re my Mariah Carey. -Patrick Brewer",
          "Talk to the hand, son. Because the ears are no longer working. -Johnny Rose",
          }


@app.route('/')
def start_here():
    """Home page."""

    return render_template('homepage.html')


@app.route('/generator')
def generate_quote():
    """Generate the quotes."""
    
    quote = random.choice(list(quotes))

    return quote

# @app.route("/quote_update", methods=['POST'])
# def show_notes():

#     quote = request.json.get('new_quote')
#     quote_update = request.json.get('quote_update')
#     db.session.commit()
#     print(quote_update)
#     return jsonify({'quote': quote})   

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
