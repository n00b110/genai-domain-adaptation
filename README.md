# Domain Adapted AI Assistant

This project demonstrates domain adaptation using LoRA fine-tuning.

Pipeline:

User -> Streamlit -> FastAPI -> Fine-tuned model

Steps:

1. Install dependencies

pip install -r requirements.txt

2. Train model

python training/train_lora.py

3. Start API

uvicorn app.api:app --reload

4. Run Streamlit

streamlit run app/streamlit_app.py
