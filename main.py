import librosa
import soundfile
import io

def reverseAudioFile(input_file, output_file):
    audio_data, sample_rate = librosa.load(input_file, sr=None, mono=None)
    reversed_audio = audio_data[::-1]
    soundfile.write(output_file, reversed_audio, sample_rate, subtype="OPUS", format="OGG")

def reverseAudioBuffer(input_data):
    output_file = io.BytesIO()
    output_file.name = "reversed.ogg"

    reverseAudioFile(io.BytesIO(input_data), output_file)

    output_file.seek(0)

    return output_file

def main():
    print('running examples...')
    reverseAudioFile("./example/original.ogg", "./example/reversed.ogg")
    print('done!')

if __name__ == '__main__':
    main()