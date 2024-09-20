from uagents import Agent,Context, Bureau, Model
class Message(Model):
    message : str

emma = Agent(name="Emma", seed = "Emma_seed")
liam = Agent(name="liam", seed = "liam_seed")

@emma.on_interval(period=3.0)
async def send_message(ctx : Context):
    message_to_liam = Message(message="Hey Liam, how's it going?")
    await ctx.send(liam.address,message_to_liam)


@emma.on_message(model=Message)
async def emma_mess_handler(ctx : Context,sender:str,msg:Message):
    ctx.logger.info(f"Received Message from {sender} : {msg.message}")


@liam.on_message(model=Message)
async def liam_mess_handler(ctx : Context,sender : str,msg : Message):
    ctx.logger.info(f"Receiver Message from {sender} : {msg.message}")
    await ctx.send(emma.address,Message(message="Hello Emma! Great and you? "))

bureau = Bureau()
bureau.add(emma)
bureau.add(liam)


if __name__ == "__main__":
    bureau.run()