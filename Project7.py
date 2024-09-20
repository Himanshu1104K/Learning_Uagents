from uagents import Agent,Context,Model,Bureau,Protocol
from uagents.setup import fund_agent_if_low

A1 = Agent(name='Agent_one', seed="a1 seed")
A2 = Agent(name='Agent_Two', seed="a2 seed")
A3 = Agent(name='Agent_Three', seed="a3 seed")

fund_agent_if_low(A1.wallet.address())
fund_agent_if_low(A2.wallet.address())
fund_agent_if_low(A3.wallet.address())

class BroadcastExampleRequest(Model):
    pass

class BroadcastExampleResponce(Model):
    text : str

proto = Protocol(name='proto',version="1.0")

@proto.on_message(model=BroadcastExampleRequest,replies=BroadcastExampleResponce)
async def handle_request(ctx : Context,sender : str ,msg : BroadcastExampleRequest):
    await ctx.send(
        sender,BroadcastExampleResponce(text=f'Hello from {ctx.agent.name}')
    )

A1.include(proto)
A2.include(proto)

@A3.on_interval(period=5.0)
async def say_hello(ctx : Context):
    status_list = ctx.broadcast(proto.digest,message=BroadcastExampleRequest())
    ctx.logger.info(f"Trying to Contact {len(status_list)} agents.")

@A3.on_message(model = BroadcastExampleResponce)
async def handle_responce(ctx : Context , sender : str , msg : BroadcastExampleResponce):
    ctx.logger.info(f"Recieved message from {sender} : {msg.text}")

bureau = Bureau(port=8000, endpoint="http://localhost:8000/submit")
bureau.add(A1) 
bureau.add(A2) 
bureau.add(A3)

if __name__ == "__main__":
    bureau.run()