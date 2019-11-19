""" This function bases to 99% on the topograpy plot written by Clara.
The difference is, that multiple args are passed to the function.
In particular, the arguments over which it is not iterated are held constant
at their value which should equals their expectation value for univariate effects.
Also a Value error is raised if NaNs appear as function values.

"""

import numpy as np
import pandas as pd
from estimagic.optimization.optimize import _process_params
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("white")


def univariate_effects_plot(
    criterion,
    params,
    criterion_args=None,
    criterion_kwargs=None,
    num_points=20,
    loc=None,
    path=None,
):
    """Plot *criterion* around *params*["value"] between bounds for *to_plot* parameters.

    Args:
        criterion (function or list of functions):
            (List of) Python function(s) that takes a pandas DataFrame with parameters as the first
            argument and returns a scalar floating point value.

        params (pd.DataFrame):
            See :ref:`params`.

        criterion_args (list or tuple):
            additional positional arguments for criterion

        criterion_kwargs (dict):
            additional keyword arguments for criterion

        num_points (int):
            number of points to evaluate between lower and upper for each parameter

        loc:
            location of parameters for which to create univariate effects plots.

        path:
            path where to save the univariate effects plot

    """
    # set default arguments
    criterion_args = [] if criterion_args is None else criterion_args
    criterion_kwargs = {} if criterion_kwargs is None else criterion_kwargs
    to_plot = params.index if loc is None else params.loc[loc].index

    for col in ['lower', 'upper']:
        assert np.isfinite(params.loc[to_plot, col]).all()

    if callable(criterion):
        func_list = [(criterion.__name__, sns.color_palette()[0], criterion)]
    else:
        func_list = [(func.__name__, sns.color_palette()[i], func) for i, func in enumerate(criterion)]

    params = _process_params(params)

    nr_plots = len(to_plot)
    with sns.axes_style("whitegrid"):
        fig, axes = plt.subplots(nrows=nr_plots, ncols=1, figsize=(10, 6 * nr_plots))
    for crit_name, color, criterion in func_list:
        for ax, param_id in zip(axes, to_plot):
            data = _univariate_effects_data(
                criterion=criterion,
                params=params,
                num_points=num_points,
                param_id=param_id)
            sns.lineplot(
                data=data,
                x='Parameter Value',
                y='Function Value',
                label=crit_name,
                ax=ax,
                color=color,
                # kind='line',
            )
            sns.scatterplot(
                data=data,
                x='Parameter Value',
                y='Function Value',
                ax=ax,
                color=color,
                # kind='line',
            )

    for ax in axes:
        if len(func_list) > 1:
            ax.legend()

    for ax, param_id in zip(axes, to_plot):
        name = params.loc[param_id, 'name']
        ax.title.set_text(name)
    fig.tight_layout()

    if path is not None:
        fig.savefig(path, dpi=200)
    return fig, axes


def _univariate_effects_data(criterion, params, num_points, param_id):
    """Create the DataFrames with the criterion evaluations between bounds around *params*["value"]."""
    lower, upper = params.loc[param_id, ['lower', 'upper']]
    x_values = np.linspace(
        start=lower,
        stop=upper,
        num=num_points,
    )
    df = pd.DataFrame()
    df['Parameter Value'] = x_values
    df['Function Value'] = _evaluate_on_linspace(
        params=params,
        x_values=x_values,
        param_id=param_id,
        criterion=criterion,
    )
    return df


def _evaluate_on_linspace(criterion, params, x_values, param_id):
    evals = []
    modified_params = params.copy(deep=True)
    for x in x_values:
        modified_params.loc[param_id, 'value'] = x
        try:
            func_val = criterion(*modified_params['value'])
        except KeyboardInterrupt:
            raise
        except:
            func_val = np.nan
        evals.append(func_val)
    return evals