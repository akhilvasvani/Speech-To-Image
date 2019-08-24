import os
import argparse

from pydub import AudioSegment

# Code based off of
# https://gist.github.com/arjunsharma97/0ecac61da2937ec52baf61af1aa1b759

# Saving wavefile with different frequency
# https://github.com/jiaaro/pydub/issues/232


def parse_args():
    parser = argparse.ArgumentParser(description='Convert a 44100 Hz .m4a file to a .wav file')
    parser.add_argument('--audio_path', help='path to audio file', type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    formats_to_convert = ['.m4a']

    for(dirpath, dirnames, filenames) in os.walk(args.audio_path):
        for filename in filenames:
            if filename.endswith(tuple(formats_to_convert)):
                filepath = dirpath + '/' + filename
                (path, file_extension) = os.path.splitext(filepath)
                file_extension_final = file_extension.replace('.', '')
                try:
                    track = AudioSegment.from_file(filepath, file_extension_final, frame_rate=44100)
                    wav_filename = filename.replace(file_extension_final, 'wav')
                    wav_path = dirpath + '/' + wav_filename
                    print('CONVERTING: ' + str(filepath))
                    track = track.set_frame_rate(16000)
                    file_handle = track.export(wav_path, format='wav')
                    os.remove(filepath)
                except:
                    print("ERROR CONVERTING " + str(filepath))


if __name__ == '__main__':
    main()
