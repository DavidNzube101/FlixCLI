import subprocess
import sys

def main():
    if len(sys.argv) < 2 or sys.argv[1] != "-d":
        print("Usage: flixcli -d")
        return

    url = input("Enter the URL to scrape media files from: ")

    try:
        # Call the Java script's main() method
        subprocess.run(["mvn", "exec:java", "-Dexec.mainClass=com.skipp.flixcore.flixcore", f"-Dexec.args={url}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Java script: {e}")

if __name__ == "__main__":
    main()