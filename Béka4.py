import Béka0
import Béka1
import Béka2
import matplotlib.pyplot as plt


def main():
    print("FUTTATÁS ELINDULT")

    # Modell futtatása
    df_results = Béka2.plant_model(
        Béka1.pc_max,
        Béka1.pd_max,
        Béka1.eta,
        Béka0.prices
    )

    print("MODELL LEFUTOTT")

    # Plot the strategy and cumulative profit over time
    import matplotlib.pyplot as plt

    # Plotting
    fig, ax1 = plt.subplots(figsize=(12, 6))



    # Line plot for cumulative profit
    ax1.plot(df_results['Datetime'], df_results['Cumulative Profit'], label='Cumulative Profit')
    ax1.set_xlabel('Datetime')
    ax1.set_ylabel('Cumulative Profit (EUR)', color='k')
    ax1.tick_params(axis='y', labelcolor='k')

    # Twin the axes for buy/sell plots
    ax2 = ax1.twinx()

    # Line plots for buy/sell of each node
    ax2.plot(df_results['Datetime'], df_results['Charge(MW)'], label='Charge(MW)', color='g')
    ax2.plot(df_results['Datetime'], df_results['Discharge(MW)'], label='Discharge(MW)', color='r')

    ax2.set_ylabel('Charge/Discharge (MW)', color='k')
    ax2.tick_params(axis='y', labelcolor='k')

    # Set labels and title
    plt.title('Plant Operations and Profit Over Time')
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()
