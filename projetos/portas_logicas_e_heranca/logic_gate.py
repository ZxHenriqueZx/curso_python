class LogicGate:
    def __init__(self, gate_name):
        self.name = gate_name
        self.output = None

    def get_name(self):
        return self.name

    def get_output(self):
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, gate_name):
        super().__init__(self, gate_name)

