import wave
import numpy as np

def find_silent_interval(file_path, start_time, end_time, silence_duration=2):
    # Open the .wav file
    with wave.open(file_path, 'rb') as wav_file:
        # Get the sample rate
        sample_rate = wav_file.getframerate()
        
        # Calculate the start and end samples based on the given timestamps
        start_sample = int(start_time * sample_rate)
        end_sample = int(end_time * sample_rate)
        
        # Set the number of silent samples required
        silence_samples = int(silence_duration * sample_rate)
        
        # Read the audio frames between the start and end samples
        wav_file.setpos(start_sample)
        frames = wav_file.readframes(end_sample - start_sample)
        
        # Convert the frames to a numpy array
        audio_data = np.frombuffer(frames, dtype=np.int16)
        
        # Find the indices where the audio data has a value greater than a threshold (considered non-silent)
        non_silent_indices = np.where(audio_data > 1000)[0]
        
        # Iterate through the non-silent indices to find the silent interval
        start_index = 0
        silent_interval_found = False
        for index in non_silent_indices:
            # Check if there are enough subsequent silent samples
            if index - start_index >= silence_samples:
                # Silent interval found
                silent_start_time = start_index / sample_rate
                silent_end_time = index / sample_rate
                silent_interval_found = True
                break
            else:
                # Update the start index
                start_index = index
        
        # If a silent interval is found, return the start and end times
        if silent_interval_found:
            return silent_start_time, silent_end_time
        
        # If no silent interval is found, return None
        return None, None

# Example usage
file_path = 'audiofiles/output.wav'
start_time = 0.0  # Start timestamp in seconds
end_time = 30.0  # End timestamp in seconds

silent_start, silent_end = find_silent_interval(file_path, start_time, end_time)

if silent_start is not None:
    print(f"Silent interval found between {silent_start:.2f}s and {silent_end:.2f}s")
else:
    print("No silent interval found.")
