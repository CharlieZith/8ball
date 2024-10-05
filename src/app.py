from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/api/8ball")
def eight_ball():
    answers = ["It is certain.", "Yes, definitely.", "You may rely on it.", "Outlook good.", "Yes", "Don't count on it.", "My sources say no.", "The outlook is not good.", "Very doubtful.", "No", "Ask me when pigs fly.", "Maybe in your dreams.", "I'm not a fortune teller, I'm an 8 ball.", "The stars are aligned in your favor.", "Keep your fingers crossed.", "Anything is possible with a little faith.", "The answer is blowing in the wind.", "Only time will tell.", "The universe has other plans for you."]
    response = {
        "success": True,
        "answer": random.choice(answers)
    }
    return response