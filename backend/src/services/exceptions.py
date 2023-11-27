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


class SummarizeException(HTTPException):
    """
    Exceção quando não consegue efetuar a sumarização

    Args:
        detail (str): Mensagem personalizada para a exceção.
    """

    def __init__(self, detail: str = "Erro ao efetuar a sumarização do texto"):
        super().__init__(status_code=500, detail=detail)


class ApiKeyException(HTTPException):
    """
    Exceção API_KEY está invalida ou sem saldo

    Args:
        detail (str): Mensagem personalizada para a exceção.
    """

    def __init__(self, detail: str = "API_KEY invalida ou sem saldo para uso"):
        super().__init__(status_code=401, detail=detail)


class NotFoundException(HTTPException):
    """
    Exceção API_KEY está invalida ou sem saldo

    Args:
        detail (str): Mensagem personalizada para a exceção.
    """

    def __init__(self, detail: str = "Arquivo não encontrado"):
        super().__init__(status_code=404, detail=detail)
