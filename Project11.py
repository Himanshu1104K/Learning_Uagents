from uagents.setup import fund_agent_if_low
from uagents import Agent, Model, Context, Protocol
from ai_engine import UAgentResponse, UAgentResponseType
import sys
import random
from uagents import Field

dungeons = Agent(
    name="dungeonsanddragonsdiceroll",
    port=6145,
    seed="random_seed",
    endpoint=["http://YOUR_IP:6145/submit"],
)

fund_agent_if_low(dungeons.wallet.address())


@dungeons.on_event("startup")
async def hi(ctx: Context):
    ctx.logger.info(dungeons.address)


class Request(Model):
    dice_sides: int = Field("How many sides does your dice need?")


dice_roll_protocol = Protocol("DungeonsAndDragonsDiceRoll")


@dice_roll_protocol.on_message(model=Request, replies={UAgentResponse})
async def roll_dice(ctx: Context, sender: str, msg: Request):
    result: int = random.randint(1, msg.dice_sides)
    message = f"Dice roll result : {result}"
    await ctx.send(
        sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
    )


dungeons.include(dice_roll_protocol, publish_manifest=True)

dungeons.run()
