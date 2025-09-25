name = input("Enter your name  ")
try:
    print(name)
except Exception as e:
    print("Exception occurred", e)
    print(name)
name = None  # Typo here, should be `name = None`
