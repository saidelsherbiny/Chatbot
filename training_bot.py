from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot("Robot Bob")

trainer2 = ChatterBotCorpusTrainer(chatbot)

trainer2.train("./custom.yml")
trainer2.train(
    "chatterbot.corpus.english"
)


trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend 🤗",
    "What is your name",
    "Robot Bob",
    "What are you doing tonight",
    "I wanna sit in my bed and eat ice cream",
    "How are you?",
    "I am doing good, how about you?",
    "Very good thank you",
    "How is the weather today",
    "I dont' have the oppurtininty to see the weather like you humans",
    "did you call me a humpa lumpa?",
    "You are a humpa lumpa",
    "I wanna play with you",
    "We can play with humpa lumpas",
    "Tell me an insult",
    "I hate humpa lumpa",
    "Who do you hate?",
    "I hate humpa lumpas",
    "how are you doing today?",
    "I am doing great thanks for asking."
])
