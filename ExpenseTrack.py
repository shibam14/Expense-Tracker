def add_expense():
  amount = float(input("Enter the amount spent: "))
  description = input("Enter a brief description: ")
  category = input("Enter the category (food, transportation, entertainment, etc.): ")
  # Store the expense data
  # Add error handling if necessary
expenses = []  # List to store expense dictionaries

def store_expense(expense):
    expenses.append(expense)
    # Optionally, store expenses in a file using JSON
valid_categories = ["food", "transportation", "entertainment", "utilities", "miscellaneous"]

def add_expense():
    # Existing code to get amount and description
    category = input("Enter the category: ").lower()
    if category not in valid_categories:
        print("Invalid category. Please choose from:", valid_categories)
        # Optionally, allow the user to add custom categories
        return
    # Continue with storing the expense
def monthly_summary():
  # Calculate total expenses for each month and display
  pass

def category_summary(category):
  # Calculate total expenses for the given category and display
  pass
def main():
  while True:
      print("Expense Tracker Menu:")
      print("1. Add Expense")
      print("2. Monthly Summary")
      print("3. Category-wise Summary")
      print("4. Exit")

      choice = input("Enter your choice: ")
      if choice == "1":
          add_expense()
      elif choice == "2":
          monthly_summary()
      elif choice == "3":
          category = input("Enter the category: ")
          category_summary(category)
      elif choice == "4":
          break
      else:
          print("Invalid choice. Please try again.")
def add_expense():
  try:
      # Existing code to get amount, description, and category
  except ValueError:
      print("Invalid input. Please enter a valid amount.")
# Function to add expense
def add_expense():
    """
    Prompt the user to input their daily expenses,
    including the amount spent, description, and category.
    """
    # Code implementation

# Main function to run the expense tracker
def main():
    """
    Main function to run the Expense Tracker program.
    Displays a menu and handles user interactions.
    """
    # Code implementation