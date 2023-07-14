import tkinter as tk
import config as cfg
from app import App
from mainframe import MainFrame        

app = App(
    window_size=cfg.APP_SIZE, 
    icon_img=cfg.APP_ICO, 
    title=cfg.APP_TITLE
)

frame = MainFrame(
    app,
    bg=cfg.MAIN_BG_COLOR, 
    padx=20,
    pady=20, 
    borderwidth=1, 
    relief="solid"
)

app.mainloop()