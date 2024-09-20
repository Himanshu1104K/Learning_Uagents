from uagents import Agent,Context

agent = Agent(name="Jatin gandu" , seed="Jatin Gandu ha")

@agent.on_event('startup')
async def initialize_storage(ctx : Context):
    ctx.storage.set("count",0)

@agent.on_interval(period=1.0)
async def On_interval(ctx:Context):
    curCount = ctx.storage.get("count")
    ctx.logger.info(f"Current count is {curCount}")
    ctx.storage.set("count",curCount+1)

if __name__ == "__main__":
    agent.run()