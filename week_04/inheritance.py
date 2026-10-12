class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_trained = False
    def train(self):
        self.is_trained = True
    def describe(self):
        return f"Model: {self.model_name}"

class ClassificationModel(AIModel):
    def __init__(self, model_name, classes):
        super().__init__(model_name)
        self.classes = classes
    def describe(self):
        return f"{super().describe()} | Classes: {self.classes}"

class RegressionModel(AIModel):
    def __init__(self, model_name, target_name):
        super().__init__(model_name)
        self.target_name = target_name
    def describe(self):
        return f"{super().describe()} | Target: {self.target_name}"

def main():
    clf = ClassificationModel("Decision Tree", 3)
    reg = RegressionModel("Linear Regression", "Student Marks")
    for m in [clf, reg]:
        m.train()
        print(f"{m.describe()} | Trained: {m.is_trained}")

if __name__ == "__main__":
    main()
# is-a: Both child classes is-a AIModel, they reuse train()