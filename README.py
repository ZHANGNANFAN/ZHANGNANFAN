import tkinter as tk
def add_item(ncmd):
    
    
    frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
    frame1.pack(fill=tk.BOTH)
    
    # EMBED WIDGET HERE
    label = tk.Label(
        master = frame1,
        text = entry.get()[0]
    )
    label.pack(side =tk.LEFT)
    for text in label:#input the number to get the 
        out = f'[{label.index(text)}] {text[0]}'
    
    bnt = tk.Button(
        text = "done",
        width = 40,
        master = frame1,
        foreground = 'blue'
    )
    bnt.pack(side = tk.RIGHT)
    
    
    def done(event):
        event.widget.master.destory()
    bnt.bind("<Button-1>",done)





    
window = tk.Tk()

entry = tk.Entry(fg="black", bg="white", width=20)
entry.pack()

bnt1 = tk.Button(text = "add item",
    width = 20,
    master = window,
    foreground = 'blue'
    
               )
bnt1.pack(side = tk.RIGHT)

bnt2 = tk.Button(text = "remove item",
    width = 20,
    master = window,
    foreground = 'blue'
    
               )
bnt2.pack(side = tk.RIGHT)


bnt1.bind("<Button-1>",add_item )




window.mainloop()
