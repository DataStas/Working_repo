import os
from typing import Dict
import whisper
import numpy as np
CHUNK_LIM = 480000
MY_PATH = 'D:\\работа\\курсы\\google_it\\2'


def make_chunks(audio):
    audios = []
    if len(audio) <= CHUNK_LIM:
        audios.append(audio)
    else:
        for i in range(0, len(audio), CHUNK_LIM):
            chunk = audio[i:i + CHUNK_LIM]
            chunk_index = len(chunk)
            if chunk_index < CHUNK_LIM:
                padding = [0] * (CHUNK_LIM - chunk_index)
                array1 = np.array(chunk)
                array2 = np.array(padding)
                concat =  np.concatenate((array1, array2))
                chunk = concat.astype(np.float32)
            audios.append(chunk)
    return audios


def make_trans(model, audios):
    results = ""
    for chunk in audios:
        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(chunk).to(model.device)

        # decode the audio
        options = whisper.DecodingOptions(fp16=False)
        result = whisper.decode(model, mel, options)
        results += result.text
    return results


def extract_text(filename):
    model = whisper.load_model("base")
    audio = whisper.load_audio(filename)
    audios = make_chunks(audio)
    text = make_trans(model, audios)
    return text


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


def read_all_mp4(my_path: str) -> Dict[str, str]:
    os.chdir(my_path)
    # model = whisper.load_model('base.en')
    all_dir = list(filter(lambda x: x[-3:] != 'zip', os.listdir(os.getcwd())))
    info = {}
    for dir in all_dir:
        os.chdir(my_path+'\\'+dir)
        tmp = my_path+'\\'+dir
        for sub_dir in [f for f in os.listdir() if os.path.isdir(f)]:
            os.chdir(tmp+'\\'+sub_dir)
            all_files = [f for f in os.listdir() if os.path.isfile(f)]
            mp4_files = list(filter(lambda x: x[-3:] == 'mp4', all_files))
            for mp4_file in mp4_files:
                try:
                    info[mp4_file] = extract_text(mp4_file)
                except:
                    break
                if mp4_file == '3. Congratulations!.mp4':
                    break
    return rewrite(info)


def save_all_files(info: Dict[str, str]):
    for file, text in info.items():
        with open(file[:-3]+'txt', 'w') as f:
            f.write(text)


if __name__ == '__main__':
    info = read_all_mp4(MY_PATH)
    os.chdir('D:\Pyhton_Dir\Projects\Working_repo\projects\\vtt_to_txt\\txt\\2')
    print(info)
    save_all_files(info)