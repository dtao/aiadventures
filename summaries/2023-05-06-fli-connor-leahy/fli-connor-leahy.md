---
date: 2023-05-06
type: interview
summary: FLI interview with Connor Leahy
url: https://www.youtube.com/watch?v=ps_CCGvgLS8
---

In a recent episode from the [Future of Life Institute][1] podcast, the host
interviewed Connor Leahy, the CEO of a company called [Conjecture][2]. I was not
familiar with Leahy before listening to this episode.

They began by discussing how with the advent of ChatGPT AI is becoming
mainstream. Leahy noted that he grew up in a rural town, and that even his
family members who seldom use computers have been asking about AI. Leahy said he
feels that the leap from GPT-3 to GPT-4 was just as big as the leap from 2 to 3,
and that he does not believe progress is slowing down or that we're likely to
hit diminishing returns any time soon.

Leahy is very concerned about AI safety and the alignment problem. I found his
general attitude about AGI to be similar to that of Eliezer Yudkowsky, i.e. he
seems quite confident that if society continues down its current trajectory---
that is, with AI labs building increasingly powerful [large language models][3]
until human-level intelligence is achieved---it will lead to humanity's
downfall. Leahy treated this as fairly obvious and claimed that when you
describe AGI to everyday people, most people say, _"That is obviously a bad
idea; don't build that."_

Yudkowsky has his "inscrutable matrices" as his phrase of choice (he also
likes "alien actress"); Leahy has [Shoggoth memes][4]: images depicting
Lovecraftian creatures with monstrous tentacled bodies, with innocent-looking
smiley faces attached to them. Both men fear that AI systems that are designed
like today's so-called LLMs (by the way, Leahy does not like the name "large
language model" because he feels it gives people a false sense of security
based on the idea that they only operate on language) are far too opaque to be
considered safe. As they become more powerful, they will become increasingly
good at convincing us they are human-like (the smiley face) when on the inside
they are something very different and foreign to us (the tentacled monster).

![Shoggoth with smiley face](/images/fli-connor-leahy-shoggoth.png)

As a small example of this, Leahy referred to the known cases of image
recognition systems being [tricked by a single pixel change][5] into labeling
a horse as a dog, a dog as a cat, or a car as an airplane. These are not
mistakes that most humans would make, and they show according to Leahy that the
way these systems model the world is alien to us.

![Results of "one pixel attacks" on image recognition systems](/images/fli-connor-leahy-one-pixel-attack.png)

Leahy said this is to be expected when you consider how these models learn
compared to how humans learn. If you took a human brain, Leahy said, removed it
from all sensory input, connected it to some apparatus that only processed a
two-way stream of binary data connected to an array of switches with on/off
states for a million years, and then put it back in a human body, that thing
would not be a human.

---

Now that we're 6 paragraphs in, I should probably summarize the actual central
topic of the interview, which is Leahy's proposal for a type of system called a
"CoEm", or _cognitive emulator_.

As far as I can tell, the idea behind CoEms is quite similar to [what Paul
Christiano described in his Bankless interview][6] as **scalable oversight**,
which is all about ensuring that the behavior of AI systems can be understood
by humans even as those systems become more intelligent than we are.

The best way I can think of to describe the idea behind a CoEm is to start by
contrasting it with what it is _not_ like. A CoEm would _not_ be like a large
language model, which is a big black box: it has impressive capabilities, but
we don't understand how it does what it does, because it doesn't "think" the way
a human thinks. In contrast, a CoEm would be built from components that adhere
to certain rules and constraints that we can understand, and which correspond to
our own cognitive functions. I think the idea is that a CoEm would follow a
thought process that humans could follow and validate, reducing our need to fear
Shoggoth-like monstrosities that merely mimic our output but think in alien ways
we can't comprehend.

I'm not totally confident that I fully grasped the nuances of the idea of CoEms.
The host actually tried to describe it once or twice and Leahy didn't seem to
think that he got it. I think a metaphor that they eventually agreed on was one
of a human corporation, where you can speak to any individual human employee
and they can explain what they're doing and how it relates to the corporation's
broader goals. However, if this is a good metaphor, then I find myself skeptical
since I tend to think a corporation exhibits emergent behavior that may not be
apparent from the individual actions of its employees; i.e. it can still end up
being a black box, even if it's seemingly composed of clear boxes.

As Leahy put it: "Once you have a black box, you're screwed." I have my doubts
that there's really any escaping _some_ black boxes. After all, one could argue
that human beings are themselves black boxes to one another (as philosophers
have known for ages).

But we haven't all killed each other... yet. That fact makes me hopeful that any
progress we make towards making AI that is more "human-like" is likely in the
right direction.

[1]: https://futureoflife.org/
[2]: https://conjecture.dev/
[3]: /summaries/eight-things-to-know-about-llms.html
[4]: https://knowyourmeme.com/memes/shoggoth-with-smiley-face-artificial-intelligence
[5]: https://arxiv.org/abs/1710.08864
[6]: /summaries/bankless-paul-christiano.html
