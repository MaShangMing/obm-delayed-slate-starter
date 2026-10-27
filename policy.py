class Policy:
    def __init__(self, config):
        self.config = config

    def choose(self, observation):
        raise NotImplementedError("Implement the sequential decision policy")
