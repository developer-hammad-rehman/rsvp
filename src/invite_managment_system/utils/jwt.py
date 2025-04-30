from jose import jwt
from ..config.env_config import SECRET_KEY, ALGORITHM

class JWTUtils:
    @staticmethod
    def create_jwt_token(data: dict, expires_delta: int) -> str:
        """
        Create a JWT token with the given data and expiration time.

        Args:
            data (dict): The data to include in the token.
            expires_delta (int): The expiration time in seconds.

        Returns:
            str: The generated JWT token.
        """
        to_encode = data.copy()
        to_encode.update({"exp": expires_delta})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def decode_jwt_token(token: str) -> dict:
        """
        Decode a JWT token and return the payload.

        Args:
            token (str): The JWT token to decode.

        Returns:
            dict: The decoded payload.
        """
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])