import os # for importing env vars for the bot to use
from twitchio.ext import commands
import pyautogui
import time

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")

@bot.event
async def event_message(ctx):

	# make sure the bot ignores itself and the streamer
	if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
		return
	await bot.handle_commands(ctx)

	if '-segment1' in ctx.content.lower():
		pyautogui.click(x=1709, y=194)

	if '-segment2' in ctx.content.lower():
		pyautogui.click(x=1893, y=195)

	if '-segment3' in ctx.content.lower():
		pyautogui.click(x=2090, y=196)

	if '-segment4' in ctx.content.lower():
		pyautogui.click(x=2255, y=202)

	if '-segment5' in ctx.content.lower():
		pyautogui.click(x=2444, y=206)

	if '-segment6' in ctx.content.lower():
		pyautogui.click(x=1710, y=331)

	if '-segment7' in ctx.content.lower():
		pyautogui.click(x=1910, y=328)

	if '-segment8' in ctx.content.lower():
		pyautogui.click(x=2078, y=328)

	if '-segment9' in ctx.content.lower():
		pyautogui.click(x=2249, y=330)

	if '-segment10' in ctx.content.lower():
		pyautogui.click(x=2418, y=336)

	if '-segment11' in ctx.content.lower():
		pyautogui.click(x=1735, y=459)

	if '-segment12' in ctx.content.lower():
		pyautogui.click(x=1900, y=453)

	if '-segment13' in ctx.content.lower():
		pyautogui.click(x=2088, y=460)

	if '-segment14' in ctx.content.lower():
		pyautogui.click(x=2261, y=464)

	if '-segment15' in ctx.content.lower():
		pyautogui.click(x=2436, y=463)

	if '-segment16' in ctx.content.lower():
		pyautogui.click(x=1723, y=586)

	if '-segment17' in ctx.content.lower():
		pyautogui.click(x=1906, y=591)

	if '-segment18' in ctx.content.lower():
		pyautogui.click(x=2074, y=592)

	if '-segment19' in ctx.content.lower():
		pyautogui.click(x=2261, y=598)

	if '-segment20' in ctx.content.lower():
		pyautogui.click(x=2438, y=596)

	if '-segment21' in ctx.content.lower():
		pyautogui.click(x=1701, y=723)

	if '-segment22' in ctx.content.lower():
		pyautogui.click(x=1900, y=725)

	if '-segment23' in ctx.content.lower():
		pyautogui.click(x=2087, y=728)

	if '-segment24' in ctx.content.lower():
		pyautogui.click(x=2264, y=721)

	if '-segment25' in ctx.content.lower():
		pyautogui.click(x=2457, y=729)

	if '-new_program1' in ctx.content.lower():
		pyautogui.click(x=1379, y=106)

	if '-new_program2' in ctx.content.lower():
		pyautogui.click(x=1373, y=163)

	if '-new_program3' in ctx.content.lower():
		pyautogui.click(x=1371, y=223)

	if '-node1' in ctx.content.lower():
		pyautogui.click(x=1625, y=230)

	if '-node2' in ctx.content.lower():
		pyautogui.click(x=1883, y=236)

	if '-node3' in ctx.content.lower():
		pyautogui.click(x=2143, y=236)

	if '-node4' in ctx.content.lower():
		pyautogui.click(x=2394, y=241)

	if '-node5' in ctx.content.lower():
		pyautogui.click(x=1623, y=472)

	if '-node6' in ctx.content.lower():
		pyautogui.click(x=1892, y=474)

	if '-node7' in ctx.content.lower():
		pyautogui.click(x=2150, y=466)

	if '-node8' in ctx.content.lower():
		pyautogui.click(x=2401, y=475)

	if '-node9' in ctx.content.lower():
		pyautogui.click(x=1618, y=712)

	if '-node10' in ctx.content.lower():
		pyautogui.click(x=1887, y=716)

	if '-node11' in ctx.content.lower():
		pyautogui.click(x=2145, y=657)

	if '-node12' in ctx.content.lower():
		pyautogui.click(x=2390, y=709)
	if '-debug_continue' in ctx.content.lower():
		pyautogui.click(x=1863, y=510)

	if '-move_step' in ctx.content.lower():
		pyautogui.click(x=1335, y=742)

	if '-run' in ctx.content.lower():
		pyautogui.click(x=1398, y=743)

	if '-fast_run' in ctx.content.lower():
		pyautogui.click(x=1489, y=743)

	if '-stop' in ctx.content.lower():
		pyautogui.click(x=1254, y=746)

	if '-done' in ctx.content.lower():
		pyautogui.click(x=1986, y=661)

	if '-escape_segment' in ctx.content.lower():
		pyautogui.press('esc')
		pyautogui.click(x=1254, y=746)

	if '-write:' in ctx.content.lower():
		text = ctx.content.lower()
		text = text.replace('-write:', '')
		pyautogui.write(text)
	if '-backspace' in ctx.content.lower():
		pyautogui.keyDown('backspace')
		time.sleep(0.1)
		pyautogui.keyUp('backspace')

	if '-help' in ctx.content.lower():
		await ctx.channel.send(f"""COMMAND LIST
			-segment[1-25] (Select level.)

			-new_program[1-3] (Select level save file.)

			-node[1-12] (Switch between nodes to edit.)

			-debug_continue (In case you press level debug button)

			-run (Run code fully.)

			-fast_run (Run code but faster.)

			-stop (Stop running code.)

			-move_step (Instead of running code, move one step.)

			-escape_segment (Exit out of the segment'Level')

			-wirte:'Your code here without apostrophe'
			
			-backspace (Deletes one character.)""")
	if '-manual' in ctx.content.lower():
		await ctx.channel.send(f"https://www.vidarholen.net/contents/junk/files/TIS-100%20Reference%20Manual.pdf")
	if '-enter' in ctx.content.lower():
		pyautogui.keyDown('enter')
		time.sleep(0.1)
		pyautogui.keyUp('enter')
		await ctx.channel.send(f"ENTER @{ctx.author.name}")
	if '-del_all' in ctx.content.lower():
		pyautogui.hotkey('ctrl', 'a')
		time.sleep(1)
		pyautogui.keyDown('backspace')
		time.sleep(0.1)
		pyautogui.keyUp('backspace')




if __name__ == "__main__":
    bot.run()