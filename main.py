import tkinter as tk
import package.config as cfg
from package.app import App
from package.mainframe import MainFrame        

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