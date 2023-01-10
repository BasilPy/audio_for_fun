import pyaudio
import wave

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)

frames = []
try:
	while True:
		data = stream.read(1024)
		frames.append(data)
except KeyboardInterrupt:
	pass

stream.stop_stream()
stream.close()
audio.terminate()

sound_file = wave.open("first_rec.wav", "wb")
sound_file.setnchannels(2)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframesraw(b''.join(frames))
sound_file.close()