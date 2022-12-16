from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import filters
from chatterbot import logic
from chatterbot import comparisons, response_selection
time_positive = ['time', 'clock', 'what is the current time', 'what is the time now', 'what’s the time', 'what time is it',
                 'what time is it now', 'do you know what time it is', 'could you tell me the time, please', 'what is the time', 'will you tell me the time',
                 'tell me the time', 'time please', 'show me the time', 'what is time', 'whats on the clock', 'show me the clock',
                 'what is the time', 'what is on the clock', 'tell me time', 'time', 'clock',]

time_negative = ['what are you doing', 'what’s up', 'when is time', 'who is time' 'could you', 'do you', 'what’s', 'will you', 'tell me', 'show me', 'current', 'do', 'now',
                 'will', 'show', 'tell', 'me', 'could', 'what', 'whats', 'i have time', 'who', 'who is', 'hardtime', 'when', 'what is', 'how',
                 'how is', 'when is', 'who is time', 'how is time', 'how is time', 'when is time', "food"]

chatbot = ChatBot("Code Ninja", filters=[
                  filters.get_recent_repeated_responses],
                  logic_adapters=[
    {"import_path": "chatterbot.logic.BestMatch",
     "statement_comparison_function": comparisons.SentimentComparison,
     "response_selection_method": response_selection.get_first_response,
     # "default_response": "I am not as smart as you may think try something else",
     "maximum_similarity_treshold": 0.8},
    {"import_path": "chatterbot.logic.TimeLogicAdapter",
     "positive": "time_positive",
     "negative": "time_negative",
     "maximum_similarity_treshold": 0.6
     }

])


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("🕵️‍♂️>")
    if query in exit_conditions:
        break
    else:
        print(f"🤖> {chatbot.get_response(query)}")
