# Organizador de Arquivos

Este projeto é um organizador de arquivos com interface gráfica, desenvolvido em Python utilizando Tkinter. Ele permite selecionar uma pasta, escolher categorias de arquivos (imagens, documentos, vídeos, etc.), visualizar uma prévia dos arquivos que serão movidos e realizar a organização de forma prática e segura.

## Funcionalidades

- Interface gráfica intuitiva com Tkinter
- Seleção de categorias de arquivos a serem organizados
- Pré-visualização dos arquivos que serão movidos
- Organização automática em subpastas por categoria
- Log das movimentações para possível desfazer
- Suporte a múltiplas extensões e tipos de arquivos

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/Vini9-6/organizador-arquivos.git
   cd organizador-arquivos
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

## Como usar

1. Execute o programa:
   ```sh
   python main.py
   ```
2. Na interface, clique em **Selecionar Pasta** e escolha a pasta que deseja organizar.
3. Marque/desmarque as categorias desejadas.
4. Confira a prévia dos arquivos que serão movidos.
5. Clique em **Organizar Arquivos** para executar a organização.

## Estrutura de Pastas

```
organizador-arquivos/
│
├── main.py
├── requirements.txt
└── README.md
```

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Vini9-6](https://github.com/Vini9-6)
