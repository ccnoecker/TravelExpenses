# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
from pathlib import Path

# %% [markdown]
# ## Load Data

# %%
INPUT_PATH = Path('../input/')
OUTPUT_PATH = Path('../output/')

INPUT_FILENAME = Path('Travel Budget.xlsx')
PATH_TO_DATA = INPUT_PATH.joinpath(INPUT_FILENAME)

TABS_TO_EXCLUDE = ['TOTAL', 'HELP', 'BASE', 'CURRENCY CONVERSIONS']

# %%
all_dataframes = pd.read_excel(PATH_TO_DATA, sheet_name=None, skiprows=11)
f'Loaded Excel tabs: {", ".join(tab_name for tab_name in all_dataframes.keys())}'

# %% [markdown]
# ## Preprocess and then union dataframes

# %%
for tab_name in all_dataframes.keys():
    # Create a column on each dataframe containing the tab name
    all_dataframes[tab_name]['TRIP NAME'] = tab_name.strip()

    # Drop columns that start with "Unnamed" as they should all be empty and/or irrelevant
    all_dataframes[tab_name] = all_dataframes[tab_name].loc[:, ~all_dataframes[tab_name].columns.str.contains('^Unnamed')]

    # Clean column names
    all_dataframes[tab_name].columns = [column.strip().upper() for column in all_dataframes[tab_name].columns]

# %%
# Union all relevant dataframes
dataframes_to_union = [dataframe for tab_name, dataframe in all_dataframes.items() if tab_name.strip().upper() not in TABS_TO_EXCLUDE]
base_dataframe = pd.concat(dataframes_to_union).reset_index()
base_dataframe.info()
