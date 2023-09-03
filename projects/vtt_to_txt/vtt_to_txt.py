import os
from typing import Dict
MY_PATH = 'D:\\работа\\курсы\\google_it\\1'


def rewrite(info: Dict[str, str]) -> Dict[str, str]:
    for file, text in info.items():
        tmp = ''
        cur_len = 0
        for word in text.replace('\n', ' ').split():
            if cur_len < 70:
                cur_len += len(word)
                tmp += word + ' '
            else:
                cur_len = 0
                tmp += '\n' + word + ' '
        info[file] = tmp
    return info


def read_all_vtt(my_path: str) -> Dict[str, str]:
    os.chdir(my_path)
    all_dir = list(filter(lambda x: x[-3:] != 'zip', os.listdir(os.getcwd())))
    info = {}
    for dir in all_dir:
        os.chdir(my_path+'\\'+dir)
        tmp = my_path+'\\'+dir
        for sub_dir in [f for f in os.listdir() if os.path.isdir(f)]:
            os.chdir(tmp+'\\'+sub_dir)
            all_files = [f for f in os.listdir() if os.path.isfile(f)]
            vtt_files = list(filter(lambda x: x[-3:] == 'vtt', all_files))
            for vtt_file in vtt_files:
                info_str = ''
                with open(vtt_file) as f:
                    for num, line in enumerate(f.readlines()):
                        if len(line.split()) > 5:
                            info_str += line
                info[vtt_file] = info_str
    return rewrite(info)


def save_all_files(info: Dict[str, str]):
    for file, text in info.items():
        with open(file[:-3]+'txt', 'w') as f:
            f.write(text)



if __name__ == '__main__':
    info = read_all_vtt(MY_PATH)
    os.chdir('D:\Pyhton_Dir\Projects\Working_repo\projects\\vtt_to_txt\\txt')
    print(os.getcwd())
    save_all_files(info)

# filenames = next(), (None, None, []))[2]  
# print(filenames)