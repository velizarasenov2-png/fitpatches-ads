# Видео реклама „Аз съм хладилникът на Ивайла“ (kie.ai + ElevenLabs)

- Глас: ElevenLabs, Peter K (eleven_v3, емоционални тагове), един дубъл от 72.4 сек (`audio/voice.mp3`). Резервният дубъл е `audio/voice_b.mp3`.
- Референции: Nano Banana Pro, 2K (`refs/`): Ивайла преди, Ивайла след (реалистично, около 7 кг по-лека), кухнята и истинската лепенка.
- Сцени: 10 клипа от Gemini Omni 1.1 Flash, 720p, 9:16 (`clips/`), общо 70 сек за 966 кредита. Продължителностите следват репликите от `audio/transcript.json`.
- Монтаж: `scripts/edl.py` + `scripts/assemble.py`. Субтитрите са по текста на сценария. Надписите 23:00/23:45 са върху нощната сцена. Финалът е снимката на лепенките с „3+2 ПОДАРЪК · ПЛАЩАНЕ ПРИ ПОЛУЧАВАНЕ“. Пианото е много тихо (−34 dB).
- Готово: `deliver/FitPatches_hladilnik_subtitri_720p.mp4` и `deliver/FitPatches_hladilnik_bez_subtitri_720p.mp4`.

```bash
export KIE_API_KEY=...   # не се комитва
python3 scripts/gen_all.py s04   # отделна сцена; без аргументи пуска референциите + всички сцени
python3 scripts/assemble.py
```
