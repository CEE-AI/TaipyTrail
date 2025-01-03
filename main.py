from taipy.gui import Gui
import taipy.gui.builder as tgb
import pandas as pd

# Sample data for visual components
data = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
metric_value = 75
progress_value = 50
indicator_value = 70

# Define the page
with tgb.Page() as page:
    # We will add components here one by one
	tgb.chart("{data}", x="x", y="y", type="bar", title="Bar Chart Example")
    # Table: Displays tabular data with sorting and filtering options
tgb.table("{data}", filter=True, number_format="%.0f")  # Use editable=True to allow user modifications
 # Metric: Highlights a specific numeric value with a title
tgb.metric("{metric_value}", title="Completion", min=0, max=100)  # Add delta=5 to show changes type=”linear” for linear metric
# Run the application
Gui(page).run(debug=True)