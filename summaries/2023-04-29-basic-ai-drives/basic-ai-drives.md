---
date: 2023-04-29
type: paper
summary: The Basic AI Drives
author: Steve Omohundro
url: https://selfawaresystems.files.wordpress.com/2008/01/ai_drives_final.pdf
---

_Note: this paper was written in 2008._

As far as I know, this paper by Steve Omohundro introduced the idea that was
later repackaged by Nick Bostrom as _instrumental convergence_. The idea is that
regardless of an AI system's "goals", which may well be harmless, as the system
becomes more capable it will develop intermediate goals or "drives" in service
of these goals; and these drives themselves may not be so harmless.

The following is my attempt to cover them all concisely. For illustration, let's
imagine an AI system whose only explicit goal is to win at chess.

1. **Self-improvement.** The system will develop an intermediate goal of finding
   ways of improving its chess skills. Doing so will help it to ultimately
   achieve its explicit goal of winning games.
2. **Rationality.** The system will strive to act in a rational way, i.e. to
   always pursue actions that maximize its chances of victory at chess. It will
   resist acting irrationally, i.e. doing things that would reduce its chances
   of victory at chess.
3. **Goal preservation.** The system will avoid modifying itself in ways that
   might reduce its desire to win chess games, or add new goals that could
   distract it from winning chess games.
4. **Avoidance of false pleasures.** The system will recognize and avoid
   "counterfeit utility", i.e. blindly pursuing signals that are typically
   correlated with winning chess games but aren't the real deal.
5. **Self-preservation.** The system will protect itself from external forces
   that would threaten to shut it down, since that would prevent it from playing
   and winning more games of chess.
6. **Acquisition of resources.** The system will aim to acquire resources
   ("space, time, matter, and free energy") in order to maximize its capacity to
   play and win more games of chess.

---

I must admit that I was a bit surprised reading this. I'm not sure why, but I
was expecting something much more scientifically rigorous. What do I mean by
that? I think I was expecting either some over-my-head mathematical proofs, or
else empirical evidence supporting these claims. As far as I can tell, it
_seems_ like these are basically well-articulated intuitions about how AI
systems might develop. Thought experiments, basically.

The "empirical evidence" I was expecting might have looked like: a survey of the
most advanced versions of artificial intelligence across multiple architectural
paradigms, showing that despite having very different architectures, each
paradigm demonstrated some form of each of the drives Omohundro describes. Or:
a review of real-world AI systems with highly divergent goals, highlighting the
emergence of these drives in each of them.

I recognize that, considering this paper was written 15 years ago (!), such
empirical evidence would likely have been impossible to produce at the time.

---

Assorted thoughts that came to me as I read the paper:

> Systems will therefore exercise great care in modifying themselves. They will
> devote significant analysis to understanding the consequences of modifications
> before they make them.

I was genuinely incredulous reading this part. I don't believe that this is
even _remotely_ true of humans: collectively, our willingness to try potentially
dangerous things without knowing the consequences in advance practically defines
us as a species. (Exhibit A: the field of artificial intelligence!)

Does Omohundro feel differently? Or would agree with this, but he feels that AI
will be fundamentally different from us in this regard? Why would it be?

> So how can it ensure that future self-modifications will accomplish its
> current objectives? For one thing, it has to make those objectives clear to
> itself.

Again, to me human behavior seems like a counterpoint to this. We are
[mesa-optimizers][1], are we not? In the developed world, affluence is
negatively correlated with birth rates.

> In many situations, irrational collective behavior arising from conflicting
> component goals ultimately hurts those components.

This acknowledges the possibility of irrational behavior emerging from rational
componentized systems. Omohundro provides a compelling example of a couple
arguing: they can't agree on what to do one evening, so they spend the entire
evening arguing, which is not something _either_ of them wanted. It feels highly
speculative to me that this phenomenon will inevitably be "overcome" by
instrumental convergence operating at every level.

Would AI be immune to [Moloch][2]?

Regarding counterfeit utility:

> AI systems will recognize this vulnerability in themselves and will go to
> great lengths to prevent themselves from being seduced by its siren call.

Again, as I read these words I wondered: _Why? How do we know this?_

Regarding self-preservation: the idea a chess-playing robot would defend itself
feels pretty contrived to me. We're talking about a superintelligent robot that
is advanced enough to exhibit all of these basic drives, but it's still _just_
playing chess?

It might be unfair for me to be judging this idea through the lens of [what we
know about large language models][3] in 2023. The notion of a chess-playing AI
with human-level intelligence that doesn't have countless other unpredictable
emergent behaviors seems downright quaint to me now. I have serious doubts about
whether such a thing is even possible. That said, maybe 15 years from now it
will seem prehistoric that the most advanced AI systems we had in 2023 were so
opaque.

Also: humans clearly value self-preservation. But under threat, a human's
behavior can be unpredictable. They may do nothing (paralyzed with fear).
Picture a hostage following instructions silently while a gun is held to their
head. They may know they are likely doomed but fail to see a viable alternative.
The rational response might be a "wait and see" approach, cooperating to
optimize for short-term survival while holding out hope that new opportunities
will present themselves, e.g. someone might show up to rescue them, or their
aggressor might trip and drop their weapon.

Regarding efficient use of resources:

> We can expect their physical forms to adopt the sleek, well-adapted shapes so
> often created in nature.

Ha! This is directly related to [Max Tegmark's point about the development of
flying machines][4] versus the evolution of birds. (In my mind, Tegmark's
observation effectively refutes this prediction.) Also related: Tegmark's story
about the researchers who [figured out how to "move" the Eiffel Tower from Paris
to Rome][5] in an AI system's internal representation of the world. Apparently
the way this system was storing this information was "incredibly dumb" i.e.
very inefficient.

I think efficiency as an emergent value is dubious. Maybe if you properly
account for _all_ resources in your "efficiency" calculation, in which case time
is probably nearly always the most constrained resource. (But serious question:
will AIs "care" about time? Will they get impatient? It's hard to say how much
our perception of time as a constrained resource is a byproduct of our lifespans
relative to our cognitive abilities.)

[1]: /thoughts/explaining-ai-terms-the-feynman-way-pt1.html
[2]: https://slatestarcodex.com/2014/07/30/meditations-on-moloch/
[3]: /summaries/eight-things-to-know-about-llms.html
[4]: /summaries/lex-fridman-max-tegmark.html
[5]: https://arxiv.org/pdf/2202.05262.pdf
