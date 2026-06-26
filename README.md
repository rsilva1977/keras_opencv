# Classificação de Imagens em Tempo Real com Keras e OpenCV

Um projeto simples para classificar imagens em tempo real usando um modelo pré-treinado do Keras e a webcam do computador.

---

## 📌 Descrição

Este projeto utiliza um modelo de **classificação de imagens** (ex: MobileNet, VGG16, ou outro modelo compatível com Keras) para detetar e classificar objetos em tempo real a partir da webcam. O script captura frames da webcam, processa-os e exibe a classe prevista junto com o *score* de confiança.

---

## 🛠 Requisitos

- Python 3.6 ou superior
- Bibliotecas necessárias:
  - `tensorflow` (ou `keras`)
  - `opencv-python`
  - `numpy`

---

## 📥 Instalação

1. **Clonar o repositório:**
  ```bash
   git clone https://github.com/rsilva1977/keras_opencv.git
   cd keras_opencv
  ```
2. **Instalar as dependências:**
  ```bash
   pip install tensorflow opencv-python numpy
  ```
3. **Preparar os ficheiros necessários:**
  - Colocar o modelo pré-treinado (`keras_model.h5`) na pasta do projeto.
  - Colocar o ficheiro `labels.txt` com os nomes das classes (uma classe por linha).

---

## 🚀 Como Usar

1. **Executar o script:**
  ```bash
   python classificador_imagens.py
  ```
2. **Interagir com o programa:**
  - Uma janela com a imagem da webcam será aberta.
  - O nome da classe detetada e o *score* de confiança serão impressos no terminal.
  - Pressionar **ESC** para sair do programa.

---

## 📂 Estrutura do Projeto

```
.
├── keras_model.h5          # Modelo pré-treinado do Keras
├── labels.txt              # Nomes das classes (uma por linha)
├── classificador_imagens.py # Script principal
└── README.md               # Este ficheiro
```

---

## 🔧 Personalização

- **Modelo:** Substituir `keras_model.h5` pelo teu modelo pré-treinado.
- **Classes:** Atualizar `labels.txt` com as classes correspondentes ao teu modelo.
- **Resolução:** Ajustar o tamanho da imagem no script (`224x224` por padrão) se o teu modelo exigir outra resolução.

---

## 📝 Notas

- O modelo deve estar treinado para **224x224 pixels** e **3 canais de cor (RGB)**.
- O ficheiro `labels.txt` deve conter **uma classe por linha**, na mesma ordem das saídas do modelo.
- Para melhor performance, certifica-te que a webcam está a funcionar corretamente.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sente-te à vontade para abrir *issues* ou *pull requests*.

---

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
