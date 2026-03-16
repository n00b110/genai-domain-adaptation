import requests

questions = [
    "What is deadlock?",
    "Explain semaphore",
    "What is a mutex?"
]

for q in questions:
    r = requests.get(
        "http://localhost:8000/ask",
        params={"question": q}
    )

    print("Question:", q)
    print("Answer:", r.json()["response"])
    print()
