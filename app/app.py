import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("../model.pkl")

# # with st.form("predict"):
# #     #locality,area,rent,price_per_sqft,facing,BHK,bathrooms,parking
# #     rent = st.number_input("Monthly Rent", value=20060)
# #     area = st.number_input("Area", value=565)
# #     locality = st.text_input("Locality (e.g., BTM Layout)", "BTM Layout")
# #     Bedrooms = st.number_input("BHK", value=1, min_value=0, max_value=10, step=1)
# #     facing = st.text_input("Facing (e.g., North)", "North-West")
# #     parking = st.selectbox("Parking", ["None", "Car", "Bike", "Car and Bike"])
# #     bathrooms = st.number_input("Bathroom", value=1)
# #     submitted = st.form_submit_button("Predict")


with st.form("predict"):
    # Locality dropdown (manually entered)
    locality = st.selectbox(
        "Select Locality",
        [
            "Attibele", "BTM Layout", "Electronic City", "Indiranagar",
            "Jayanagar", "K R Puram", "Malleshwaram", "Marathahalli", "Yalahanka"
        ],
        index=1  # Default: BTM Layout
    )

    # Area slider (approx range from dataset)
    area = st.slider(
        "Area (sqft)",
        200, 5000, 565
    )

    # Rent slider (approx range from dataset)
    rent = st.slider(
        "Monthly Rent (₹)",
        5000, 200000, 20060, step=500
    )

    # BHK slider
    Bedrooms = st.slider("BHK", 1, 5, 1)

    # Bathrooms slider
    bathrooms = st.slider("Bathrooms", 1, 10, 1)

    # Facing dropdown
    facing = st.selectbox(
        "Facing",
        ["East", "North", "North-East", "North-West", "South", "South-East", "West"],
        index=3  # Default: North-West
    )

    # Parking dropdown
    parking = st.selectbox(
        "Parking",
        ["Bike", "Car", "Bike and Car"]
    )

    # Submit button
    submitted = st.form_submit_button("Predict")

# # import streamlit as st

# # with st.form("predict"):

# #     st.markdown("### 🏠 Property Details")

# #     # Locality dropdown (searchable if many)
# #     locality = st.selectbox(
# #         "📍 Select Locality",
# #         [
# #             "Attibele", "BTM Layout", "Electronic City", "Indiranagar",
# #             "Jayanagar", "K R Puram", "Malleshwaram", "Marathahalli", "Yalahanka"
# #         ],
# #         index=1
# #     )

# #     # Area number input
# #     area = st.number_input(
# #         "📐 Area (sqft)",
# #         min_value=200,
# #         max_value=5000,
# #         value=565,
# #         step=10
# #     )

# #     # Rent number input
# #     rent = st.number_input(
# #         "💰 Monthly Rent (₹)",
# #         min_value=5000,
# #         max_value=200000,
# #         value=20060,
# #         step=500
# #     )

# #     st.markdown("---")
# #     st.markdown("### 🛋️ Interior & Amenities")

# #     # BHK radio buttons
# #     Bedrooms = st.radio("🛏️ BHK", options=list(range(1, 6)), index=0, horizontal=True)

# #     # Bathrooms radio
# #     bathrooms = st.radio("🚿 Bathrooms", options=list(range(1, 6)), index=0, horizontal=True)

# #     # Facing select slider
# #     facing = st.select_slider(
# #         "🧭 Facing",
# #         options=["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"],
# #         value="North-West"
# #     )

# #     # Parking radio
# #     parking = st.radio(
# #         "🚗 Parking",
# #         ["Bike", "Car", "Bike and Car"],
# #         index=0,
# #         horizontal=True
# #     )

# #     submitted = st.form_submit_button("🔮 Predict Rent")

# import streamlit as st

# with st.form("predict"):

#     st.markdown("## 🏠 Property Prediction Form")

#     # ---------------- Property Details ----------------
#     st.markdown("### 📍 Property Details")

#     locality = st.selectbox(
#         "Select Locality",
#         [
#             "Attibele", "BTM Layout", "Electronic City", "Indiranagar",
#             "Jayanagar", "K R Puram", "Malleshwaram", "Marathahalli", "Yalahanka"
#         ],
#         index=1
#     )

#     # Area slider
#     area = st.slider(
#         "📐 Area (sqft)",
#         200, 5000, 565, step=10
#     )

#     # Rent slider
#     rent = st.slider(
#         "💰 Monthly Rent (₹)",
#         5000, 200000, 20060, step=500
#     )

#     # ---------------- Interior & Amenities ----------------
#     st.markdown("---")
#     st.markdown("### 🛋️ Interior & Amenities")

#     # BHK radio buttons
#     Bedrooms = st.radio("🛏️ BHK", options=list(range(1, 6)), index=0, horizontal=True)

#     # Bathrooms radio
#     bathrooms = st.radio("🚿 Bathrooms", options=list(range(1, 6)), index=0, horizontal=True)

#     # Parking radio
#     parking = st.radio(
#         "🚗 Parking",
#         ["Bike", "Car", "Bike and Car"],
#         index=0,
#         horizontal=True
#     )

#     # ---------------- Facing Compass ----------------
#     st.markdown("---")
#     st.markdown("### 🧭 Facing Direction")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         north_west = st.button("↖️ NW")
#         west = st.button("⬅️ W")
#         south_west = st.button("↙️ SW")

#     with col2:
#         north = st.button("⬆️ N")
#         st.markdown("<div style='text-align:center;'>🏠</div>", unsafe_allow_html=True)
#         south = st.button("⬇️ S")

#     with col3:
#         north_east = st.button("↗️ NE")
#         east = st.button("➡️ E")
#         south_east = st.button("↘️ SE")

#     # Store user’s selection
#     facing = None
#     if north: facing = "North"
#     elif south: facing = "South"
#     elif east: facing = "East"
#     elif west: facing = "West"
#     elif north_east: facing = "North-East"
#     elif north_west: facing = "North-West"
#     elif south_east: facing = "South-East"
#     elif south_west: facing = "South-West"

#     if facing:
#         st.success(f"✅ You selected: {facing}")

#     # ---------------- Submit ----------------
#     submitted = st.form_submit_button("🔮 Predict Rent")



if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "area": area,
        "locality": locality ,
        "BHK": Bedrooms,
        "facing":facing if locality else "Missing",
        "bathrooms": bathrooms,
        "parking": parking if parking else "Missing"
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")


# import streamlit as st
# import joblib
# import pandas as pd

# st.title("🏠 House Price Predictor")

# model = joblib.load("../model.pkl")

# with st.form("predict"):

#     st.markdown("## 🏠 Property Prediction Form")

#     # ---------------- Property Details ----------------
#     st.markdown("### 📍 Property Details")

#     locality = st.selectbox(
#         "Select Locality",
#         [
#             "Attibele", "BTM Layout", "Electronic City", "Indiranagar",
#             "Jayanagar", "K R Puram", "Malleshwaram", "Marathahalli", "Yalahanka"
#         ],
#         index=1
#     )

#     # Area slider
#     area = st.slider(
#         "📐 Area (sqft)",
#         200, 5000, 565, step=10
#     )

#     # Rent slider
#     rent = st.slider(
#         "💰 Monthly Rent (₹)",
#         5000, 200000, 20060, step=500
#     )

#     # ---------------- Interior & Amenities ----------------
#     st.markdown("---")
#     st.markdown("### 🛋️ Interior & Amenities")

#     # BHK radio buttons
#     Bedrooms = st.radio("🛏️ BHK", options=list(range(1, 6)), index=0, horizontal=True)

#     # Bathrooms radio
#     bathrooms = st.radio("🚿 Bathrooms", options=list(range(1, 6)), index=0, horizontal=True)

#     # Parking radio
#     parking = st.radio(
#         "🚗 Parking",
#         ["Bike", "Car", "Bike and Car"],
#         index=0,
#         horizontal=True
#     )

#     # ---------------- Facing Compass ----------------
#     st.markdown("---")
#     st.markdown("### 🧭 Facing Direction")

#     # Create a 3x3 compass layout with radios
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         nw = st.radio("", ["↖️ NW", ""], index=1, label_visibility="collapsed")
#         w = st.radio("", ["⬅️ W", ""], index=1, label_visibility="collapsed")
#         sw = st.radio("", ["↙️ SW", ""], index=1, label_visibility="collapsed")

#     with col2:
#         n = st.radio("", ["⬆️ N", ""], index=1, label_visibility="collapsed")
#         st.markdown("<div style='text-align:center;'>🏠</div>", unsafe_allow_html=True)
#         s = st.radio("", ["⬇️ S", ""], index=1, label_visibility="collapsed")

#     with col3:
#         ne = st.radio("", ["↗️ NE", ""], index=1, label_visibility="collapsed")
#         e = st.radio("", ["➡️ E", ""], index=1, label_visibility="collapsed")
#         se = st.radio("", ["↘️ SE", ""], index=1, label_visibility="collapsed")

#     # Extract facing from selection
#     facing = None
#     for option in [nw, w, sw, n, s, ne, e, se]:
#         if option != "":
#             facing = option.split(" ")[1]  # Extract direction text

#     if not facing:
#         facing = "North-West"  # default fallback

#     # ---------------- Submit ----------------
#     submitted = st.form_submit_button("🔮 Predict Rent")

# if submitted:
#     X = pd.DataFrame([{
#         "rent": rent,
#         "area": area,
#         "locality": locality,
#         "BHK": Bedrooms,
#         "facing": facing,
#         "bathrooms": bathrooms,
#         "parking": parking
#     }])
#     pred = model.predict(X)[0]
#     st.success(f"Predicted Price: {pred:,.2f}")
