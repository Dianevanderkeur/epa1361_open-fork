from ema_workbench import Model, ema_logging, MultiprocessingEvaluator, Policy, Scenario

from ema_workbench.em_framework.evaluators import perform_experiments
from ema_workbench.em_framework.samplers import sample_uncertainties
from ema_workbench import ema_logging, Samplers
import time
from problem_formulation import get_model_for_problem_formulation

model, _ = get_model_for_problem_formulation(5)
#model.uncertainties = []

ema_logging.log_to_stderr(ema_logging.INFO)

with MultiprocessingEvaluator(model) as evaluator:
    results = evaluator.perform_experiments(scenarios=200,               #500
                                            policies=4,
                                            uncertainty_sampling=Samplers.MC)