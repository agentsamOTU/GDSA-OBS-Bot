import discord
import asyncio
import threading
import obspython as obs
from dotenv import load_dotenv
from os import getenv

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

def script_load(self):
  global client  
  if asyncio.get_event_loop().is_closed():
        asyncio.set_event_loop(asyncio.new_event_loop())
  load_dotenv(script_path()+".env")
  token = getenv("TOKEN")

  client = MyClient()
  thread=threading.Thread(target=client.run,args=(token,))
  thread.start()

def script_description():
  return """<center><h2>Source Shake!!</h2></center>
            <p>Shake a source in the current scene when a hotkey is pressed. Go to <em>Settings
            </em> then <em>Hotkeys</em> to select the key combination.</p><p>Check the <a href=
            "https://github.com/obsproject/obs-studio/wiki/Scripting-Tutorial-Source-Shake.md">
            Source Shake Scripting Tutorial</a> on the OBS Wiki for more information.</p>"""

def timed_update():
  print("test")