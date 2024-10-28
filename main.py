from flask import Flask
import random


app = Flask(__name__)
facts_list = ["Elon Musk claims that social networks are designed to keep us inside the platform to spend as much time as possible viewing content.",
"According to a 2018 study, more than 50% of people aged 18-34 think they are addicted to their smartphones.",
"Social networks have positive and negative sides and we should be aware of both when using these platforms.",
"The study of technology addiction is one of the most relevant areas of modern scientific research."]


@app.route("/")
def index():
return f '<h1>HELLO! On this page, you can learn a few interesting facts about technological addictions!<a href="/random_fact">View a random fact!</a>'


@app.route("/random_real")
def facts():
return f'<h1>{random.choice(facts_list)}</h1>'


@app.route("/t")
def slm():
return f'<h1>selam ben tifo</h1>'
app.run(debug=True)
