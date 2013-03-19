import Crypto.Hash.HMAC
import Crypto.Protocol.KDF

from .hashes import SHA1, SHA512


def pbkdf2_sha1(password, salt, length, iterations):
    prf = lambda p,s: Crypto.Hash.HMAC.new(p, s, digestmod=SHA1).digest()
    return Crypto.Protocol.KDF.PBKDF2(password=password, salt=salt, dkLen=length, count=iterations, prf=prf)


def pbkdf2_sha512(password, salt, length, iterations):
    prf = lambda p,s: Crypto.Hash.HMAC.new(p, s, digestmod=SHA512).digest()
    return Crypto.Protocol.KDF.PBKDF2(password=password, salt=salt, dkLen=length, count=iterations, prf=prf)
