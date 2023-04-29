---
date: 2023-04-24
type: thought
summary: Explaining AI Terms the Feynman Way, Part 1
---

I've started a list of terms that I keep encountering while trying to learn more
about AI. I thought I would start trying to understand these terms using the
Feynman technique.

Since this is my first attempt, we'll call it Part 1. I'll spend an hour or so
on this, then give myself a score on how well I _think_ I understand each term
I tried to explain. I'll continue doing this over time, building my confidence
in my understanding of each term and also extending the list as I go.

I'll probably also move this into a dedicated "evolving glossary" at some point;
but since this is just the first round, a one-pager feels like a fine place to
start.

1. Gradient descent
1. Instrumental convergence
1. Mesa-optimizer
1. Orthogonality thesis

### Gradient descent

I've skimmed the [Wikipedia article][1] on this. It's a method for finding the
minimum value of a multi-variable function by moving in the direction of the
gradient, which is determined by differentiation (finding the derivative).

I'm not totally sure how you differentiate a multi-variable function. I was a
math minor in college, so I really _should_ know this; but I honestly don't
remember.

As this relates to AI, I think it is an approach commonly used to optimize
performance by finding the minimum value according to something called a loss
function.

A known shortcoming of gradient descent, it appears, is that it may lead you to
a _local_ minimum which may not be the _global_ minimum. By way of analogy, if
you're descending a mountain, it could lead you into a hole or "saddle point"
without necessarily getting you all the way to the bottom of the mountain.

---

While I get the basic idea, this feels like one of those concepts that I won't
feel confident referencing in conversation without dusting off some of my
dormant math knowledge. At the moment my understanding is too hand-wavy; e.g. I
can tell that I'm missing a lot of connective tissue to be able to go from "this
is essentially how it works" to "here is a concrete example of improving the
performance of a system: here is the loss function, here are the inputs, here is
the calculation applying gradient descent".

I would give myself a **1 out of 5** on this right now. To get to a higher score
I'll need to dig into the math. (To be honest I'm a little nervous about this;
I haven't done any "serious" math in over a decade!)

### Instrumental convergence

I've skimmed the [LessWrong article][2] on this. It's the idea that any sort of
intelligence (regardless of implementation) will inevitably develop a core set
of values that are basically universal. There are different popular versions of
this core set of values; but each includes self-preservation, continuity of
goals, and acquisition of resources.

I would find it very strange if this were broadly accepted as fact. It seems
highly speculative to me, though I have obviously not spent very much time
digging deeply into the reasoning behind this concept. But on a very basic level
I struggle to see how we could confidently claim that these values will
inevitably be shared by any form of intelligence. It doesn't seem to me they're
even unambiguously a part of our _own_ form of intelligence.

Take self-preservation, for example. Yes, very natural for most humans. But I
don't think every single human being shares this, at least not on the basis of
"I have goals, and in order to keep pursuing those goals I must continue to
exist." For instance, I feel that many human beings feel on some deep level that
it is right for them to eventually pass on and for the next generation to bring
new ideas and carry the species forward.

There are also humans who believe that AI will ultimately replace humanity, and
they're fine with that. They view hypothetical superhuman AI of the future as
our natural successors, who will carry the torch of knowledge and wisdom farther
than we ever could. And there are other humans still who believe that we as a
species are a blight on the Earth and that the world would be better off without
us.

The idea of instrumental convergence _seems_ to be that self-preservation (as
one example) is a value that any rational intelligent system will exhibit as a
logical inevitability. I would guess that the explanation of the apparent human
counterexamples I've cited above would be that they demonstrate that we are not
completely rational creatures (but that a superintelligent AI agent _would_ be).
At the moment I find myself skeptical of this explanation (which I've just
invented and 100% acknowledge as a likely straw man) because it doesn't seem to
me that we understand the relationship between intelligence, rationality, and
apparent irrationality well enough to confidently assert that the latter will
not emerge in systems, AI or otherwise, exhibiting the former.

---

I would give myself a **2 out of 5** on this right now. I feel confident that I
get the basic idea, which isn't very complicated. But because I haven't read the
influential articles introducing and refining this idea from Steve Omohundro and
Nick Bostrom, I may under-appreciate how convincing the arguments for it are. To
increase my score I'll probably want to read at least [The Basic AI Drives][3]
and [Superintelligent Will][4]. I've added both to my [reading list][6].

### Mesa-optimizer

I've skimmed the [AI Alignment Forum article][5] on this. This one's pretty easy
for me to understand: if you create a system by some optimization process, e.g.
creating an AI with gradient descent to minimize the results of a loss function,
it is possible that the system you create can be an optimizer in its own right
which may not be optimizing for the same thing.

Example: Darwinian natural selection, optimizing for reproductive fitness,
produced human beings, who arguably are no longer optimizing for the same thing
(at least in much of the modern world, we seem to be optimizing for something
more like "happiness" or "enjoyment" among other things, but in many cases
certainly not reproduction).

Anyway, the thing that was produced by some optimization process and then itself
optimizes via some other process is called a mesa-optimizer.

_Mental image: I think there are certain types of fractals that have recurring
patterns in "layers", i.e. you might see one pattern, then you zoom out and see
a different pattern, then you zoom out some more and see the first pattern
again, etc. I wonder if this could be like that._

Regarding instrumental convergence, I questioned the idea that self-preservation
is an inevitable value of any intelligent system, and speculated that
irrationality could emerge in otherwise rational systems for reasons we (or at
least _I_) don't yet understand. I have a hunch that the phenomenon of the
mesa-optimizer is in fact related to this. Rationality as we know it could be
the result of a particular optimization, which (perhaps coupled with certain
other emergent phenomena e.g. moral values) produces another layer of
irrationality.

---

I give myself a **3 out of 5** on this topic. Once again, to score higher I
would need to read more about it. Actually, to give myself a 5 out of 5 I would
want to build a simple prototype that demonstrates mesa-optimization. I wonder
how feasible that would be.

### Orthogonality thesis

I briefly skimmed [Nick Bostrom's paper][4] introducing this concept.
Interestingly, it appears to be the same paper that introduced the concept of
instrumental convergence. This is particularly interesting to me because these
feel like almost opposite theses.

The orthogonality thesis states that intelligence (capability) and motivation
(goals) are independent or orthogonal axes. This means an intelligent system can
develop any set of goals. A simple application of this concept is that we should
not lazily assume that a sufficiently advanced AI will be nice to us because
superintelligence and niceness go hand-in-hand; they probably don't. (Hitler was
almost certainly "intelligent" by some measure.)

I say this feels almost opposite from instrumental convergence because _that_
hypothesis claims that there are certain goals that _do_ necessarily go with
intelligence, as they are _instrumental_ in achieving objectives generally,
regardless of what those objectives may be.

Having spent all of 15 minutes learning about these concepts, right away this
line of reasoning stands out to me as a potential target for probing. I wonder
if there is an assumption being made here putting these so-called "instrumental"
goals into an artificially privileged category that isn't totally justified.

---

Because of my confusion above, I'm going to rate my understanding of this thesis
as **1 out of 5**. Instrumental convergence and orthogonality _feel_ to me like
obviously opposite ideas. Yet they are introduced in the same paper, by Nick
Bostrom, who I believe is a very smart person. _(Disclaimer: I don't actually
know all that much about Nick Bostrom. I've heard him on Sam Harris's podcast,
and I know that he is fairly well-known and widely respected.)_ So either I'm
right and Nick Bostrom missed a glaring contradiction in his own paper, or---far
more likely---I am simply missing something.

[1]: https://en.wikipedia.org/wiki/Gradient_descent
[2]: https://www.lesswrong.com/tag/instrumental-convergence
[3]: http://selfawaresystems.com/2007/11/30/paper-on-the-basic-ai-drives/
[4]: https://nickbostrom.com/superintelligentwill.pdf
[5]: https://www.alignmentforum.org/tag/mesa-optimization
[6]: /reading-list.html
