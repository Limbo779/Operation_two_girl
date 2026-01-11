import torch
import torch.nn.functional as F
import librosa
import msclap.CLAPWrapper

# --- FIX: Bypass torchaudio entirely ---
def safe_read_audio(self, audio_path, resample=True):
    # Use librosa to load. It returns numpy array.
    # We must specify the target sample rate directly to avoid resampling twice.
    target_sr = self.args.sampling_rate if resample else None
    
    # Load with librosa (returns numpy array)
    audio_np, sample_rate = librosa.load(audio_path, sr=target_sr)
    
    # Convert numpy -> torch tensor
    audio_time_series = torch.from_numpy(audio_np)
    
    # CLAP expects shape (channels, time) but librosa gives (time,) for mono
    # We need to ensure it's (1, time) if it's mono
    if audio_time_series.ndim == 1:
        audio_time_series = audio_time_series.unsqueeze(0)
        
    return audio_time_series, sample_rate

# Apply patch
msclap.CLAPWrapper.CLAPWrapper.read_audio = safe_read_audio
# --- END FIX ---

from msclap import CLAP
clap_model = CLAP(version='2023', use_cuda=False)

def get_song_vector(file_path):
    audio_embeddings = clap_model.get_audio_embeddings([file_path])
    return audio_embeddings[0]


def compare_vectors(vec_a, vec_b):
    # Normalize vectors first for accurate Cosine Similarity
    vec_a = F.normalize(vec_a.unsqueeze(0), dim=1)
    vec_b = F.normalize(vec_b.unsqueeze(0), dim=1)
    
    # Compute similarity (0 to 1)
    return F.cosine_similarity(vec_a, vec_b).item()

target = "/home/limbo/Desktop/Random Learning/Operation_two_girl/Phase_1.5/Phase_1.5_Target.mp3"
candidate = "/home/limbo/Desktop/Random Learning/Operation_two_girl/Phase_1.5/Clipping/"
candidate += input()
candidate += ".mp3"

v1 = get_song_vector(target)
v2 = get_song_vector(candidate)

# Compare
score = compare_vectors(v1, v2)
print(f"Similarity: {score}")