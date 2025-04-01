import customtkinter as ctk
import pyshorteners

def shorten_url():
    url = entry.get()  # Get the URL from the input box
    if url:
        try:
            # Use pyshorteners to shorten the URL
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            result_label.configure(text=f"Shortened URL: {short_url}")
        except Exception as e:
            result_label.configure(text=f"Error: {str(e)}")

app = ctk.CTk()
app.geometry("700x200")
app.title("URL Shortener")

ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"

label = ctk.CTkLabel(app, text="Enter URL to shorten:", font=("Arial", 14))
label.pack(pady=10)

entry = ctk.CTkEntry(app, width=300, font=("Arial", 12))
entry.pack(pady=5)

shorten_button = ctk.CTkButton(app, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
result_label.pack(pady=20)

app.mainloop()
