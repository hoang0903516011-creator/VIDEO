"""Generate Vietnamese narration with local Piper/VITS via sherpa-onnx.
Usage: python scripts/generate_voice.py /path/to/vits-piper-vi_VN-vais1000-medium
Requires sherpa-onnx==1.13.8 soundfile numpy and ffmpeg.
"""
import sys,json,subprocess
from pathlib import Path
import numpy as np
import sherpa_onnx as so
import soundfile as sf
ROOT=Path(__file__).resolve().parents[1]
MODEL=Path(sys.argv[1])
lines=[
 (0.30,2.30,'Khoan! Quên người bạn đồng hành rồi!'),
 (2.70,1.10,'Ủa, ai nữa?'),
 (4.25,2.85,'À, Tốp Gia! Khăn giấy ướt đây rồi.'),
 (7.25,3.35,'Mở một lô mà tưởng đang khui quà!'),
 (11.20,1.20,'Đi làm mang gì?'),
 (12.55,1.10,'Có khăn!'),
 (14.15,.80,'Đi chơi?'),
 (15.10,1.40,'Vẫn có khăn!'),
 (17.20,2.15,'Sáu gói, một trăm năm mươi nghìn!'),
 (19.55,2.05,'Hai mươi đến ba mươi mốt tháng mười,'),
 (21.80,1.90,'tại giỏ hàng Đồ Gia dụng tốt nhé!'),
 (24.25,2.65,'Bấm giỏ hàng, chọn Tốp Gia nha!'),
 (27.10,2.55,'Có khăn rồi, giờ thì đi thật!'),
]
v=so.OfflineTtsVitsModelConfig(model=str(MODEL/'vi_VN-vais1000-medium.onnx'),tokens=str(MODEL/'tokens.txt'),data_dir=str(MODEL/'espeak-ng-data'),noise_scale=.5,noise_scale_w=.5)
c=so.OfflineTtsConfig(model=so.OfflineTtsModelConfig(vits=v,num_threads=2),max_num_sentences=2,silence_scale=.15)
assert c.validate()
tts=so.OfflineTts(c)
rate=tts.sample_rate
mix=np.zeros(rate*30,dtype=np.float32)
tmp=ROOT/'.hyperframes'/'voice-work';tmp.mkdir(parents=True,exist_ok=True)
meta=[]
for i,(start,slot,text) in enumerate(lines):
 a=tts.generate(text,speed=0.90)
 x=np.asarray(a.samples,dtype=np.float32)
 nz=np.flatnonzero(np.abs(x)>.007)
 if len(nz):x=x[max(0,nz[0]-int(.035*rate)):min(len(x),nz[-1]+int(.08*rate))]
 sf.write(tmp/f'{i}-raw.wav',x,rate)
 duration=len(x)/rate
 factor=max(1.,duration/slot)
 if factor>1.001:
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(tmp/f'{i}-raw.wav'),'-af',f'atempo={factor:.5f}',str(tmp/f'{i}.wav')],check=True)
  x,r=sf.read(tmp/f'{i}.wav',dtype='float32')
 x=x[:int(slot*rate)]
 pos=int(start*rate);mix[pos:pos+len(x)]+=x
 meta.append({'start':start,'end':round(start+len(x)/rate,3),'text':text,'tempo_factor':round(factor,3)})
 print(i,round(duration,2),'->',round(len(x)/rate,2),text,flush=True)
mix*=.88/max(.01,float(np.max(np.abs(mix))))
sf.write(ROOT/'assets'/'narration.wav',mix,rate)
(ROOT/'voice-timing.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
