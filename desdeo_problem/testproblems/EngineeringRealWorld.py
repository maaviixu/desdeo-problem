from desdeo_problem.problem.Variable import Variable
from desdeo_problem.problem.Objective import ScalarObjective
from desdeo_problem.problem.Problem import MOProblem, ProblemBase

import numpy as np

def re21(var_iv: np.array = ([2, 2, 2, 2])) -> MOProblem:
    """ Four bar truss design problem
    
    Arguments:
        var_iv (np.array): Optional, initial variable values.
            Defaults are [2, 2, 2, 2]. x1 and x4 lbound is 1, x2 and x3 lb is sqrt(2),
            ubound for all xs is 3.
    Returns:
        MOProblem: a problem object.
    """

    F = 10.0
    sigma = 10.0
    E = 2.0 * 1e5
    L = 200.0
    a = F / sigma

    def f_1(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)
        return L * ((2 * x[:, 0]) + np.sqrt(2.0) * x[:, 1] + np.sqrt(x[:, 2]) + x[:, 3])

    def f_2(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)
        return ((F * L) / E) * ((2.0 / x[:, 0]) + 
            (2.0 * np.sqrt(2.0) / x[:, 1]) - (2.0 * np.sqrt(2.0) / x[:, 2]) + (2.0 / x[:, 3]))

    objective_1 = ScalarObjective(name="name", evaluator=f_1, maximize=[False])
    objective_2 = ScalarObjective(name="name", evaluator=f_2, maximize=[False])

    objectives = [objective_1, objective_2]

    x_1 = Variable("x_1", 2 * a, a, 3 * a)
    x_2 = Variable("x_2", 2 * a, (np.sqrt(2.0) * a), 3 * a)
    x_3 = Variable("x_3", 2 * a, (np.sqrt(2.0) * a), 3 * a)
    x_4 = Variable("x_4", 2 * a, a, 3 * a)

    variables = [x_1, x_2, x_3, x_4]

    problem = MOProblem(variables=variables, objectives=objectives)

    return problem

def re22(var_iv: np.array = ([7, 10, 20])) -> MOProblem:
    """ Reinforced concrete beam design problem.
    
    Arguments:
        var_iv (np.array): Optional, initial variable values.
            Defaults are [7, 10, 20]. Bounds: x1 [0.2, 15], x2 [0, 20], x3 [0, 40]
    Returns:
        MOProblem: a problem object.
    """

    def f_1(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)
        return (29.4 * x[:, 0]) + (0.6 * x[:, 1] * x[:,2])

    def f_2(x: np.ndarray) -> np.ndarray:
        x = np.atleast_2d(x)
        return

    objective_1 = ScalarObjective(name="name", evaluator=f_1, maximize=[False])
    objective_2 = ScalarObjective(name="name", evaluator=f_2, maximize=[False])

    objectives = [objective_1, objective_2]

    x_1 = Variable("x_1", 7, 0.2, 15)
    x_2 = Variable("x_2", 10, 0, 20)
    x_3 = Variable("x_3", 20, 0, 40)

    variables = [x_1, x_2, x_3]

    problem = MOProblem(variables=variables, objectives=objectives)

    return problem