import os

import discord

import openai

with open("chat.txt"  ,"r") as f:

        chat=f.read()



openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")


class MyClient(discord.Client):

        async def on_ready(self):
                print(f"Logged on as { self.user}!")

        async def on_message(self, message):
                global chat
                chat+=( f"{message.author}:{message.content}\n")

                print(f"Message from {message.author}:{message.content}")
                if self.user != message.author:
                        if self.user in message.mentions:
                                print(chat)
                                response = openai.Completion.create(
                                    model="gpt-3.5-turbo-instruct",
                                    prompt=f"{chat}\nsubhamGPT: ",
                                    temperature=1,
                                    max_tokens=256,
                                    top_p=1,
                                    frequency_penalty=0,
                                    presence_penalty=0)
                        channel = message.channel
                        messageToSend = response.choices[0].text
                        await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)

# app id 1161510766541799474
# public key158a1363fdf8bba2d4c40d48b96e579e0ae868ddf996d2e20be9bf18d3c5038b
# token MTE2MTUxMDc2NjU0MTc5OTQ3NA.G-cyLa.COjssOC4lf93b1wOeL66i5oGY_x4IpC-L9H0C4
