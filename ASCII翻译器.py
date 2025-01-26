from pickle import TRUE
def string_to_ascii_binary(input_string):
            binary_list = []
            for char in input_string:
                
                binary_representation = format(ord(char), '08b')
                binary_list.append(binary_representation)
            return ' '.join(binary_list)
def ascii_binary_to_string(binary_string):
            binary_values = binary_string.split()
            characters = []
            for binary in binary_values:
                character = chr(int(binary, 2))
                characters.append(character)
            return ''.join(characters)
def input_2():
        try:
            test_binary_string = input("请输入要转换的二进制 ASCII 字符串（以空格分隔）：") 
            if test_binary_string.isascii():
                result_string = ascii_binary_to_string(test_binary_string)
                print("对应的字符串为：")
                print(result_string)
            else :
                print("这不是ASCII字符")
                input_2()
        except ValueError:  
            print("请输入二进制字符!!!")
            input_2()
def input_1():
            test_string = input("请输入要转换的字符串：")
            binary_result = string_to_ascii_binary(test_string)
            print("字符串的 ASCII 二进制表示为：")
            print(binary_result)
def jei():
    while True:  
        try:
            sr = int(input('编码输入1，解码输入2：'))
            if sr in [1, 2]:
                break  
            else:
                print("请输入1或2。")  
        except ValueError:  
            print("1/2!!!")
    if sr == 1:
        input_1()
    elif sr == 2: 
        input_2()
while True:
    jei()
