import random
from flask import Flask, request

app = Flask(__name__)


quotes = {"I like the wine, and not the label.-David Rose",
          "I do not have a lot to my name right now, but I do have one thing: taste.-David Rose",
          "I have never heard someone say so many wrong things, one after the other, consecutively, in a row.-David Rose",
          "I could not be more at one with nature. I do Coachella every year.-David Rose",
          "Congratulations on your ongoing love for one another. You did it.-David Rose",
          "I’m starting to feel like I’m trapped in an Avril Lavigne lyric here.-David Rose",
          "Excuse me, I haven’t bedazzled anything since I was 22.-David Rose",
          "The internet is a breeding ground for freaks.-David Rose",
          "I’m trying very hard not to connect with people right now.-David Rose",
          "Like Beyonce, I excel as a solo artist and my mom dressed me well into my teens.-David Rose",
          "Very uninterested in that opinion.-David Rose",
          "I would hardly call myself an expert on this subject. And by subject, I mean genuine human emotion.-David Rose",
          "I’ve been burned so many times I’m like the human equivalent of the inside of a roasted marshmallow.-David Rose",
          }


@app.route('/')
def start_here():
    """Home page."""

    return """ 
    <!doctype html>
    <html>
        Hi! Welcome to the Schitts Creek Quotes Generator!<br/><a href='/greet'>click here to generate a quote</a></html>
    </html>
    """


# @app.route('/hello')
# def say_hello():
#     """Say hello and prompt for user's name."""

#     return """
#     <!doctype html>
#     <html>
#       <head>
#         <title>Hi There!</title>
#       </head>
#       <body>
#         <h1>Hi There!</h1>
#         <form action="/greet">
#           <select >
#             <option value="awesome">awesome</option>
#             <option value="terrific">terrific</option>
#             <option value="fantastic">fantastic</option>
#             <option value="neato">neato</option>
#             <option value="fantabulous">fantabulous</option>
#             <option value="wowza">wowza</option>
#             <otpion vaule="oh-so-not-meh">oh-so-not-meh</option>
#             <option value="brilliant">brilliant</option>
#             <option value="ducky">ducky</option>
#             <option value="coolio">coolio</option>
#             <option value="incredible">incredible</option>
#             <option value="wonderful">wonderful</option>
#             <option value="smashing">smashing</option>
#             <option value="lovely">lovely</option>
#           </select>
#             What's your name? <input type="text" name="person">
#             <input type="submit" value="Submit">
#         </form>
#       </body>
#     </html>
#     """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    quote = random.choice(list(quotes))

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Quote:</title>
      </head>
      <body>
        {quote}
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")

# key = random.choice(list(quotes))
# print(key)