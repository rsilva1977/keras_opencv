# Importa a função para carregar modelos do Keras (requer TensorFlow)
from keras.models import load_model
# Importa a biblioteca OpenCV para captura e processamento de imagem
import cv2
# Importa a biblioteca NumPy para manipulação de arrays
import numpy as np

# Desativa a notação científica para melhor legibilidade dos outputs
np.set_printoptions(suppress=True)

# Carrega o modelo pré-treinado a partir do ficheiro "keras_model.h5"
# compile=False indica que o modelo não será recompilado após o carregamento
model = load_model("keras_model.h5", compile=False)

# Carrega os nomes das classes a partir do ficheiro "labels.txt"
# Cada linha do ficheiro corresponde a uma classe (ex: "cachorro", "gato", etc.)
class_names = open("labels.txt", "r").readlines()

# Inicializa a captura de vídeo a partir da webcam (0 é o índice padrão para a webcam integrada)
camera = cv2.VideoCapture(0)

# Loop infinito para captura contínua de imagens
while True:
    # Captura um frame da webcam
    # ret: booleano que indica se a captura foi bem-sucedida
    # image: o frame capturado
    ret, image = camera.read()

    # Redimensiona a imagem para 224x224 pixels (tamanho esperado pelo modelo)
    # INTER_AREA é o método de interpolação usado para redimensionamento
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Mostra a imagem redimensionada numa janela com o título "Webcam Image"
    cv2.imshow("Webcam Image", image)

    # Converte a imagem para um array NumPy do tipo float32
    # e remodela para o formato esperado pelo modelo: (1, 224, 224, 3)
    # 1: batch size (número de imagens a processar de uma vez)
    # 224, 224: altura e largura
    # 3: canais de cor (RGB)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normaliza os valores dos pixels para o intervalo [-1, 1]
    # Divide por 127.5 e subtrai 1 para centrar os valores em 0
    image = (image / 127.5) - 1

    # Faz a previsão do modelo com a imagem processada
    prediction = model.predict(image)

    # Obtém o índice da classe com maior probabilidade
    index = np.argmax(prediction)

    # Obtém o nome da classe correspondente ao índice
    # [2:] remove os primeiros dois caracteres (ex: "\n" no início de cada linha do ficheiro)
    class_name = class_names[index]

    # Obtém o score de confiança (probabilidade) da previsão
    confidence_score = prediction[0][index]

    # Imprime o nome da classe e o score de confiança arredondado a 2 casas decimais
    print("Classe:", class_name[2:], end="")
    print("Score de Confiança:", str(np.round(confidence_score * 100))[:-2], "%")

    # Aguarda 1 milissegundo por input do teclado
    keyboard_input = cv2.waitKey(1)

    # Se a tecla ESC (código ASCII 27) for pressionada, sai do loop
    if keyboard_input == 27:
        break

# Liberta os recursos da câmara
camera.release()
# Fecha todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
