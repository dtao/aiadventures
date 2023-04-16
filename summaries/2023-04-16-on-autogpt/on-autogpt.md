---
date: 2023-04-16
type: article
summary: On AutoGPT
url: https://www.lesswrong.com/posts/566kBoPi76t8KAkoD/on-autogpt
---

I'm not familiar with the work of [Zvi Mowshowitz][1]; this is my first exposure
to his writing. I found his style very readable and engaging.

Overall this paper summarizes the very rapid spread of AI "agents", the most
popular of the moment being called [AutoGPT][2].

_What is an agent?_ I will give my own plain English explanation. This is an
emergent phenomenon, so I _think_ it's fair to say there is no widely-accepted
authority responsible for formalizing definitions when it comes to AI. (I am
sure there are already definitions of "agency" in the worlds of philosophy,
epistemology, and/or some other academic field(s); but I still feel justified
in saying the _application_ of even well-studied concepts to the state of the
art in AI today _must_ be nascent, because the tectonic plates are shifting on
a seemingly daily basis.)

Consider an AI application like ChatGPT. This system responds to human queries.
It never takes any action without some input from a human, typically in the
form of a question or request.

But since ChatGPT has an API (_application programming interface_), it is
possible for a human to write a program that provides constant input to ChatGPT;
the queries keep coming, and so the AI system keeps acting.

This system becomes an **agent** when you make it a "loop": the program prompts
the AI, performs whatever action the AI recommends, then asks the AI
to _generate another prompt_, which the program then sends to the AI, and
repeats. There are a few more pieces than this (for example, the system needs a
data store to act as "memory"), but that's the basic idea.

Probably the most remarkable parts of this paper, to me, are the author's
observations about the role of human... curiosity? recklessness? (are these
different things?)... in accelerating the arrival of whatever dangers AI may
bring.

> One might hope to execute our Plan A of having our AIs not be agents. Alas,
> even if technically feasible (which is not at all clear) that only can work
> if we don't intentionally turn them into agents via wrapping code around
> them. We've checked with actual humans about the possibility of kindly not
> doing that. Didn't go great.
>
> So, Plan B, then.

His overall stance on this seems to be aligned with what OpenAI have asserted as
[their approach to AI safety][3]. I've compared this to how many vaccines work:
by exposing the body to a small, non-critical amount of an antigen, in order to
train the immune system how to generate the right antibodies to fight off the
same threat should it return in greater force.

While this makes sense to me, and I struggle to offer a more pragmatic approach
that is likely to be successful in preparing humanity for what is to come, I
still have misgivings about this when the following observation is also true:

> We also know that no matter how stupid you think an instruction would be to
> give to a self-directed AI agent, no matter how much no movie that starts
> this way could possibly ever end well, that's exactly one of the first things
> someone is going to try, except they're going to go intentionally make it
> even worse than that.
>
> Thus, for example, we already have ChaosGPT, told explicitly to cause mayhem,
> sow distrust and destroy the entire human race. This should at least partially
> answer your question of 'why would an AI want to destroy humanity?' it is
> because humans are going to tell it to do that.

I wish he were making this up, but sadly [he's not][4].

The article goes on to discuss the possibility of testing out the safety of AI
agents by setting them loose in a _game_ world, like a sandbox, to see if they
are able to successfully take control. The author acknowledges that this is a
risky strategy given that it's difficult to be perfectly confident an AI
agent's influence could be contained to an artificial world, particularly if
there are human participants (which there would _need_ to be for it to be a
valid test).

It concludes my making quite a few predictions about how things will play out
from here, and I would describe them as "cynical and probably accurate" (but
perhaps that just means _I_ am cynical), based on the potential power of agents,
and the incentives that exist today and that will only become stronger to use
them for every imaginable use case.

I'll close with one of these predictions, which feels directionally right to me.

> We will, by the end of 2023, have the first agent GPTs that have been
> meaningfully 'set loose' on the internet, without any mechanism available for
> humans to control them or shut them down. Those paying attention will realize
> that we don't actually have a good way to shut the next generation of such a
> thing down if it goes rogue. People will be in denial about the implications,
> and have absolutely zero dignity about the whole thing.

Of course it's impossible to argue with the author's _final_ prediction, which
is that all of his predictions are likely to be wrong and/or he will have
changed his mind about all of this in a month's time. I can relate.

[1]: https://thezvi.wordpress.com/
[2]: https://github.com/Significant-Gravitas/Auto-GPT
[3]: /summaries/our-approach-to-ai-safety.html
[4]: https://decrypt.co/126122/meet-chaos-gpt-ai-tool-destroy-humanity
