import os
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import askdirectory

# dicionario de categorias e extensoes
locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".svg"],
    "planilha": [".xlsx", ".xls", ".ods"],
    "pdf": [".pdf"],
    "csv": [".csv"],
    "documento": [".doc", ".docx", ".txt", ".odt", ".rtf", ".ppt", ".pptx"],
    "video": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm"],
    "audio": [".mp3", ".wav", ".aac", ".ogg", ".wma", ".flac", ".m4a"],
    "zipados": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
}


class OrganizadorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Organizador de Arquivos")
        self.geometry("600x500")
        self.caminho = ""
        self.selecionadas = {}
        self.arquivos_preview = []

        # botao para selecionar pasta
        self.btn_pasta = ttk.Button(
            self, text="Selecionar Pasta", command=self.selecionar_pasta)
        self.btn_pasta.pack(pady=10)

        # frame para categorias
        self.frame_categorias = ttk.LabelFrame(self, text="Categorias")
        self.frame_categorias.pack(fill="x", padx=10, pady=5)
        for cat in locais:
            var = tk.BooleanVar(value=True)
            chk = ttk.Checkbutton(self.frame_categorias, text=cat.capitalize(
            ), variable=var, command=self.atualizar_preview)
            chk.pack(side="left", padx=5)
            self.selecionadas[cat] = var

        # lista de previa dos arquivos
        self.lbl_preview = ttk.Label(self, text="Arquivos que serao movidos:")
        self.lbl_preview.pack(pady=(10, 0))
        self.lst_preview = tk.Listbox(self, height=15)
        self.lst_preview.pack(fill="both", expand=True, padx=10, pady=5)

        # botao para confirmar organizacao
        self.btn_confirmar = ttk.Button(
            self, text="Organizar Arquivos", command=self.organizar)
        self.btn_confirmar.pack(pady=10)

    def selecionar_pasta(self):
        # abre dialogo para selecionar pasta
        self.caminho = askdirectory(title="Selecione uma pasta")
        self.atualizar_preview()

    def atualizar_preview(self):
        # atualiza a lista de previa dos arquivos que serao movidos
        self.lst_preview.delete(0, tk.END)
        self.arquivos_preview.clear()
        if not self.caminho:
            return
        lista_arquivos = os.listdir(self.caminho)
        for arquivo in lista_arquivos:
            caminho_arquivo = os.path.join(self.caminho, arquivo)
            if not os.path.isfile(caminho_arquivo):
                continue
            nome, extensao = os.path.splitext(arquivo)
            if not extensao:
                continue
            for cat, extensoes in locais.items():
                if self.selecionadas[cat].get() and extensao.lower() in extensoes:
                    self.lst_preview.insert(tk.END, f"{arquivo} → {cat}/")
                    self.arquivos_preview.append((arquivo, cat))
                    break

    def organizar(self):
        # move os arquivos para as pastas correspondentes e salva o log
        if not self.caminho or not self.arquivos_preview:
            messagebox.showwarning(
                "Aviso", "Selecione uma pasta e categorias validas.")
            return
        log_path = os.path.join(self.caminho, "log_movimentacoes.txt")
        with open(log_path, "w", encoding="utf-8") as log_file:
            for arquivo, cat in self.arquivos_preview:
                caminho_arquivo = os.path.join(self.caminho, arquivo)
                destino_pasta = os.path.join(self.caminho, cat)
                if not os.path.exists(destino_pasta):
                    os.mkdir(destino_pasta)
                destino_arquivo = os.path.join(destino_pasta, arquivo)
                if not os.path.exists(destino_arquivo):
                    os.rename(caminho_arquivo, destino_arquivo)
                    log_file.write(f"{destino_arquivo}|{caminho_arquivo}\n")
        messagebox.showinfo("Concluido", "Arquivos organizados com sucesso!")
        self.atualizar_preview()


if __name__ == "__main__":
    # inicializa o aplicativo
    app = OrganizadorApp()
    app.mainloop()
