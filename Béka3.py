import Béka2

def main():
    print("FUTTATÁS ELINDULT")

    df_results = Béka2.plant_model(
        Béka1.pc_max,
        Béka1.pd_max,
        Béka1.eta,
        Béka0.prices
    )

    print("MODELL LEFUTOTT")
    print(df_results.head())

if __name__ == "__main__":
    main()

