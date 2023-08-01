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
        super().__init__(gate_name)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return self.put_pin_a()
        else:
            return self.pin_a

    def get_pin_b(self):
        if self.pin_b == None:
            return self.put_pin_b()
        else:
            return self.pin_b

    def put_pin_a(self):
        return int(input(f"Digite a entrada do pino A para a porta {self.get_name}: "))

    def put_pin_b(self):
        return int(input(f"Digite a entrada do pino B para a porta {self.get_name}: "))

class UnaryGate(LogicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)
        self.pin_a

    def get_pin_a(self):
        if self.pin_a == None:
            return self.put_pin_a()
        else
            return self.pin_a

    def put_pin_a(self):
        return int(input(f"Digite a entrada do pino A para a porta {self.get_name}"))

class AndGate(BinaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)

    def perform_gate_logic(self):
        a = self.get_pin_a
        b = self.get_pin_b
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)

    def perform_gate_logic(self):
        a = self.get_pin_a
        b = self.get_pin_b
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, gate_name):
        super().__init__(gate_name)

    def perform_gate_logic(self):
        a = self.get_pin_a
        if a == 1:
            return 0
        else:
            return 1

