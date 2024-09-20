from uagents import Agent,Context,Model

class GreetMessage(Model):
    name : str

class GreeterAgent(Agent):
    def __init__(self,name:str):
        super().__init__(name=name)

        self.on_message(GreetMessage)(self.greet)

    # @Agent.on_message(GreetMessage)
    async def greet(self,ctx : Context, message : GreetMessage):
        responce = f"Hello, {message.name}!"
        print(responce)

        await ctx.send(GreetMessage(name=responce))

if __name__ == "__main__":
    agent = GreeterAgent(name = "Greeter")
    agent.run()
        