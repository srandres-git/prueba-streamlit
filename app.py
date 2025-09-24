import streamlit as st
import pandas as pd
st.title("Pruebas de Streamlit")

def dynamic_table(
    df: pd.DataFrame,
    rows: list[str],
    cols: list[str],
    values: dict[str, str],  # {column: aggfunc}
    filters: dict[str, list],
    container,
    format_func: callable = None,
    sort_args: list = None,
    top_n: int = None,
    bottom_n: int = None,
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
        format_func: Optional function to format cell values
        sort_args: Optional list of args for sorting the final table
        top_n: Optional int to show only top N rows
        bottom_n: Optional int to show only bottom N rows
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
    # sort the table if args provided
    if sort_args:
        pivot_df = pivot_df.sort_values(*sort_args)
    # show only top N rows if specified
    if top_n:
        pivot_df = pivot_df.head(top_n)
    # show only bottom N rows if specified
    if bottom_n:
        pivot_df = pivot_df.tail(bottom_n)
    # Reset index and start it on 1 so it shows nicely in Streamlit
    pivot_df = pivot_df.reset_index()
    pivot_df.index += 1
     # Apply formatting function if provided
    if format_func:
        pivot_df = pivot_df.applymap(format_func)
    # 

    # --- Display ---
    container.table(pivot_df, border='horizontal')

def format_currency(x):
    if isinstance(x, (int, float)):
        return f"${x:,.2f}"
    return x

def format_region(x):
    if x=="North":
        return f":blue[{x}]"
    elif x=="South":
        return f":red[{x}]"
    return x
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
dynamic_table(df, rows, cols, values, filters, container, format_func=lambda x: format_region(format_currency(x)),
              sort_args=["Region", False], top_n=5)
