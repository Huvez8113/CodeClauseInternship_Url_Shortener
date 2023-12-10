import tkinter as tk
import pyshorteners as py

root = tk.Tk()

root.title("URL Shortener")

root.geometry("300x250")

def shorten():
    shortener = py.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    shorturl_entry.insert(0,short_url)

longurl_label = tk.Label(root,text="Enter the Long URL")
longurl_entry = tk.Entry(root)
longurl_label.pack(padx=10,pady=10)
longurl_entry.pack(padx=10,pady=10)

shorturl_label = tk.Label(root,text="Shortened URL Is")
shorturl_entry = tk.Entry(root)
shorturl_label.pack(padx=10,pady=10)
shorturl_entry.pack(padx=10,pady=10)

shorten_button = tk.Button(root,text="Shorten URL",command=shorten)
shorten_button.pack(padx=10,pady=10)

root.mainloop()