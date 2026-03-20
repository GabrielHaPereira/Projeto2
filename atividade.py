import tkinter as tk
from tkinter import font

# criar janela
janela = tk.Tk()

# título da janela
janela.title("Minha Primeira Janela")

# tamanho da janela
janela.geometry("400x200")

# carregar imagem
imagem = tk.PhotoImage(file="C:\Users\1052028\Desktop\378-3780451_sticker-risitas-bolsonaro-heureux-victoire-jair-bolsonaro.png")

# mostrar imagem
label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack()


# criar fonte em negrito
fonte_negrito = font.Font(size=14, weight="bold")

# criar etiqueta
etiqueta = tk.Label(
    janela,
    text="Fredy the best teacher!",
    font=fonte_negrito
)

# posicionar etiqueta
etiqueta.pack(pady=40)

# loop da janela
janela.mainloop()