from fastapi import HTTPException


class FileFormatException(HTTPException):
    """
    Exceção para indicar formato de arquivo inválido em uploads.
    Usada quando um arquivo enviado não está no formato '.mp3' ou '.wav'.

    Args:
        detail (str): Mensagem personalizada para a exceção.
    """

    def __init__(self, detail: str = "Formatos aceitos: '.mp3' ou '.wav'."):
        super().__init__(status_code=400, detail=detail)


class RecognizeException(HTTPException):
    """
    Exceção quando a lib que faz a coversão de audio pra texto apresentar erro

    Args:
        detail (str): Mensagem personalizada para a exceção.
    """

    def __init__(self, detail: str = "Erro ao ler o conteudo do aúdio"):
        super().__init__(status_code=500, detail=detail)
