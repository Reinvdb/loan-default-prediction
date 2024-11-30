def check_missing_values(df: pd.DataFrame) -> None:
    """
    Function to calculate total and relative missing values per feature
    """

    ratios = []

    for col in df.columns:

        r = round(df[col].isnull().sum() / len(df) * 100, 3)
        ratios.append(f"{r}% ({df[col].isnull().sum()}/{len(df)})")

    print("Missing values:\n")

    for i, col in enumerate(df.columns):
        print(f"{col}: {ratios[i]}")


def check_outliers(df: pd.DataFrame) -> None:
    """
    Funtion to calculate total and relative number of outliers per feature
    """

    ratios = []

    for col in df.columns:

        iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
        lower_bound = df[col].quantile(0.25) - 1.5 * iqr
        upper_bound = df[col].quantile(0.75) + 1.5 * iqr

        r = round(
            len(df[(df[col] < lower_bound) | (df[col] > upper_bound)]) / len(df) * 100,
            3,
        )
        ratios.append(
            f"{r}% ({len(df[(df[col] < lower_bound) | (df[col] > upper_bound)])}/{len(df)})"
        )

    print("Outliers:\n")

    for i, col in enumerate(df.columns):
        print(f"{col}: {ratios[i]}")
