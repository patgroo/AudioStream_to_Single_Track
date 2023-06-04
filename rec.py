import pyaudio
import wave


def record_audio(output_file, duration=10, sample_rate=44100, chunk_size=1024):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("Recording started...")

    frames = []
    for _ in range(int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate() 

    wave_file = wave.open(output_file, 'wb')
    wave_file.setnchannels(1)
    wave_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

    print(f"Audio saved to: {output_file}")


# Usage
output_file = "audiofiles/output.wav"
record_audio(output_file, duration=30)
