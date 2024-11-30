import pandas as pd
import plotly.express as px


def plot_histogram(df: pd.DataFrame, feature: str, save: bool = False) -> None:
    """
    Function to plot histogram of a feature
    """

    fig = px.histogram(df, x=feature)

    fig.update_layout(
        title=f"<b>Histogram of {feature}",
        xaxis=dict(title=f"{feature}"),
        yaxis=dict(title="Count"),
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(f"{VIZUALIZATION_DIR}/histogram_{feature}.png", format="png")
        if save
        else fig.show()
    )


def plot_histogram_per_category(
    df: pd.DataFrame, feature: str, category_feature: str, save: bool = False
) -> None:
    """
    Function to plot histogram of a feature per category
    """

    fig = px.histogram(df, x=feature, color=category_feature)

    fig.update_layout(
        title=f"<b>Histogram of {feature} per {category_feature}",
        xaxis=dict(title=f"{feature}"),
        yaxis=dict(title="Count"),
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(
            f"{VIZUALIZATION_DIR}/histogram_{feature}_per_{category_feature}.png",
            format="png",
        )
        if save
        else fig.show()
    )


def plot_boxplot(df: pd.DataFrame, feature: str, save: bool = False) -> None:
    """
    Function to plot boxplot of a feature
    """

    fig = px.box(df, y=feature, points="all")

    fig.update_layout(
        title=f"<b>Boxplot of {feature}",
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(f"{VIZUALIZATION_DIR}/boxplot_{feature}.png", format="png")
        if save
        else fig.show()
    )


def plot_boxplot_per_category(
    df: pd.DataFrame, feature: str, category_feature: str, save: bool = False
) -> None:
    """
    Function to plot boxplot of a feature per category
    """

    fig = px.box(df, y=feature, x=category_feature, points="all")

    fig.update_layout(
        title=f"<b>Boxplot of {feature} per {category_feature}",
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(
            f"{VIZUALIZATION_DIR}/boxplot_{feature}_per_{category_feature}.png",
            format="png",
        )
        if save
        else fig.show()
    )


def plot_violin(df: pd.DataFrame, feature: str, save: bool = False) -> None:
    """
    Function to plot violin plot of a feature
    """

    fig = px.violin(df, y=feature, box=True, points="all")

    fig.update_layout(
        title=f"<b>Violin plot of {feature}",
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(f"{VIZUALIZATION_DIR}/violin_{feature}.png", format="png")
        if save
        else fig.show()
    )


def plot_violin_per_category(
    df: pd.DataFrame, feature: str, category_feature: str, save: bool = False
) -> None:
    """
    Function to plot violin plot of a feature per category
    """

    fig = px.violin(df, y=feature, x=category_feature, box=True, points="all")

    fig.update_layout(
        title=f"<b>Violin plot of {feature} per {category_feature}",
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(
            f"{VIZUALIZATION_DIR}/violin_{feature}_per_{category_feature}.png",
            format="png",
        )
        if save
        else fig.show()
    )


def plot_bar_frequency(df: pd.DataFrame, feature: str, save: bool = False) -> None:
    """
    Function to plot frequency per category of a feature
    """

    counts = df[feature].value_counts()
    fig = px.bar(y=counts.values, x=counts.index, text=counts.values)

    fig.update_layout(
        title=f"<b>Frequency of values in {feature}",
        xaxis=dict(title=f"{feature}"),
        yaxis=dict(title="Count"),
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(
            f"{VIZUALIZATION_DIR}/bar_frequency_{feature}.png", format="png"
        )
        if save
        else fig.show()
    )


def plot_bar_frequency_per_category(
    df: pd.DataFrame, feature: str, category_feature: str, save: bool = False
) -> None:
    """
    Function to plot frequency of categorical variable per feature category
    """

    # Grouping by the feature and category feature to get counts
    grouped = df.groupby([feature, category_feature]).size().reset_index(name="counts")

    # Plot the bar chart
    fig = px.bar(grouped, x=feature, y="counts", color=category_feature, text="counts")

    fig.update_layout(
        title=f"<b>Frequency of values in {feature} per {category_feature}",
        xaxis=dict(title=f"{feature}"),
        yaxis=dict(title="Count"),
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(
            f"{VIZUALIZATION_DIR}/bar_frequency_{feature}_per_{category_feature}.png",
            format="png",
        )
        if save
        else fig.show()
    )


def plot_scatter(
    df: pd.DataFrame, x_feature: str, y_feature: str, save: bool = False
) -> None:
    """
    Function to plot scatter plot of 2 features
    """

    fig = px.scatter(df, x=x_feature, y=y_feature)

    fig.update_layout(
        title=f"<b>Scatter plot of {x_feature} and {y_feature}",
        xaxis=dict(title=f"{x_feature}"),
        yaxis=dict(title=f"{y_feature}"),
        height=600,
        width=1000,
        margin=dict(t=100, l=80),
    )

    (
        fig.write_image(
            f"{VIZUALIZATION_DIR}/scatter_{x_feature}_{y_feature}.png", format="png"
        )
        if save
        else fig.show()
    )


def plot_correlation_heatmap(df: pd.DataFrame, save: bool = False) -> None:
    """
    Function to create a correlation matrix heatmap
    """

    fig = px.imshow(
        round(df.corr(), 3),
        color_continuous_scale="RdBu_r",  # Reverse Red-Blue colormap
        title="Correlation Matrix Heatmap",
        text_auto=True,
        aspect="auto",
    )

    # Update the layout for better appearance
    fig.update_layout(
        title_font=dict(size=20, family="Arial", color="black"),
        title_x=0.5,  # Center the title
        margin=dict(l=40, r=40, t=40, b=40),
    )

    (
        fig.write_image(f"{VIZUALIZATION_DIR}/correlation_matrix.png", format="png")
        if save
        else fig.show()
    )
