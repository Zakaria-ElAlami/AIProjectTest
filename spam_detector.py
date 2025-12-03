# spam_detector.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. The Dataset (Usually this is a CSV file)
# We act as the "Teacher" providing examples.
data = {
    'text': [
        "Meeting is at 5pm today",             # Ham (Normal)
        "Win a free iPhone now!",              # Spam
        "Can we have lunch together?",         # Ham
        "Congratulations you won a lottery",   # Spam
        "Please review the attached report",   # Ham
        "URGENT! You have a cash prize waiting", # Spam
        "Hey, how are you doing?",             # Ham
        "Click here to claim your money",      # Spam
        "Don't forget the assignment deadline",# Ham
        "Free entry in a weekly competition"   # Spam
    ],
    'label': [
        "ham", "spam", "ham", "spam", "ham", "spam", "ham", "spam", "ham", "spam"
    ]
}

# Convert dictionary to a nice Table (DataFrame)
df = pd.DataFrame(data)

# 2. Preprocessing: Converting Words to Numbers (Vectorization)
# Machines cannot read text. They only understand numbers.
# "CountVectorizer" counts how many times each word appears.
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text']) # The Inputs (Features)
y = df['label']                          # The Answers (Targets)

# 3. Training the Model
# We use Naive Bayes, a famous algorithm for text (it calculates probabilities)
model = MultinomialNB()
model.fit(X, y)

print("🤖 Model Trained Successfully!")

# 4. The Real Test
# Let's give it sentences it has NEVER seen before.
new_emails = [
    "Hey, do you want to study later?",
    "YOU WON A FREE CAR CLICK HERE",
    "Please send me the project files",
    "Win cash instantly"
]

# We must transform these new emails using the SAME rules (vectorizer) as before
X_new = vectorizer.transform(new_emails)
predictions = model.predict(X_new)

print("\n--- AI Predictions ---")
for email, category in zip(new_emails, predictions):
    print(f"📩 Content: '{email}'\n   🏷️  AI says: {category.upper()}\n")