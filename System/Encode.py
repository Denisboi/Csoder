try:
    from struct import Struct
    from System.Reader import Reader
    from PIL import Image, ImageDraw
    from System.Logger import Console
except:
    raise RuntimeError('Please use command "pip install -r requirements.txt"!')
def ceil(integer) -> int:
    return round(integer + 0.5)  
def encode_sc(data, fileName):
    pass
