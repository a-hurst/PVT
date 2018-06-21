from klibs.KLIndependentVariable import IndependentVariableSet

# Create an independent variable set object for the experiment
PVT_ind_vars = IndependentVariableSet()

# Add a dummy variable so that the experiment runs
PVT_ind_vars.add_variable("dummy", str, ['null'])