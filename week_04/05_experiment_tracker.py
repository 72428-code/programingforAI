import json 
from pathlib import Path 
from experiment import Experiment 
lab_folder = Path(__file__).resolve().parent 
json_path = lab_folder / "data" / "experiments.json" 
report_path = lab_folder / "reports" / "experiment_summary.txt" 
def add_experiment(experiments, experiment_id, model_name, dataset_name, accuracy):
    """Create, validate, and add an experiment."""
    accuracy = float(accuracy)

    experiment = Experiment(experiment_id, model_name, dataset_name, accuracy)

    experiments.append(experiment)
    return experiment
def display_experiments(experiments):
    """Display all experiments clearly."""
    if not experiments:
        print("No experiments are available.")
        return

    for experiment in experiments:
        print(
            f"{experiment.experiment_id} | {experiment.model_name} | {experiment.dataset_name} | Accuracy: {experiment.accuracy:.2f}"
        )
        def search_experiment(experiments, experiment_id):
            """Search for an experiment by its ID."""
            for experiment in experiments:
                if experiment.experiment_id == experiment_id:
                    return experiment
            return None
        def find best_experiment(experiments):
             if not experiments:
                 return None
           retrun max(experiments, key=lambda experiment:experiments.accuracy)
        def load-experiments(file_path):
            """Load experiments from a JSON file."""
            json_path = Path(file_path)
            if not json_path.exists():
                return []

            with json_path.open("r", encoding="utf-8") as file:
                experiment_records = json.load(file)

            experiments = []
            for record in experiment_records:
                experiment = Experiment(
                    record["experiment_id"],
                    record["model_name"],
                    record["dataset_name"],
                    record["accuracy"]
                )
                experiments.append(experiment)

            return experiments
