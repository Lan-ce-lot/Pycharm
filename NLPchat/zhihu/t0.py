from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    "My ChatterBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter"
)

