---
date: 2023-04-29
type: paper
summary: The Superintelligent Will
subtitle: Motivation and Instrumental Rationality in Advanced Artificial Agents
author: Nick Bostrom
url: https://nickbostrom.com/superintelligentwill.pdf
---

This paper formally introduces two concepts. The first is the **orthogonality
thesis**, which says that intelligence and goals are independent of each other.
E.g. you could have a superintelligent AI that wants to help humanity, or you
could have a superintelligent AI that wants to kill humanity, or you could have
a superintelligent AI that wants to make paperclips. The second is
**instrumental convergence**, which is Bostrom's interpretation of the concepts
introduced by Steve Omohundro in [The Basic AI Drives][1].

I responded similarly to this paper as I did to Omohundro's paper. I'll just
quote myself:

> I'm not sure why, but I was expecting something much more scientifically
> rigorous. What do I mean by that? I think I was expecting either some
> over-my-head mathematical proofs, or else empirical evidence supporting these
> claims. As far as I can tell, it _seems_ like these are basically
> well-articulated intuitions about how AI systems might develop.

Reflecting on the paper a bit further, I notice that its cogence for me depends
greatly on how I think about it.

If I view it as **a set of predictions about how AI systems will develop**, then
I find it unconvincing.

On the other hand, if I view it as **a response to _alternative_ predictions
about the risks of AI systems**, then suddenly the points resonate much more
strongly with me.

---

### As predictions

I expressed a decent amount of skepticism towards the ideas of instrumental
convergence already in my [summary of Omohundro's paper][1].

With respect to orthogonality, I would say I'm agnostic. I don't dispute that
_logically_ we can imagine intelligence and purpose as independent axes. In
practice, though, I don't know that we can separate them in any reliable
way---and it seems like we would _need_ to be able to do that to confidently
declare them to be orthogonal.

To be specific: I would not be surprised if it turned out there isn't any
practical way to create an intelligent system that _just_ wants to play chess,
or make paperclips, or any other mundane task like that. I just have a hunch
that increased cognitive capabilities inexorably lead to more complex goals in
ways that cannot be avoided. Whether there are mathematical or natural forces
that might lead to those emergent goals clustering in some way, I can only
guess.

I also mentioned this [here][2]: I have an inkling that orthogonality and
instrumental convergence might actually be contradictory ideas, made
artificially coherent by an invented distinction between intermediate goals and
so-called "final" goals. The orthogonality thesis relies on the concept of final
goals, but Bostrom himself entertains a line of thought that, to me, undermines
this concept:

> We humans often seem happy to let our final goals and values drift. This
> might often be because we do not know precisely what they are.

My gut says that the idea of AI having "final" goals is a red herring; that AI
researchers will increasingly find greater success in both capability _and_
alignment by developing systems that exhibit open-ended goal discovery,
refinement, and even replacement; and that as a result, much of what has been
written about AI referencing final goals to date will become moot.

### As a response to alternative predictions

Now that I've expressed so much skepticism towards this paper, I will
acknowledge that a totally different interpretation of Bostrom's points may be
more appropriate.

I _suspect_ this is actually the case, given the way he phrases his concluding
section:

> we cannot blithely assume that a superintelligence will necessarily share any
> of the final values stereotypically associated with wisdom and intellectual
> development in humans

And:

> we cannot blithely assume that a superintelligence with the final goal of
> calculating the decimals of pi (or making paperclips, or counting grains of
> sand) would limit its activities in such a way as to not materially infringe
> on human interests

I wholeheartedly agree with both of these statements.

Put another way: maybe it isn't that Bostrom is saying, "Orthogonality is
definitely true, and instrumental convergence is definitely real." Rather, I
think he is saying, "Orthogonality _could_ be true, and instrumental convergence
_could_ be real; and we would be wise to act accordingly."

This makes a lot more sense to me. From this angle, the burden of proof would
not be on Bostrom to made an ironclad argument that these two theses would
necessarily apply to any and all AI systems. The burden of proof would be on
those neglecting to take these ideas seriously to explain why we _can_ safely
assume that AI without explicit instructions to do harm would be harmless.

Then again... perhaps even if such a thing could be proved, it wouldn't do us
much good considering that [people _will_ explicitly give AI instructions to do
harm][3].

[1]: /summary/basic-ai-drives.html
[2]: /thoughts/explaining-ai-terms-the-feynman-way-pt1.html
[3]: /summary/on-autogpt.html
