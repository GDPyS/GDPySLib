import base64
from itertools import cycle


def cipher_xor(data: bytes, key: bytes) -> bytes:
    """Encodes `data` using the XOR cipher with the key `key`.
    Args:
        data (bytes): The data that is to be encoded using the XOR cipher.
        key (bytes): The key to be used within the encryption process.
    Returns:
        XOR encoded bytes.
    """
    return bytes(
        byte ^ key_byte for byte, key_byte in zip(data, cycle(key))
    )

def cipher_xor_str(
    data: str,
    key: bytes,
    encoding: str = "utf-8",
    errors: str = "strict",
) -> str:
    """Encodes a given string in using XOR, taking into consideration the
    string encoding itself.
    
    Args:
        data (str): The data string to be encoded.
        key (bytes): The XOR key to be used for the cipher.
        encoding (str): The encoding to be used for the string and result.
        errors (str): Specifies the error handling scheme for encoding errors.
    
    Returns:
        An XOR encoded string.
    """

    return cipher_xor(
        data.encode(encoding, errors),
        key,
    ).decode(encoding, errors)

def cipher_b64_encode(text: str) -> str:
    """Encodes the string `text` using the URL-safe Base64 algorithm.
    Args:
        text (str): The text that is to be encoded using the base64 algorithm.
    Returns:
        str: Base64 encoded string of param `text`.
    """

    return base64.urlsafe_b64encode(text.encode()).decode()
