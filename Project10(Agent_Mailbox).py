from uagents import Context,Agent,Model 

class Message(Model):
    message : str

AGENT_MAILBOX_KEY = 'PUT YOUR AGENT MAILBOX KEY'
SEED_PHRASE = 'Your Seed Phrase'

agent = Agent(
    name='alice',
    seed="Alice Seed",
    mailbox= f"{AGENT_MAILBOX_KEY}@https://agentverse.ai"
)

@agent.on_message(model=Message,replies={Message})
async def handle_message(ctx :Context,sender : str, msg : Message):
    ctx.logger.info(f'Recieved Message from {sender} : {msg}')


# print(f'Your Agent address is : {agent.address}')

if __name__ == "__main__":
    agent.run()