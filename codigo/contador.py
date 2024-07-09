import os
import time
import customtkinter as CTk
from collections import defaultdict
import threading
import json
from PIL import ImageFont

stop_thread = False  # Variável de controle global

def load_config(config_file=r"settings\config.json"):
    """Carrega as configurações do arquivo JSON."""
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config.get("allowed_extensions", [])
    except Exception as e:
        print(f"Erro ao carregar o arquivo de configuração: {e}")
        return []

def count_non_blank_lines(file_path):
    """Conta o número de linhas não em branco em um arquivo."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            non_blank_lines = [line for line in lines if line.strip()]
        return len(non_blank_lines)
    except Exception as e:
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        return 0

def rank_files_by_extension(directory, allowed_extensions):
    """Classifica os arquivos por extensão com base no número de linhas não em branco."""
    extension_count = defaultdict(int)

    # Explora o diretório e suas subpastas
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file_path)
            if ext in allowed_extensions:
                non_blank_lines = count_non_blank_lines(file_path)
                extension_count[ext] += non_blank_lines

    # Classifica as extensões por número de linhas não em branco
    ranked_extensions = sorted(extension_count.items(), key=lambda x: x[1], reverse=True)
    return ranked_extensions

def update_display(ranking, textbox):
    """Atualiza o frame de labels com a classificação das extensões."""
    textbox.configure(state="normal")  # Habilita edição para atualizar o conteúdo
    textbox.delete("1.0", CTk.END)  # Limpa o conteúdo atual
    header = f"{'Extension':<15} {'Lines':<15}\n"
    separator = "▬" * 30 + "\n"
    textbox.insert(CTk.END, header)
    textbox.insert(CTk.END, separator)
    for ext, count in ranking:
        line = f"{ext:<15} {count:<15}\n"
        textbox.insert(CTk.END, line)
    textbox.insert(CTk.END, separator)
    textbox.configure(state="disabled")  # Desabilita edição para evitar modificações

def main_function(directory, interval, textbox, allowed_extensions):
    """Função principal que atualiza o ranking a cada intervalo."""
    global stop_thread
    while not stop_thread:
        ranking = rank_files_by_extension(directory, allowed_extensions)
        update_display(ranking, textbox)
        time.sleep(interval)

def start_counting(directory_entry, interval, textbox, allowed_extensions):
    """Inicia a contagem de linhas e a atualização do ranking."""
    global stop_thread
    stop_thread = False  # Resetar a variável de controle
    directory = directory_entry.get()
    if not os.path.isdir(directory):
        textbox.configure(state="normal")
        textbox.insert(CTk.END, "Diretório inválido.\n")
        textbox.configure(state="disabled")
        return
    # Usa threading para não bloquear a interface gráfica
    thread = threading.Thread(target=main_function, args=(directory, interval, textbox, allowed_extensions))
    thread.daemon = True  # Permite que o programa seja fechado mesmo que a thread esteja rodando
    thread.start()

def main_window():
    """Cria a janela principal da interface gráfica."""
    root = CTk.CTk()
    root.geometry('400x450')
    root.title('Contador de Linhas')

    # Definir o caminho para o arquivo da fonte .ttf
    font_path = r".settings\consolaz.ttf"  # Substitua pelo caminho real para o arquivo Consolas.ttf

    # Registrar a fonte Consolas a partir do arquivo .ttf
    try:
        font = ImageFont.truetype(font_path, 12)  # Definindo o tamanho da fonte
        CTk.set_appearance_mode("dark")  # Se desejar usar o modo escuro
    except IOError:
        print(f"Fonte não encontrada em {font_path}. Usando fonte padrão.")

    # Carrega as configurações
    allowed_extensions = load_config()

    # Frame para exibir o ranking
    textbox = CTk.CTkTextbox(root, width=380, height=350, font=("Consolas", 12))
    textbox.pack(pady=20)

    # Frame para o campo de entrada e o botão de início
    input_frame = CTk.CTkFrame(root)
    input_frame.pack(pady=10)

    # Rótulo e campo de entrada para o diretório
    directory_label = CTk.CTkLabel(input_frame, text="Diretório:")
    directory_label.pack(side=CTk.LEFT, padx=5)

    directory_entry = CTk.CTkEntry(input_frame, width=200)
    directory_entry.pack(side=CTk.LEFT, padx=5)

    interval = 30  # Intervalo de 30 segundos

    # Botão para iniciar a contagem
    start_button = CTk.CTkButton(input_frame, text="start", command=lambda: start_counting(directory_entry, interval, textbox, allowed_extensions))
    start_button.pack(side=CTk.LEFT, padx=5)

    root.mainloop()

    # Fechamento do programa, garantindo que a thread daemon pare
    global stop_thread
    stop_thread = True

if __name__ == '__main__':
    main_window()
