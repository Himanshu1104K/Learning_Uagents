from uagents import context, Model, Agent, Bureau
from datetime import datetime


class Message(Model):
    message: str


agent_2 = Agent(
    name="bob", seed="bob seed", port=8001, endpoint="http://localhost:8001/submit"
)

ALICE_ADD = "Alice_add"


@agent_2.on_interval(period=3.0)
async def send_message(ctx : context):
    await ctx.send(ALICE_ADD,Message(message=f'Hello {datetime.today().date()}'))

if __name__ == "__main__":
    agent_2.run()