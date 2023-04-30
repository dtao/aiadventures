---
date: 2023-05-01
type: interview
summary: Lex Fridman interview with Yann LeCun
url: https://www.youtube.com/watch?v=SGzMElJ11Cc
---

This interview took place over a year ago, in January 2022. I sought it out
because I kept noticing Yann LeCun's name in exchanges with other prominent
figures like Elon Musk, Max Tegmark, and Eliezer Yudkowsky; and LeCun appeared
to be, as far as I could tell, the highest-profile person arguing _against_ the
viewpoint that continued AI research is extremely dangerous. Even [Sam Altman]
[1], despite embracing the ["Let it out" approach to AI safety][2], seems
significantly more concerned about AI safety than LeCun does.

Related: [here's a transcript of a conversation between LeCun and Yudkowsky][3].

To be honest, I struggled to absorb much of the first hour or so of this
conversation. It isn't that it failed to hold my interest; I think it was just
a bit too academic for me to understand given how new I am to the entire field.
LeCun spoke at length about [self-supervised learning][4], which is a technique
for enabling AI systems to develop generalized knowledge of the world, also
known as common sense, which he called the "dark matter" of intelligence.

One casual observation LeCun made that stuck with me was that a human child can
see just a few pictures of an elephant, for example in a children's book, and
from just those few pictures develop a fairly accurate internal model of what an
elephant is. In contrast, machine learning models (at least as of when the
interview took place) require data sets that are orders of magnitude larger.
LeCun believes that the key reason for this is that the human child utilizes
extensive background knowledge that the model doesn't have. He considers this a
relative blind spot among the AI research community, hence the "dark matter"
analogy.

Fridman and LeCun also talked for a bit about Meta, Facebook, the history and
culture of FAIR (at the time, "Facebook AI Research", but now rebranded to
"Fundamental AI Research"), and the global impact of social media as a whole.
Fridman observed that perhaps social media has increased division, but that one
should look at all of its effects, not just one in isolation. Adding to this,
LeCun made an interesting point---that the _printing press_ increased division,
in fact in a huge way, as it gave rise to Protestantism. I myself am not
especially sympathetic towards Facebook, but I found that to be a
thought-provoking point.

Towards the final third of the conversation, I became much more engaged as they
started discussing some truly fascinating topics. One in particular that I
really enjoyed was the mystery of complexity. They were talking about cellular
automata and the phenomenon of emergence. Fridman asked LeCun if he understood
or could explain emergence; he responded that no, it is a mystery to physicists,
chemists, biologists, all scientists.

LeCun noted that there is no rigorous mathematical way of quantifying
complexity. And because we cannot measure it, we cannot validate methods for
reducing it. Complexity, LeCun said, is in the eye of the beholder. He gave the
example of an image of the [MNIST digits][5]: if you took this image and
applied a fixed random permutation to every pixel, the result would appear
chaotic and random. But then you could imagine wearing a special pair of glasses
that reversed the permutation, and what had appeared complicated a moment ago
would suddenly seem simple.

He pointed out that if we were to meet an alien race who viewed the world
differently, as if they were wearing such permutation-reversing glasses, it
could be that what we find simple, they find complex, and vice versa.

It struck me that this is potentially a significant opportunity for someone with
the right skills and insight to have a huge impact on science in general, and
artificial intelligence in particular. The fact that we [seem to be seeing
emergence in modern AI systems][6], yet we lack a robust theoretical or
mathematical undersatnding of emergence, feels imporatnt.

[1]: /summaries/lex-fridman-sam-altman.html
[2]: /thoughts/three-approaches-to-ai-safety.html
[3]: https://www.lesswrong.com/posts/tcEFh3vPS6zEANTFZ/transcript-and-brief-response-to-twitter-conversation
[4]: https://ai.facebook.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/
[5]: https://en.wikipedia.org/wiki/MNIST_database
[6]: /summaries/eight-things-to-know-about-llms.html
