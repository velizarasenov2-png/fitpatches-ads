import json, subprocess, sys, numpy as np
from faster_whisper import WhisperModel
raw = subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-f","f32le","-ac","1","-ar","16000","-"],capture_output=True).stdout
m = WhisperModel("medium", device="cpu", compute_type="int8")
segs,_ = m.transcribe(np.frombuffer(raw, np.float32), language="bg", word_timestamps=True, beam_size=5)
words=[{"w":w.word.strip(),"s":round(w.start,2),"e":round(w.end,2)} for s in segs for w in s.words]
json.dump(words, open(sys.argv[2],"w"), ensure_ascii=False, indent=0)
print(" ".join(f"{x['w']}[{x['s']}]" for x in words))
