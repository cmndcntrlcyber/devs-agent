from transformers import AutoModelForCausalLM, AutoTokenizer
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
        self.tokenizer = AutoTokenizer.from_pretrained("cognitivecomputations/dolphin-2.5-mixtral-8x7b")
        self.model = AutoModelForCausalLM.from_pretrained("cognitivecomputations/dolphin-2.5-mixtral-8x7b")

    def run_workflow(self):
        # Logic to run the workflow based on the diagram
        input_ids = self.tokenizer.encode("Your input text here", return_tensors='pt')
        output = self.model.generate(input_ids)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        print(response)
        pass

if __name__ == "__main__":
    agent = Agent()
    agent.run_workflow()
