from uagents import Agent,Context,Model
agent = Agent(name = "Himanshu" , seed = "hello my first seed")

# @agent.on_event("startup")
# async def introduce_agent(ctx : Context):
#     ctx.logger.info(f"Hello, I am Agent {agent.name} and My address is {agent.address}.")

print("Fetch Network Address : ",agent.wallet.address())

if __name__ == "__main__":
    agent.run()