PYTHON_DECODE_STUB_BASE85 = 'from base64 import b85decode as {b}\nvalue ="""{}"""\nexec({b}(v))'
PYTHON_DECODE_STUB_ROT42 = 'v ="""{}"""\neval(''.join(chr((ord({b}) - 42)for {b} in v)))'

RUBY_DECODE_STUB_BASE64 = 'require \'base64\'\nv = """{}"""\nexec(Base64.decode64(v))'
RUBY_DECODE_STUB_ROT42 = 'v = """{}""""\naa = []\nfor {b} in v.split("")\n\taa.push((a.ord - 14).c\
hr)\nend\neval(b.join(""))'


def _get_python_enc_stub(os: str) -> str:
    if "base" in os.lower():
        return PYTHON_DECODE_STUB_BASE85
    if "rot" in os.lower():
        return PYTHON_DECODE_STUB_ROT42

    return ""


def _get_ruby_enc_stub(os: str) -> str:
    if "base" in os.lower():
        return RUBY_DECODE_STUB_BASE64
    if "rot" in os.lower():
        return RUBY_DECODE_STUB_ROT42

    return ""


def get_enc_stub(lan: str, enc_type: str) -> str:
    if lan.lower() == "ruby":
        return _get_ruby_enc_stub(enc_type)
    if lan.lower() == "python":
        return _get_python_enc_stub(enc_type)
    return ""