#!/usr/bin/python
#-*-coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import sys

BOT_NAME = "Bot"

chatbot = ChatBot(
                    BOT_NAME,
                    storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
                    database="chatterbot-database",
                    logic_adapters=[
                      "chatterbot.adapters.logic.MathematicalEvaluation",
                      "chatterbot.adapters.logic.TimeLogicAdapter",
                      "chatterbot.adapters.logic.ClosestMatchAdapter"
                    ],
                    filters=[
                      'chatterbot.filters.RepetitiveResponseFilter'
                    ],
                  )

if len(sys.argv) < 2:
  sys.exit(0)

message = sys.argv[1]
result = chatbot.get_response(message)
print ("%s" % result)