source lenv/bin/activate  # For Linux/macOS

pip install -r requirements.txt

llm_summarizer/
│
├── server.py           # FastAPI server with endpoints
├── summarizer.py       # Summarization logic (Hugging Face model)
├── config.json         # Configurations (e.g., default model, port)
├── utils.py            # Utility functions (e.g., load config, env)
├── .env                # API keys and sensitive data
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation


uvicorn server:app --reload


