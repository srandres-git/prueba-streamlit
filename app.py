import streamlit as st
import pandas as pd
st.title("Pruebas de Streamlit")

def dynamic_table(
    df: pd.DataFrame,
    rows: list[str],
    cols: list[str],
    values: dict[str, str],  # {column: aggfunc}
    filters: dict[str, list],
    container
):
    """
    Create a dynamic pivot-like table in Streamlit with filters.

    Args:
        df: DataFrame
        rows: list of columns to use as rows
        cols: list of columns to use as columns
        values: dict of {column: aggfunc}
        filters: dict of {column: list of preselected values}
        container: Streamlit container to display the table
    """

    # --- Filtering widgets ---
    filtered_df = df.copy()
    for col, preselected in filters.items():
        unique_vals = df[col].dropna().unique().tolist()
        selected = container.multiselect(
            f"Filter {col}",
            options=unique_vals,
            default=preselected
        )
        if selected:
            filtered_df = filtered_df[filtered_df[col].isin(selected)]

    # --- Pivot table ---
    pivot_df = pd.pivot_table(
        filtered_df,
        index=rows if rows else None,
        columns=cols if cols else None,
        values=list(values.keys()),
        aggfunc=values,
        fill_value=0
    )

    # Reset index so it shows nicely in Streamlit
    pivot_df = pivot_df.reset_index()

    # --- Display ---
    container.dataframe(pivot_df)


# ---------------- Example usage ---------------- #
st.title("Dynamic Pivot Table Example")

# Example DataFrame
data = {
    "Region": ["North", "North", "South", "South", "East", "East"],
    "Product": ["A", "B", "A", "B", "A", "B"],
    "Sales": [100, 150, 200, 250, 300, 350],
    "Quantity": [10, 15, 20, 25, 30, 35],
}
df = pd.DataFrame(data)

# Define config
rows = ["Region"]
cols = ["Product"]
values = {"Sales": "sum", "Quantity": "mean"}
filters = {"Region": ["North", "South"]}  # preselected filters

container = st.container()
dynamic_table(df, rows, cols, values, filters, container)
