from jr_devs.jr_dev1 import JrDev1
from jr_devs.jr_dev2 import JrDev2
from jr_devs.jr_dev3 import JrDev3
from jr_devs.jr_dev4 import JrDev4
from jr_devs.jr_dev5 import JrDev5

class Agent:
    def __init__(self):
        self.dev1 = JrDev1()
        self.dev2 = JrDev2()
        self.dev3 = JrDev3()
        self.dev4 = JrDev4()
        self.dev5 = JrDev5()

    def run_workflow(self):
        # Logic to run the workflow based on the diagram
        pass

if __name__ == "__main__":
    agent = Agent()
    agent.run_workflow()
