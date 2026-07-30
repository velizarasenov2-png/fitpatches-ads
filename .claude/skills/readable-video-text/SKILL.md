---
name: readable-video-text
description: Techniques for getting fully readable, correctly-spelled on-screen text, captions, subtitles, signage, or logos in AI-generated video (Veo, Kling, Sora, Runway, and similar text/image-to-video models). Use this whenever the user wants text in an AI video to be legible, non-garbled, correctly spelled, or "every letter in the right place" — including complaints like letters being merged, scrambled, jumbled, or unreadable, unwanted burned-in captions appearing on dialogue clips, or requests to add a sign, label, price, logo, or headline into a generated video. This skill covers prompting techniques to prevent garbled text at generation time AND post-production techniques to fix or replace it — it does not cover visual style/art direction of the video itself (see a dedicated style skill for that) or scripting/storytelling.
---

# Readable On-Screen Text in AI Video

AI video models don't typeset text — they paint pixels that statistically resemble text. That's why letters merge, words come out scrambled, or captions look like a different alphabet. It gets worse the longer the string, the more it moves, and the more it sits on a non-flat surface. This skill exists because there is no reliable way to make a diffusion video model spell perfectly every time — so the real fix is a combination of prompting tricks that raise the odds, plus never trusting anything that has to be 100% correct (brand name, price, CTA) to the generation step alone.

**The one rule that matters most: if a piece of text must be perfect — logo, price, brand name, exact headline — don't generate it as pixels. Suppress on-screen text at generation time, then add that text yourself in post-production as a real typography layer.** Everything below supports that rule, either by making AI-rendered text as clean as possible when you do want it baked in, or by getting rid of AI text cleanly when you don't.

## Two different problems — diagnose which one you have

1. **You want specific text baked into the scene** (a sign, a t-shirt, a product label, a headline) and it's coming out garbled.
2. **You don't want any text at all**, but the model is burning in captions/subtitles anyway (this happens a lot on dialogue/voiceover clips in Veo and similar models).

The fixes are different — use the matching section below.

## Problem 1: You want text in the scene, and it's garbled

### Prompt techniques (apply all of them together — they stack)

- **Wrap the exact string in quotation marks.** This is the strongest signal to the model that this is a literal string to render, not a vibe: `a wooden sign that says "OPEN"`. (Note: this is the opposite of what you want for spoken dialogue — see Problem 2.)
- **Keep it very short.** A single word or 2-3 word phrase renders far more reliably than a sentence. If you need a longer message, either split it across multiple generated shots or plan to add it in post.
- **Describe the typography, not just the words.** Specify font style, weight, and color: "clean bold sans-serif," "thin serif engraved lettering." The more precisely you constrain what the letters should look like, the less the model has to improvise.
- **Put it on a flat, head-on surface.** Text on a flat sign, wall, or screen renders far better than text on a curved surface, fabric, or anything with folds (t-shirts, crumpled paper, wrapped labels are the worst case).
- **Frame it close and static.** A tight shot on the text with a locked-off or slow-static camera gives the model fewer competing details and less chance for letters to warp between frames. Avoid whip pans or fast motion across the text.
- **Iterate rather than expect one-shot success.** Treat the first generation as a draft — tweak wording, framing, or font description and regenerate rather than assuming a bad result means the concept won't work.

### If it still comes out wrong

Don't keep re-rolling the same prompt hoping for luck — change something first (shorter text, flatter surface, different font description) since an unchanged prompt just gambles on the same odds. If it's still not clean after a couple of honest attempts, treat it as a Problem-2-style situation: generate the shot with no text at all, then add your real text in post (see below).

## Problem 2: Unwanted captions/subtitles are burning into dialogue clips

This is a known, well-documented behavior in Veo 3/3.1 and similar models: because training footage often had subtitles baked in, the model learned to associate on-screen speech with on-screen text, and it adds captions even when you explicitly ask for none. These captions are burned into the pixels — there's no toggle to remove them after the fact.

### Prevent it at generation time (stack all four)

1. **Use a colon, never quotation marks, for spoken dialogue.** Quotes signal "render this as text." A colon signals "this is spoken audio."
   - Triggers captions: `A barista says: "Your latte is ready."`
   - Cleaner: `A barista says: Your latte is ready.`
   - Avoid apostrophes in the line too (they behave like quotes) — write "do not" instead of "don't" if a clip keeps fighting you.
2. **Put the dialogue at the start of the prompt**, before the visual description. Speech-first prompts get captioned far less often, and tend to get better lip-sync as a bonus.
3. **Add an explicit no-text instruction immediately after the dialogue line**, not buried at the end of a long prompt: `(no subtitles, no captions, no on-screen text)`.
4. **Fill the negative prompt field** if the tool has one: `subtitles, captions, closed captions, on-screen text, text overlay, watermark, words on screen, lower-third text, burned-in text`.

Combined template:

```
[Speaker] says: [short plain-text line, no quotes, no apostrophes].
(no subtitles, no captions, no on-screen text)

Visual: [subject + action], [setting], [lighting], [camera move].
Negative prompt: subtitles, captions, on-screen text, text overlay, watermark, words on screen
```

Keep each spoken line short (roughly one sentence, 8-12 words) — long dialogue is the single biggest caption trigger and also hurts lip-sync. For two-speaker scenes, label speakers by position/appearance ("the woman on the left in the red jacket") rather than by name, and keep exchanges short — split a conversation into multiple short clips if needed.

**Compose with headroom at the bottom of frame even when following all of the above.** Auto-captions, when they do slip through, land in the lower third — leaving dead space there costs nothing visually and gives you a free escape hatch (see Method 1 below).

## Post-production: your safety net when prevention isn't enough

No prompting technique is 100%. Always have a post-production plan, in order of how much of the frame you're willing to sacrifice:

1. **Crop the bottom strip.** Fast and free. Crop out the bottom 12-18% where burned-in captions almost always land, re-frame to keep the subject centered. Works best on vertical 9:16 content, and works painlessly if you left headroom at generation time.
2. **Cover it with your own text.** Drop a correctly-spelled lower-third, caption bar, or brand graphic over the bottom strip using a real editor (CapCut, Premiere, DaVinci Resolve, VEED, Kapwing). This is usually the best choice for ads: you get full control over font, color, size, and timing, and zero risk of a merged or scrambled letter, because you typed it yourself.
3. **AI text/object removal (inpainting).** For a hero shot where cropping would ruin the composition, use an AI text-removal or inpainting tool to reconstruct the pixels behind the garbled text. Works well on plain backgrounds, less reliably on busy or moving ones — preview a few frames before committing to a full export.
4. **Re-roll — but only with a corrected prompt.** Regenerating with the exact same prompt just burns credits on the same odds. Apply the Problem 2 prevention techniques first, then re-roll.

## The default workflow for anything with critical text (ads, product callouts, prices, CTAs)

1. Generate the video with on-screen text fully suppressed (Problem 2 techniques), leaving bottom headroom.
2. Add every piece of text that has to be correct — brand name, price, CTA, headline — as a real overlay layer in post, using an actual font. This is the only method with zero risk of merged or scrambled letters, because no AI model is drawing the letters.
3. Reserve "let the AI render the text" (Problem 1 techniques) only for atmospheric, non-critical background text where an occasional imperfect result is acceptable (a blurry sign in a crowd scene, for instance) — never for anything the viewer needs to read accurately.
