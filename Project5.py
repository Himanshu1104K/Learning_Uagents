from uagents import Agent,Context,Model,Bureau

class Message(Model):
    message : str
    money : int

honey = Agent(name = "honey" , seed = "honey seed")
himanshu = Agent(name = "himanshu" , seed = "himanshu seed")

@honey.on_interval(period = 3.0)
async def send_message(ctx : Context):
    await ctx.send(himanshu.address,Message(message = "Hello there Himanshu.",money = 15000))

@honey.on_message(model = Message)
async def honey_mess_handler(ctx : Context,sender : str,msg:Message):
    ctx.logger.info(f"Received message from {sender} : {msg.message}\nHe have {msg.money} Money.")

@himanshu.on_message(model = Message)
async def himanshu_mess_handler(ctx : Context,sender : str,msg:Message):
    ctx.logger.info(f"Received message from {sender} : {msg.message}\nHe have {msg.money} Money.")
    await ctx.send(honey.address,Message(message = "Hello there Honey.",money = 19000))

bureau = Bureau()
bureau.add(honey)
bureau.add(himanshu)

if __name__ == "__main__":
    bureau.run()
