import Béka0
import Béka1
import Béka2_1, Béka2_2, Béka2_3

def main():
    print("FUTTATÁS ELINDULT")

    # Modell futtatása
    df_year = Béka0.df_all[Béka0.df_all['Delivery Day'].dt.year == 2018]
    df_year = df_year.copy()

    df_year["Price"] = (
        df_year["Price"]
        .astype(float)
        .interpolate()
        .bfill()
        .ffill()
    )

    prices_year = df_year['Price'].to_numpy()
    #nan_index = np.where(np.isnan(Béka0.prices))[0]

    df_results1 = Béka2_1.plant_model(
        Béka1.pc_max,
        Béka1.pd_max,
        Béka1.eta_t, Béka1.eta_p,
        prices_year,
        Béka1.FLH1
    )
    df_results2 = Béka2_2.plant_model(
        Béka1.pc_max,
        Béka1.pd_max,
        Béka1.eta_t, Béka1.eta_p,
        prices_year,
        Béka1.FLH2
    )
    df_results3 = Béka2_3.plant_model(
        Béka1.pc_max,
        Béka1.pd_max,
        Béka1.eta_t, Béka1.eta_p,
        prices_year,
        Béka1.FLH3
    )

    print("MODELL LEFUTOTT")

    # Plot the strategy and cumulative profit over time
    import matplotlib.pyplot as plt

    # Plotting
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Ábra Kumulatív profit 1
    ax1.plot(df_results1['Datetime'], df_results1['Cumulative Profit'], label='Kumulatív profit (FLH = 500)', color='g')
    ax1.plot(df_results2['Datetime'], df_results2['Cumulative Profit'], label='Kumulatív profit (FLH = 1000)', color='r')
    ax1.plot(df_results3['Datetime'], df_results3['Cumulative Profit'], label='Kumulatív profit (FLH = 2000)', color='b')
    ax1.set_xlabel('Dátum')
    ax1.set_ylabel('Kumulatív profit (EUR)', color='k')
    ax1.tick_params(axis='y', labelcolor='k')
    plt.title('Kumulatív profit 1')
    ax1.legend(loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plotting
    fig, bx1 = plt.subplots(figsize=(12, 6))

    # Line plots for buy/sell of each node
    bx1.plot(df_results1['Datetime'], df_results1['Charge(MW)'], label='Charge(MW)', color='g')
    bx1.plot(df_results1['Datetime'], df_results1['Discharge(MW)'], label='Discharge(MW)', color='r')
    bx1.set_ylabel('Charge/Discharge (MW)', color='k')
    bx1.tick_params(axis='y', labelcolor='k')
    bx1.legend(loc='upper left')
    plt.xticks(rotation=45)
    plt.title('Plant Operations 1')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
