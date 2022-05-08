
def rgb_to_hex(rgb):
    """
    RGB转十六进制
    """
    r, g, b = rgb

    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        print('注意：RGB格式颜色错误，请输入三个0~255之间数值组成的元组\n')   #提示语
        return None
    else:         
        hex_r = hex(r)[2:].upper().zfill(2)
        hex_g = hex(g)[2:].upper().zfill(2)
        hex_b = hex(b)[2:].upper().zfill(2)
        return '#' + hex_r + hex_g + hex_b

def hex_to_rgb(hex):
    """
    十六进制转RGB
    """
    if hex[0] != '#' or len(hex) != 7:   
        print('注意：十六进制格式颜色错误，请输入7位以\'#\'开头的字符串\n')
        return None
    else:
        r = int('0x' + hex[1:3], 16)
        g = int('0x' + hex[3:5], 16)
        b = int('0x' + hex[5:7], 16)
        return (r, g, b)



a = rgb_to_hex((-2, 57, 225))
print(a)
b = hex_to_rgb('#1839E1')
print(b)