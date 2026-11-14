"""Pista de misterio sintetizada (0 créditos): drone grave, estática de radio, sonar, golpes y reloj.
Uso: python3 tools/musica_misterio.py <salida.wav> [segundos] [corte1 corte2 ...]"""
import sys, numpy as np, scipy.io.wavfile as wf, scipy.signal as ss

SR = 44100


def env_exp(n, tau):
    return np.exp(-np.arange(n) / (tau * SR))


def reverb(x, secs=2.2, mix=0.35, seed=1):
    rng = np.random.default_rng(seed)
    n = int(secs * SR)
    ir = rng.standard_normal(n) * env_exp(n, secs / 5)
    ir /= np.abs(ir).sum() ** 0.5 * 6
    y = ss.fftconvolve(x, ir)[: len(x)]
    return (1 - mix) * x + mix * y / (np.abs(y).max() + 1e-9) * np.abs(x).max()


def pista(dur, cortes):
    n = int(dur * SR); t = np.arange(n) / SR
    rng = np.random.default_rng(7)
    out = np.zeros(n)
    # drone en re menor, ligeramente desafinado, que crece
    swell = np.clip(t / 2.5, 0, 1) * (0.75 + 0.25 * np.clip((t - cortes[-1]) / 2, 0, 1))
    for f, a in [(36.7, .5), (36.9, .5), (55.0, .35), (73.4, .2), (87.3, .12)]:
        out += a * np.sin(2 * np.pi * f * t + rng.uniform(0, 6)) * swell
    # pad agudo disonante con trémolo (inquietud)
    pad = sum(np.sin(2 * np.pi * f * t) for f in (587.3, 622.3, 880.0)) / 3
    out += 0.05 * pad * (0.5 + 0.5 * np.sin(2 * np.pi * 5.5 * t)) * np.clip(t / 4, 0, 1)
    # estática de radio al principio (aviso por radio de las 06:52)
    sta = ss.lfilter(*ss.butter(2, [800, 3500], "bandpass", fs=SR), rng.standard_normal(n))
    out += 0.22 * sta * np.clip(1 - t / 3.0, 0, 1) * (0.6 + 0.4 * (rng.random(n) > 0.002))
    # sonar: ping cada 2,4 s con eco
    for p0 in np.arange(0.4, dur - 1, 2.4):
        i = int(p0 * SR); m = min(int(2.0 * SR), n - i)
        ping = np.sin(2 * np.pi * 1180 * np.arange(m) / SR) * env_exp(m, 0.35) * 0.18
        out[i:i + m] += ping
        j = i + int(0.45 * SR); mm = min(m, n - j)
        if mm > 0: out[j:j + mm] += 0.4 * ping[:mm]
    # golpe grave (caída) en cada corte de plano + latido
    for c in cortes:
        i = int(c * SR); m = min(int(1.6 * SR), n - i)
        tt = np.arange(m) / SR
        boom = np.sin(2 * np.pi * (70 * np.exp(-tt * 3) + 28) * tt) * env_exp(m, 0.45)
        out[i:i + m] += 0.9 * boom
        hit = ss.lfilter(*ss.butter(2, 2500, "low", fs=SR), rng.standard_normal(m)) * env_exp(m, 0.08)
        out[i:i + m] += 0.35 * hit
    for b in np.arange(1.0, cortes[-1], 1.05):  # latido lento hasta la revelación
        for k, a in ((0, 1.0), (0.22, 0.6)):
            i = int((b + k) * SR); m = min(int(0.3 * SR), n - i)
            if m <= 0: continue
            tt = np.arange(m) / SR
            out[i:i + m] += 0.35 * a * np.sin(2 * np.pi * 52 * tt) * env_exp(m, 0.07) * np.clip(b / cortes[-1], 0.3, 1)
    # reloj en la última parte («MAÑANA · 18:00»)
    for k, b in enumerate(np.arange(cortes[-1] + 0.6, dur - 0.6, 0.5)):
        i = int(b * SR); m = min(int(0.05 * SR), n - i)
        tick = ss.lfilter(*ss.butter(2, [2500, 6000], "bandpass", fs=SR), rng.standard_normal(m)) * env_exp(m, 0.008)
        out[i:i + m] += (0.5 if k % 2 == 0 else 0.35) * tick
    out = reverb(out)
    out *= np.clip(t / 0.15, 0, 1) * np.clip((dur - t) / 1.2, 0, 1)
    out /= np.abs(out).max() / 0.9
    # estéreo con leve desfase
    d = int(0.012 * SR)
    st = np.stack([out, np.concatenate([np.zeros(d), out[:-d]])], 1)
    return (st * 32767).astype(np.int16)


if __name__ == "__main__":
    dst = sys.argv[1]; dur = float(sys.argv[2]) if len(sys.argv) > 2 else 12.5
    cortes = [float(x) for x in sys.argv[3:]] or [3.15, 6.3]
    wf.write(dst, SR, pista(dur, cortes))
    print(dst)
