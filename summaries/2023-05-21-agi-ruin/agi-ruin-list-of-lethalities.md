---
date: 2023-05-21
type: article
summary: AGI Ruin
subtitle: A List of Lethalities
url: https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities
---

"AGI Ruin" is a fairly famous piece of writing in the world of AI alignment by
Eliezer Yudkowsky, who is a bit like the spokesperson for the community of
those concerned about AI existential risk (referred to perjoratively as "AI
doomers" by those on the other side including [Yann LeCun][1]).

While the article was written back in June 2022, an interesting recent
development is that the philosopher David Chalmers [asked][2]:

> is there a canonical source for "the argument for AGI ruin" somewhere,
> preferably laid out as an explicit argument with premises and a conclusion?

This question prompted a dialogue between Yudkowsky and Chalmers, who made it
clear that he does not consider Yudkowsky's article to qualify as a formal
argument.

Related: I recently [wrote about this piece][3]:

> I _have_ been reading a lot of articles on LessWrong, and a lot of
> them _do_ seem quite long and difficult to digest. For example, [this article
> from Eliezer Yudkowsky][4] and [this response from Paul Christiano][5] are
> both written in the form of lists of points... which, ordinarily, I would
> consider to be an effective style for maximizing comprehensibility. But
> Yudkowsky's list has 43 points on it, and Christiano's has 46! Reading them,
> I find my brain struggling to synthesize the points they're making into a
> high-level summary. The prioritization isn't clear, many of them overlap with
> each other, etc.

While I will [not be the first][6] to attempt it, these feel like ideal
circumstances for me to try to summarize the _implicit_ argument underlying
"AGI Ruin" that is woven through its 43 points, many of which are phrased like
responses to countless objections that Yudkowsky has no doubt encountered over
the years.

---

### Premises

1. **P1** The current trajectory of AI research will lead to superhuman AGI.
2. **P2** Superhuman AGI will be capable of escaping any human efforts to
   control it.
3. **P3** Superhuman AGI will be _misaligned_ by default, i.e. it will likely
   adopt values and/or set long-term goals that will lead to extinction-level
   outcomes, meaning outcomes that are _as bad as_ human extinction.
4. **P4** We do not know _how to align_ superhuman AGI, i.e. reliably imbue it
   with values or define long-term goals that will ensure it does _not_
   ultimately lead to an extinction-level outcome, without some amount of trial
   & error (how nearly all of scientific research works).

### Conclusions

1. **C1**: **P2** + **P3** In the case of superhuman AGI, since it will be able
   to escape human control and misaligned by default, the only survivable path
   to alignment cannot involve trial & error because the first failed try will
   result in an extinction-level outcome.
2. **C2**: **P4** + **C1** This means we will not survive superhuman AGI,
   because our survival would require alignment, towards which we have no
   survivable path: the only path we know of involves trial & error, which is
   not survivable.
3. **C3**: **P1** + **C2** Therefore the current trajectory of AI research which
   will produce superhuman AGI leads to an outcome where we do not survive.

---

I might play with that some more, but I think it's pretty close.

For what it's worth, the premises here that I am inclined to agree with _most_
are P2 and P4.

Regarding the 2nd premise: it does not seem difficult to me to accept that
control requires an asymmetry of power, and power increases with intelligence.
Intelligence is certainly not the _only_ factor that increases power
(for example, access to resources is another); but a large enough difference in
intelligence levels between two parties can offset any other factors that might
otherwise favor the less intelligent party, because the more intelligent party
can use deception, persuasion, and other techniques to either neutralize or
reverse those other factors.

Simple example: a human with a banana and a chimpanzee with a gun. The chimp is
in a more powerful position based on its far greater physical strength and its
possession of the gun. But the human can trick the chimp into trading the gun
for the banana, which then gives the human the upper hand. Intelligence alone
is sufficient for the human to flip the asymmetry of power despite being at an
apparent disadvantage in the beginning.

So I agree that if we build superintelligent AGI, we will likely not be able to
actually control it.

Regarding the 4th premise: I don't have confidence that we (humanity) know how
to build thinking systems that vastly exceed our own intelligence in such a way
that we can define or control their goals in any meaningful way. I have a
strong suspicion that these systems would inevitably show signs of emergent
goals that we would not be able to influence or even predict.

At least Yudkowsky believes that alignment is _theoretically_ possible. I'm not
personally even sure of _that_. But if it is, I do agree that we generally
don't know how to solve such problems without relying on trial & error, also
known as the scientific method (i.e. form hypotheses and try to invalidate them
through empirical experiments). Our whole way of discovering and learning is
just too messy: we try things, see what works and what doesn't work, and _over
time_ develop theories to provide an explanatory model that makes sense of it
all.

So I also agree that we don't seem to be in a position to "solve" AI alignment
in a way that we should feel confident we could prevent AGI ruin if current AI
research is leading imminently to superintelligent AGI.

I am a lot less confident about the premises P1 and P3.

Regarding the 1st premise: I think it is quite reasonable to be _concerned_
about the potential for P1, i.e. that superhuman AGI is imminent based on the
current state of research. As Yudkowsky stated in his [recent interview with Lex
Fridman][7], part of the reason he wrote "AGI Ruin" is that he was alarmed at
the progress of large language models and the fact that adding enough compute
power and enough training data was enough for OpenAI to create GPT-4. It does
seem to me that it ought to fill us all with at least a _little_ bit of dread
that [capabilities seem to emerge spontaneously and unpredictably][8] in LLMs.

On the other hand, the very fact that we cannot explain the emergence of these
capabilities _to me_ ought to diminish anyone's confidence that they can predict
how far LLMs can actually go.

Consider human beings. If some alien researchers were observing a human child,
you could imagine that they would be alarmed at the child's rate of cognitive
development over the first several years. They might fear that there would be
no limit to how intelligent the human would become. But eventually they would
be relieved to see that human cognitive ability does more or less plateau at a
certain point.

To be clear I'm not saying this is necessarily how it would always play out. But
I think we have evidence of cases where things _do_ play out this way.

So I have my doubts that we are on the brink of superhuman intelligence based on
the state of the art in AI research today.

See also: [this very astute point][9] from Amjad Masad, the CEO of Replit,
regarding how incentives on both sides of the AI existential risk divide
encourage exaggeration:

> On the one hand AI labs are incentivized to oversell their models'
> capabilities. [...] On the other hand you have people who built their entire
> identity on freaking out about AGI, and the louder they freak out the more
> attention and funding they attract. So they're incentivized to also overstate
> the capabilities.

Then there is P3, that superhuman AGI will be misaligned by default. This is
probably the weakest part of the whole argument to me. It seems almost
necessarily unknowable, for reasons that share a common foundation with the
reasoning behind the 2nd premise (that we won't be able to control
superintelligent AGI). We are talking about an intelligence beyond our own,
which we cannot confidently reason about.

As far as I can tell, this premise is heavily predicated on the idea of
[instrumental convergence][10], which is a hypothesis that any sufficiently
advanced intelligence will inevitably adopt certain intermediate goals or
sub-goals that include self-preservation and self-improvement among other
things. I find this hypothesis to be pretty tenuous to begin with: as I have
[previously written][11]: the canonical arguments for it (from what I have read,
which I admit may be not nearly enough to be able to represent this hypothesis
adequately) really just boil down to the fact that it _seems true to some
people_, e.g. the authors of the influential papers on the subject.

Consider human beings once more. Our intelligence certainly exceeds that of many
if not all other species on our planet. And indeed, our actions have led to the
extinction of many species---though I believe the vast majority of such cases
have been unintentional. There are also many species we have _not_ exterminated
accidentally. And in modern times, we actively protect many species that we have
identified as being in danger of extinction.

If anything, as our capabilities have increased, our values have also evolved to
be more compassionate towards other life forms. See the rise in popularity of
vegetarianism/veganism, sustainability, biodiversity, and related values over
time. As these ideas spread, it seems the limiting factor in their adoption is
quite possibly our own intelligence: i.e. we don't quite know _how_ to achieve
the levels of production our society requires without doing collateral damage to
other life forms (and very often ourselves, directly or indirectly); but if we
could figure it out, a harmonious existence with all life on Earth seems to be
what most, or at least _many_ of us, would prefer.

So: I am skeptical of any prediction about what values a future superintelligent
AGI may have with respect to other life forms. To be clear I certainly believe
it is possible that it would be indifferent towards humanity in a way that
would be very bad for us; but this hardly seems guaranteed. I have a _hunch_
that it might be more "friendly", for lack of a better word, than many in the
AI existential risk camp expect.

The only thing I believe with any significant conviction on this topic is that
we simply don't know.

[1]: /summaries/lex-fridman-yann-lecun.html
[2]: https://twitter.com/davidchalmers42/status/1647333812584562688
[3]: /summaries/ai-alignment-alchemy-chemistry.html
[4]: https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities
[5]: https://www.lesswrong.com/posts/CoZhXrhpQxpy9xw9y/where-i-agree-and-disagree-with-eliezer
[6]: https://wiki.aiimpacts.org/doku.php?id=arguments_for_ai_risk:is_ai_an_existential_threat_to_humanity:will_malign_ai_agents_control_the_future:argument_for_ai_x-risk_from_competent_malign_agents:start
[7]: /summaries/lex-fridman-eliezer-yudkowsky.html
[8]: /summaries/eight-things-to-know-about-llms.html
[9]: https://every.to/chain-of-thought/ai-and-the-future-of-programming
[10]: /summaries/superintelligent-will.html
[11]: /summaries/basic-ai-drives.html
