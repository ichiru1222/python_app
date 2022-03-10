import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit first")

st.write("DataFrame")

df = pd.DataFrame({
    "first": [1, 2, 3, 4],
    "second": [10, 20, 30, 40]
})

st.dataframe(df)

"""
# title
## subtitle

```python
import streamlit
```
"""

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=["lat", "lon"]
)

# st.area_chart(df2)

st.map(df2)

st.write("Display image")
if st.checkbox("show image"):
    img = Image.open("01A64370-4D2D-4E42-BE2F-2F1C2B1F3FCF.jpeg")
    st.image(img, caption="test")


st.write("text")

text = st.text_input("who are you?")

"Your name:", text