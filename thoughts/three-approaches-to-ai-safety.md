---
date: 2023-04-17
type: thought
summary: Three Approaches to AI Safety
---

A lot of people know that there are seismic shifts happening right now with
artificial intelligence.

A lot of people may _not_ know that many of those driving much of the
progress here, in both research and industry, are very concerned about the
dangers of AI. This includes Elon Musk, Steve Wozniak, Andrew Yang, and many
other researchers, executives, and other prominent figures who [published an
open letter in March][1] imploring all AI labs to pause AI experiments for 6
months. It also includes the researcher Eliezer Yudkowsky who, along with many
others, believes AI will [inevitably lead to human extinction][2].

To truly appreciate the depth and urgency of this concern, consider that the
**majority** of [AI researchers polled in a 2022 survey][3] estimated somewhere
between a 5-10% probability of AI "causing human extinction or similarly
permanent and severe disempowerment of the human species". _(There were two
similarly worded questions to this effect, with median responses of 5% and
10%.)_

Given this state of affairs it should not be surprising that quite a lot of
thought (although most of the individuals above would argue not _enough_
thought!) has been put into the topic of AI safety: how best to responsibly
proceed with artificial intelligence without leading to the downfall of
civilization. Broadly I am aware of two approaches that are being explicitly
championed by thought leaders in this space; and there is a third approach that
I think is pretty obvious, and which I think it is safe to assume is being
implicitly pursued by at least a percentage of those in positions of power who
care about this topic.

These approaches are:

1. Shut it down (terminate)
2. Let it out (inoculate)
3. Wall it off (consolidate)

### 1. Shut it down (terminate)

The most dramatic proposal on the table that I'm aware of is to completely shut
down AI research. This is what Eliezer Yudkowsky is advocating. In his article
published in Time magazine (linked above), he writes:

> Frame nothing as a conflict between national interests, have it clear that
> anyone talking of arms races is a fool. That we all live or die as one, in
> this, is not a policy but a fact of nature. Make it explicit in international
> diplomacy that preventing AI extinction scenarios is considered a priority
> above preventing a full nuclear exchange, and that allied nuclear countries
> are willing to run some risk of nuclear exchange if that's what it takes to
> reduce the risk of large AI training runs.

Here is my oversimplified version of the argument for this:

1. **Superintelligent AGI, when achieved, will be unstoppable by humans.** (I
   think of this as AI achieving "escape velocity", at which point human
   intelligence, like gravity, will no longer be able to contain it.)
2. **Superintelligent AGI is likely to result in human extinction**, because it
   will be _capable_ of exterminating us, and we don't know how to instill it
   with values or design it in such a way to make sure it doesn't do that.
3. **We don't get multiple tries to solve this problem.** Unlike every other
   line of scientific research up to this point in human history, we don't have
   the luxury of learning from failed experiments and forming new hypotheses if
   we get this one wrong on the first attempt. The "failed experiment" would be
   that AI kills everyone.
4. **This isn't just a theoretical problem anymore**; with the surprising rate
   of progress in LLMs like GPT-4 we are racing towards superintelligent AGI
   faster than many researchers anticipated. Therefore we are already too close
   for comfort to point 1 above, and the only sane thing to do is just stop.

Personally, the part of this argument I have the hardest time subscribing to is
the 2nd point. It's possible I simply haven't come across the version of this
point that resonates for me. But my best attempt to explain it, for now, is
that we don't have a robust argument for why a superintelligent AI would
_not_ wipe us out. I'm genuinely not sure if this is a logical argument or a
pragmatic one; i.e. "If we aren't confident it won't happen, we ought to
assume it will happen."

Silly reference: this is sort of the same point Bruce Wayne makes in the film
[Batman v Superman][4] when explaining why he believes he needs to fight
Superman.

> If we believe there's even a one percent chance that he is our enemy we have
> to take it as an absolute certainty.

_Note: I am not saying this is the same as Yudkowsky's argument. Rather, it is
the same as my probably-wrong attempt to represent Yudkowsky's argument, given
my very shallow understanding of it._

#### Is this even possible?

It isn't obvious to me this is possible. But I _am_ currently listening to Lex
Fridman's interview with Max Tegmark, who replied to this question in the
affirmative and gave the example of human cloning.

According to Tegmark, we gained the technological capability of cloning humans
decades ago; but thanks to public pressure we collectively avoided ever
actually doing it. (He shared that there is one known historical case of a
Chinese scientist doing it, but he was subsequently imprisoned by the Chinese
government.)

#### And then what?

Something I'm not currently sure about is whether Yudkowsky and others arguing
for the "Shut it down" approach believe we should ever _resume_ AI research
after shutting it down. Should we just discard everything we know so far? Lock
it up and throw away the key?

Or are there some thresholds we need to reach, e.g. in the areas of alignment
and interpretability, after which it will be safe to pick up where we left
off? (Is there any chance we could ever reach these thresholds _without_
continuing research into more advanced AI? Sam Altman doesn't think so,
according to my memory of [his conversation with Lex Fridman][5].)

#### 1.1 ...or we could just _slow_ it down (decelerate)

A less dramatic proposal than _shutting down_ AI research is to hit the pause
button for a little while and give AI safety researchers some time to catch up.
This is effectively what the [open letter][1] that Musk et al signed is
suggesting. The letter proposes a 6-month pause on any AI experiments using
systems as powerful as GPT-4 or greater.

During this time, the letter advocates for AI labs to collectively focus on
safety, not building more powerful systems; and it also encourages AI developers
and policymakers to collaborate on instituting thoughtful regulation to direct
the safe development of AI systems moving forward.

### 2. Let it out (inoculate)

If the first approach to safety, i.e. "Shut it down", is analogous to a
quarantine, then the second approach, "Let it out", would be more like a
an inoculation campaign.

Think of the development and spread of AI like a contagion. Preventing the
spread of an infectious disease via quarantine can be very effective, but it
requires significant coordination. This is achievable to some extent in states
with powerful centralized control (e.g. China). It turns out to be much harder
in parts of the world with far greater individual freedom (e.g. the United
States).

However, even in the parts of the world that are more centrally controlled,
globalization makes it difficult if not impossible to _truly_ contain a highly
infectious contagion, when people are still passing in and out of the country's
borders.

An alternative approach is to willingly allow the contagion to spread, to give
the population some opportunity to develop natural immunity to it. (You could
also try to develop a vaccine, which would have a similar effect. Interestingly,
if you think about it, the way a vaccine works is more or less a microscopic
version of the same phenomenon that happens with a population developing natural
immunity through infection. It's just on the scale of a single human body versus
an entire population.)

This is the approach that [OpenAI assert they are taking][6]: exposing the world
to AI capabilities as they're developed so that we can build up natural defenses
against them.

#### Is this even possible?

It does seem possible to me. As I [pondered yesterday][7], to be successful with
this strategy inoculating for _any_ threat seems to require at least two things:

1. You need to be able to present a **non-lethal dose of the threat**. If the
   smallest amount we can produce is already lethal, then we'll die. With AI,
   part of the risk we're facing is that we may not recognize when we've already
   exceeded this dosage. (Again, this is Yudkowsky's fear.)
2. The recipient needs to be capable of **developing effective antibodies**. A
   vaccine doesn't do you any good if it just makes you sick, and your body
   doesn't develop any new defenses as a result. Thus far it's difficult to say
   whether we are hardening ourselves against more powerful AI in any meaningful
   way. We probably are in some ways, e.g. the [open letter][1] raising
   awareness of the dangers of AI and inspiring some smart scientists to get
   more involved. On the other hand, people _are_ [already trying to get AI to
   destroy the world][8]. So it's a mixed bag.

#### And then what?

I think the hope with this approach is that eventually, by the time we do
inevitably achieve superintelligent AGI, human society will have developed a
robust set of defenses (effective strategies for achieving alignment and
ensuring AI safety, international agreements enforcing safe deployment,
education programs, etc.) to protect ourselves.

Let's hope so!

### 3. Wall it off (consolidate)

I haven't heard anyone explicitly advocating for this approach. In fact, what
I'm about to describe as an _approach to AI safety_ is more commonly identified
as a _concern_ that many people justifiably have about the future of AI.

Nonetheless, while this would be bad in many ways, another path towards making
the development of AI _more_ safe, I suspect, would be to restrict access to a
much smaller group of humans. Realistically this would be AI labs at major
corporations, and world governments. Public APIs like ChatGPT, DALL-E 2,
Midjourney, and others would be taken offline. Open source projects providing
reusable building blocks for building AI systems would be removed from public
repositories and made illegal to use with steep penalties.

I realize this all feels a bit dystopian, and it probably would be. It would
also put us in that really unfortunate position of immense power being
consolidated under a tiny percentage of human beings on the planet, and large
corporations such as Microsoft and Google exerting more control than ever
before. (Alternately the government could claim all of the power, which probably
wouldn't be much better.)

_How is this an approach to safety at all?_ It would significantly reduce the
surface area of the existential risk we face. It would make AI research much
more like the Manhattan Project, where a small team of scientists with top
security clearance worked on a very dangerous technology that was not shared
with the general public. Yes, this put tremendous power into the hands of very
few; and yes, it still led to the creation of some incredibly destructive
technology, resulting in the loss of millions of lives.

But what is happening today is a bit like if all of the research conducted for
the Manhattan Project were published in real time, daily, in every newspaper in
the country. And if the materials to make nuclear weapons at home were readily
available to everyone. (Well, maybe not _quite_ like that last part. I don't
have a great feel yet for the amount of computing power you actually need to
create something like GPT-4. But given the sheer number of personal computers
connected to the Internet and the fact that peer-to-peer technology is an
established thing, it's difficult for me to imagine that orchestrating that
much computing power would truly be prohibitive.)

I will say this. At a high level, it seems like a good thing that the number of
people with the power to launch nuclear weapons is very small. I would prefer
for it to be zero; but if it's going to be a positive number, I'm glad it's in
the single digits and not in the millions.

#### Is this even possible?

Once again, I'm not sure. If the U.S. government passed a law _tomorrow_ making
AI illegal everywhere... would the development stop? The consequences would have
to be absolutely massive, and there would need to be unmistakable early
demonstrations of the government's commitment to enforcing the law. Like "Sam
Altman sentenced to life in prison" or "Google fined $100 billion" or something
like that.

It's really hard for me to imagine that happening, but what do _I_ know?

#### And then what?

Again, good question. The future where humanity _survives_ but we're all
powerless to resist the permanent control of a monopolistic organization, or an
iron-fisted government, doesn't exactly feel like one to aspire to. I suppose I
would probably still pick it over extinction.

Ben Franklin [would not approve][9]:

> Those who would give up essential liberty to purchase a little temporary
> safety, deserve neither liberty nor safety.

On the other hand, I'm also not sure how much thought Ben Franklin put into AI.

[1]: https://futureoflife.org/open-letter/pause-giant-ai-experiments/
[2]: https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/
[3]: https://aiimpacts.org/2022-expert-survey-on-progress-in-ai/
[4]: https://www.imdb.com/title/tt2975590/
[5]: /summaries/lex-fridman-sam-altman.html
[6]: /summaries/our-approach-to-ai-safety.html
[7]: https://twitter.com/dan_tao/status/1647699714203176960
[8]: /summaries/on-autogpt.html
[9]: https://www.goodreads.com/quotes/140634
