import webbrowser
import os
import readline  # For enabling tab-completion of file paths

# Store the user's preferred browser globally
preferred_browser = None

def print_ascii_art():
    """Print an ASCII art for URLsOpener."""
    art = r"""
 _   _ ___   _        __                                     
| | | |  _ \| |      / _ \ _ __   ___ _ __   ___ _ __ 
| | | | |_) | |     | | | | '_ \ / _ \ '_ \ / _ \ '__|
| |_| |  _ <| |___  | |_| | |_) |  __/ | | |  __/ |   
 \___/|_| \_\_____|  \___/| .__/ \___|_| |_|\___|_|   
                          |_|                         
    """
    print(art)

def set_preferred_browser():
    """Allow the user to select a preferred browser."""
    global preferred_browser

    print("Choose a browser to open URLs (or press Enter to use the default browser):")
    print("1. Brave")
    print("2. Chrome")
    print("3. Firefox")
    print("4. Edge")
    print("5. Default")

    choice = input("Enter your choice (1-5): ").strip()

    browsers = {
        "1": "brave",
        "2": "chrome",
        "3": "firefox",
        "4": "edge",
        "5": None  # Use default browser
    }

    preferred_browser = browsers.get(choice, None)

    if preferred_browser:
        print(f"Preferred browser set to: {preferred_browser}")
    else:
        print("Using the default browser.")

def open_urls(urls):
    """Open a list of URLs in the selected browser."""
    global preferred_browser

    for url in urls:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url  # Ensure the URL has a protocol
        print(f"Opening: {url}")

        if preferred_browser:
            try:
                webbrowser.get(preferred_browser).open(url)
            except webbrowser.Error:
                print(f"Error: Could not open URL with {preferred_browser}. Falling back to default browser.")
                webbrowser.open(url)
        else:
            webbrowser.open(url)

def load_urls_from_file(file_path):
    """Load URLs from a file, one URL per line."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    
    with open(file_path, "r") as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

def enable_tab_completion():
    """Enable tab-completion for file paths."""
    readline.parse_and_bind("tab: complete")
    readline.set_completer_delims(' \t\n;')

def main():
    global preferred_browser

    enable_tab_completion()
    print_ascii_art()

    print("Choose an option:")
    print("1. Enter URLs manually")
    print("2. Load URLs from a file")
    print("3. Set preferred browser")

    choice = input("Enter your choice (1, 2, or 3): ").strip()
    urls = []

    if choice == "1":
        print("Enter URLs one by one. Type 'done' (case insensitive) to finish:")
        while True:
            url = input("Enter URL (or 'done' to finish): ").strip()
            if url.lower() == "done":
                break
            urls.append(url)
    elif choice == "2":
        file_path = input("Enter the file path (tab-completion enabled): ").strip()
        urls = load_urls_from_file(file_path)
    elif choice == "3":
        set_preferred_browser()
        return
    else:
        print("Invalid choice.")
        return

    if urls:
        open_urls(urls)
        print("All URLs have been opened. Exiting...")
    else:
        print("No URLs to open. Exiting...")

if __name__ == "__main__":
    main()