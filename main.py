import os

def main():
    print("Welcome to the automated CI/CD pipeline example!")
    
    # Example environment variable check
    if os.getenv("CI") == "true":
        print("Running in CI environment")
    else:
        print("Running in local environment")

if __name__ == "__main__":
    main()
