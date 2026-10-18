"""Deterministic original upbeat bed + comic pop and bell effects, no external music."""
from pathlib import Path
import numpy as np
import soundfile as sf
import json
R=Path(__file__).resolve().parents[1];sr=44100;t=np.arange(sr*30)/sr
y=np.zeros_like(t);rng=np.random.default_rng(310)
# Light marimba-like melody, syncopated bass, claps and a restrained kick.
notes=[72,76,79,76,69,72,76,72,65,69,72,69,67,71,74,71]
for k in range(120):
 start=k*.25;sel=(t>=start)&(t<start+.24);u=t[sel]-start
 f=440*2**((notes[k%16]-69)/12)
 y[sel]+=.12*np.exp(-u*15)*(np.sin(2*np.pi*f*u)+.25*np.sin(4*np.pi*f*u))
 if k%2==0:
  bass=440*2**(([48,45,41,43][(k//16)%4]-69)/12)
  y[sel]+=.08*np.exp(-u*10)*np.sin(2*np.pi*bass*u)
 if k%4==0:y[sel]+=.09*np.exp(-u*28)*np.sin(2*np.pi*(58*u+1.4*(1-np.exp(-u*22))))
 if k%4==2:y[sel]+=.025*np.exp(-u*45)*rng.uniform(-1,1,len(u))
# Comic pause after KHOAN; duck under speech.
y[(t>.25)&(t<3.65)]*=.08
for line in json.loads((R/'voice-timing.json').read_text()):
 sel=(t>=line['start']-.07)&(t<=line['end']+.12);y[sel]*=.42
# Pops at reveals.
for start in [.18,4.12,7.12,9.47,11.12,12.6,14.12,15.15,24.15]:
 sel=(t>=start)&(t<start+.15);u=t[sel]-start
 y[sel]+=.25*np.exp(-u*34)*np.sin(2*np.pi*(700*u-1600*u*u))
# Price 'ting' and final sparkle.
for start in [17.5,24.7]:
 sel=(t>=start)&(t<start+.7);u=t[sel]-start
 y[sel]+=.12*np.exp(-u*6)*(np.sin(2*np.pi*1318.51*u)+.4*np.sin(2*np.pi*2637.02*u))
y*=np.minimum(1,np.minimum(t/.12,(30-t)/.4))
sf.write(R/'assets'/'music-sfx.wav',np.clip(y,-.9,.9),sr)
