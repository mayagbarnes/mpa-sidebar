import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from datetime import datetime
from datetime import date

st.set_page_config(page_title='Home', initial_sidebar_state='expanded')

st.sidebar.header('Sidebar ⚡')
w1 = st.date_input("Label 1", date(1970, 1, 1))
st.write("Value 1:", w1)

st.sidebar.color_picker("Pick a Color", value="#464AB3")

y = st.sidebar.text_input("type here")

w2 = st.sidebar.date_input("Date Input", datetime(2019, 7, 6, 21, 15))
st.write("Value 2:", w2)


interactive_scatter_spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Drag the sliders to highlight points.",
  "title": f"Interactive Scatter Chart",
  "data": {"url": "https://vega.github.io/vega-datasets/data/cars.json"},
  "transform": [{"calculate": "year(datum.Year)", "as": "Year"}],
  "layer": [{
    "params": [{
      "name": "CylYr",
      "value": [{"Cylinders": 4, "Year": 1977}],
      "select": {"type": "point", "fields": ["Cylinders", "Year"]},
      "bind": {
        "Cylinders": {"input": "range", "min": 3, "max": 8, "step": 1},
        "Year": {"input": "range", "min": 1969, "max": 1981, "step": 1}
      }
    }],
    "mark": "circle",
    "encoding": {
      "x": {"field": "Horsepower", "type": "quantitative"},
      "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
      "color": {
        "condition": {"param": "CylYr", "field": "Origin", "type": "nominal"},
        "value": "grey"
      }
    }
  }, {
    "transform": [{"filter": {"param": "CylYr"}}],
    "mark": "circle",
    "encoding": {
      "x": {"field": "Horsepower", "type": "quantitative"},
      "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
      "color": {"field": "Origin", "type": "nominal"},
      "size": {"value": 100}
    }
  }]
}

st.vega_lite_chart(interactive_scatter_spec, None, use_container_width=True)