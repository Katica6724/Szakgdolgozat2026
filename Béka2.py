print("BÉKA2 FÁJL BETÖLTŐDÖTT")
import Béka0 , Béka1
import pandas as pd
import pyomo.environ as pyo


def plant_model(pc_max, pd_max, eta, prices):
    print("A - beléptem a függvénybe")

    m = pyo.ConcreteModel()
    print("B - modell létrehozva")

    print("C - tovább megyünk")

    # time is what we will use as the index
    m.t = pyo.RangeSet(0, 1800)
    # Parameters
    m.min_cap = 0  # no negative discharging
    m.max_cap = pc_max  # don’t charge over
    # Variables
    m.buy = pyo.Var(m.t, bounds=(0, pc_max), initialize=0)  # Buy from grid
    m.sell = pyo.Var(m.t, bounds=(0, pc_max), initialize=0)  # Sell to grid
    m.C = pyo.Var(m.t, bounds=(0, pc_max), initialize=0)  # Plant state
    m.y = pyo.Var(m.t, domain=pyo.Binary) # binary variable
    print("2 - változók definiálva")

    #Constraints
    # Plant state - set initial state to max capacity and accounts for efficiency
    def storage_state(m,t):
        # set first hour at max charge
        if t == m.t.first():
            return m.C[t] == m.max_cap
        else:
            return m.C[t] == m.C[t-1] + eta*m.buy[t] - m.sell[t]/eta

    m.storage_state = pyo.Constraint(m.t, rule=storage_state)

    # Make sure plant does not charge and discharge at the same time

    def buy_sell_logic(m, t):
        return m.buy[t] <= pc_max * m.y[t]

    m.buy_logic = pyo.Constraint(m.t, rule=buy_sell_logic)

    def sell_logic(m, t):
        return m.sell[t] <= pd_max * (1 - m.y[t])

    m.sell_logic = pyo.Constraint(m.t, rule=sell_logic)

    # make sure plant does not charge above the limit
    def over_charge(m, t):
        return m.buy[t] <= (m.max_cap - m.C[t]) / eta

    m.over_charge = pyo.Constraint(m.t, rule=over_charge)

    def over_discharge(m, t):
        return m.sell[t] <= m.C[t] * eta

    m.over_discharge = pyo.Constraint(m.t, rule=over_discharge)

# Plant cannot store more energy than its maximum capacity
    def charge_less_than_capacity(m, t):
        return m.C[t] <= m.max_cap

    m.charge_constraint = pyo.Constraint(m.t, rule=charge_less_than_capacity)

    # Plant cannot be zero
    def zero_bound_capacity(m, t):
        return m.C[t] >= m.min_cap

    m.zero_bound_capacity = pyo.Constraint(m.t, rule=zero_bound_capacity)

    # Positive Buy/Sell values only
    def buy_positive(m,t):
        return m.buy[t] >= 0

    m.buy_positive = pyo.Constraint(m.t, rule=buy_positive)

    def sell_positive(m,t):
        return m.sell[t] >= 0

    m.sell_positive = pyo.Constraint(m.t, rule=sell_positive)
    print("3 - constraint kész")
    print("Időlépések száma:", len(prices))

    #OBJECTIVE FUNCTION

    def objective(m):
        profit = sum(
            (m.sell[t] * (prices[t])) - (m.buy[t] * (prices[t]))for t in m.t) - Béka1.Ctot_1
        return profit

    m.objective = pyo.Objective(rule=objective, sense=pyo.maximize)

    # Solve the model


    solver = pyo.SolverFactory('highs')
    print("4 - solver indul")
    results = solver.solve(m, tee=True)

    profit = m.objective.expr()
    print("5 - solver vége")

    charge_hist = [pyo.value(m.C[t]) for t in m.t]
    buy_hist = [pyo.value(m.buy[t]) for t in m.t]
    sell_hist = [pyo.value(m.sell[t]) for t in m.t]

    profit_hist = [
        sell_hist[t] * prices[t]
        - buy_hist[t] * prices[t]
        for t in range(len(m.t))
    ]

    print("6 - df_results kész")

    df_results = pd.DataFrame({
        'Datetime': Béka0.df_all['Delivery Day'][:len(m.t)],
        'Hour': Béka0.df_all['Hour'][:len(m.t)],
        'Price(EUR/MWh)': prices[:len(m.t)],
        'Charge(MW)': buy_hist,
        'Discharge(MW)': sell_hist,
        'Profit(EUR)': profit_hist
    })

    df_results['Cumulative Profit'] = df_results['Profit(EUR)'].cumsum()

    print("7 - return előtt")

    return df_results












