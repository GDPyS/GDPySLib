from gdpyslib.cryptography import constants
from gdpyslib.cryptography import cipher

def decode(gjp: str) -> str:
    """Decodes a GJP (Geometry Jump Password) encoded password into plaintext."""

    return cipher.xor_str(
        cipher.b64_encode(gjp),
        constants.xor.GJP,
    )

def encode(plaintext: str) -> str:
    """Encodes a plaintext password using the Geometry Jump password format."""

    return cipher.b64_encode(
        cipher.xor_str(
            plaintext,
            constants.xor.GJP,
        )
    )
