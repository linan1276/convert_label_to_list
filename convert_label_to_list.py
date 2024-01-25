import os
import langid

def convert_lab_folder_to_txt(input_folder, output_txt_path):
    with open(output_txt_path, 'a', encoding='utf-8') as txt_file:
        for filename in os.listdir(input_folder):
            if filename.endswith('.lab'):
                lab_file_path = os.path.join(input_folder, filename)

                # 获取 .wav 文件的路径， .lab 文件与相应的 .wav 文件同名
                wav_file_path = os.path.splitext(lab_file_path)[0] + '.wav'

                # 获取 .wav 所在文件夹的名字
                folder_name = os.path.basename(os.path.dirname(wav_file_path))

                # 从 .lab 文件内容中提取文本内容
                with open(lab_file_path, 'r', encoding='utf-8') as lab_file:
                    lab_content = lab_file.read()

                # 利用 langid 库识别语言
                lang, _ = langid.classify(lab_content)

                # 根据识别结果添加对应的语言标记
                if lang == 'zh':
                    language = 'ZH'
                elif lang == 'en':
                    language = 'EN'
                elif lang == 'ja':
                    language = 'JP'
                else:
                    # 默认为中文
                    language = 'ZH'

                # 获取 .txt 文件名，为 output
                txt_file_name = folder_name

                # 将数据写入 .txt 文件
                txt_file.write(f'{wav_file_path}|{txt_file_name}|{language}|{lab_content}\n')

def convert_txt_to_list(input_txt_path, output_list_path):
    with open(input_txt_path, 'r', encoding='utf-8') as txt_file, \
         open(output_list_path, 'w', encoding='utf-8') as list_file:
        for line in txt_file:
            # 去除每行末尾的换行符
            line = line.rstrip('\n')
            # 替换.txt为.list
            line = line.replace('.txt', '.list')
            list_file.write(line + '\n')

# 路径
input_folder = ''
output_txt_path = ''
output_list_path = ''

convert_lab_folder_to_txt(input_folder, output_txt_path)
convert_txt_to_list(output_txt_path, output_list_path)


