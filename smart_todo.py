# smart_todo.py

# 1. Define our simple "Brain" (Knowledge Base)
# We map keywords to categories.
categories = {
    "groceries": ["milk", "eggs", "bread", "cheese", "apple", "banana", "food"],
    "work": ["report", "meeting", "email", "client", "project", "deadline"],
    "study": ["exam", "assignment", "homework", "chapter", "read", "math"],
    "home": ["clean", "laundry", "fix", "water", "plants"]
}

def categorize_task(task):
    """
    This function looks at a task and guesses the category.
    """
    task = task.lower() # Convert to lowercase to make matching easier
    
    # Check every category in our 'brain'
    for category, keywords in categories.items():
        for word in keywords:
            if word in task:
                return category
    
    return "general" # If no keyword matches

# 2. Main Loop (The App Interface)
todo_list = []

print("--- AI To-Do List (Type 'exit' to stop) ---")

while True:
    user_input = input("\nEnter a task: ")
    
    if user_input.lower() == 'exit':
        break
    
    # The AI Magic happens here
    predicted_category = categorize_task(user_input)
    
    # Add to list
    todo_list.append({"task": user_input, "category": predicted_category})
    
    print(f"✅ Added to [{predicted_category.upper()}] list!")

# 3. Show final list
print("\n--- Final List ---")
for item in todo_list:
    print(f"- {item['task']} ({item['category']})")