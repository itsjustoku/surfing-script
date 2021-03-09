import webbrowser
import time
video = input("Search in google :-")
time.sleep(1.5)
print("Searching in process")
time.sleep(2.5)
print("Fetching results...")
time.sleep(2)
webbrowser.open_new_tab("https://www.google.com/search?q=" + video)
