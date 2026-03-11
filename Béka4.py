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
        prices_year
    )
    df_results2 = Béka2_2.plant_model(
        Béka1.pc_max,
        Béka1.pd_max,
        Béka1.eta_t, Béka1.eta_p,
        prices_year
    )
    df_results3 = Béka2_3.plant_model(
        Béka1.pc_max,
        Béka1.pd_max,
        Béka1.eta_t, Béka1.eta_p,
        prices_year
    )

    print("MODELL LEFUTOTT")

    # Plot the strategy and cumulative profit over time
    import matplotlib.pyplot as plt

    # Plotting
    fig, ax1 = plt.subplots(figsize=(12, 6))



    # Line plot for cumulative profit 1
    ax1.plot(df_results1['Datetime'], df_results1['Cumulative Profit'], label='Cumulative Profit')
    ax1.set_xlabel('Datetime')
    ax1.set_ylabel('Cumulative Profit (EUR)', color='k')
    ax1.tick_params(axis='y', labelcolor='k')

    # Twin the axes for buy/sell plots
    ax2 = ax1.twinx()

    # Line plots for buy/sell of each node
    ax2.plot(df_results1['Datetime'], df_results1['Charge(MW)'], label='Charge(MW)', color='g')
    ax2.plot(df_results1['Datetime'], df_results1['Discharge(MW)'], label='Discharge(MW)', color='r')

    ax2.set_ylabel('Charge/Discharge (MW)', color='k')
    ax2.tick_params(axis='y', labelcolor='k')

    # Set labels and title
    plt.title('Plant Operations and Profit Over Time 1')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Line plot for cumulative profit 2
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(df_results2['Datetime'], df_results2['Cumulative Profit'], label='Cumulative Profit')
    ax1.set_xlabel('Datetime')
    ax1.set_ylabel('Cumulative Profit (EUR)', color='k')
    ax1.tick_params(axis='y', labelcolor='k')

    # Twin the axes for buy/sell plots
    ax2 = ax1.twinx()

    # Line plots for buy/sell of each node
    ax2.plot(df_results2['Datetime'], df_results2['Charge(MW)'], label='Charge(MW)', color='g')
    ax2.plot(df_results2['Datetime'], df_results2['Discharge(MW)'], label='Discharge(MW)', color='r')

    ax2.set_ylabel('Charge/Discharge (MW)', color='k')
    ax2.tick_params(axis='y', labelcolor='k')

    # Set labels and title
    plt.title('Plant Operations and Profit Over Time 2')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Line plot for cumulative profit 3
    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.plot(df_results3['Datetime'], df_results3['Cumulative Profit'], label='Cumulative Profit')
    ax1.set_xlabel('Datetime')
    ax1.set_ylabel('Cumulative Profit (EUR)', color='k')
    ax1.tick_params(axis='y', labelcolor='k')

    # Twin the axes for buy/sell plots
    ax2 = ax1.twinx()

    # Line plots for buy/sell of each node
    ax2.plot(df_results3['Datetime'], df_results3['Charge(MW)'], label='Charge(MW)', color='g')
    ax2.plot(df_results3['Datetime'], df_results3['Discharge(MW)'], label='Discharge(MW)', color='r')

    ax2.set_ylabel('Charge/Discharge (MW)', color='k')
    ax2.tick_params(axis='y', labelcolor='k')

    # Set labels and title
    plt.title('Plant Operations and Profit Over Time 3')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()
