def chose_model():
    choice = input("Enter model name (cbow/skip): ").strip().lower()
    if choice == "cbow":
        return 0  
    elif choice == "skip":
        return 1  
    else:
        print("Invalid choice, defaulting to CBOW")
        return 0