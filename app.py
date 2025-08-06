# app_gradio.py
import pickle
import numpy as np
import gradio as gr

# Load artifacts
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Hardcoded selected features from training step
features = ["MedInc", "AveRooms", "AveOccup", "HouseAge"]  # Example from California dataset

title = "🏠 House Price Estimator (Ridge Regression)"
description = f"Predicts median house value (in $100,000s) using {', '.join(features)}."

# Prediction function
def predict(*vals):
    arr = np.array(vals).reshape(1, -1)
    arr_scaled = scaler.transform(arr)
    pred = model.predict(arr_scaled)[0]
    return {
        "Predicted Value (in $100k units)": round(pred, 3),
        "Predicted Value (USD)": round(pred * 100000, 2)
    }

# Build Gradio interface
inputs = [gr.Number(label=f, value=1.0, precision=3) for f in features]
output = gr.JSON(label="Prediction")


iface = gr.Interface(
    fn=predict,
    inputs=inputs,
    outputs=output,
    title=title,
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch()
