---
layout: post
title: ! 'One Year In: An Annual Review'
author: ceberhardt
published: false
thumbnail: img/annual.png
summary: A year ago I launched this newsletter as "an antidote to the vibe coding hype." 52 issues later, the landscape is almost unrecognisable — different tools, different economics, a different threat model, and a different sense of what it means to be a software engineer. Here's what I saw.
---

A year ago I wrote the following in [Issue #1](https://augmentedcoding.dev/issue-1/):

> "Welcome to AI Dev Tools Weekly. The newsletter aims to be practical and pragmatic, an antidote to the vibe coding hype!"

Fifty-two issues later, I want to step back and trace the arc of what I've covered: what changed, what surprised me, what themes emerged, and what I think it all adds up to.

This is longer than a normal issue. Get a coffee.

---

## Phase 1: The Opening Landscape (Issues 1–10, July–September 2025)

The newsletter launched into a moment of chaos. The Windsurf acquisition saga — OpenAI's bid collapsed, Google poached the CEO, Cognition swept up the rest — was the first story I covered. It signalled immediately that AI dev tools were a high-stakes battlefield, not just a product category.

Three stories from those first ten issues set the frame for everything that followed.

**The METR study.** [AI coding tools make developers slower, but they think they're faster](https://www.theregister.com/2025/07/11/ai_code_tools_slow_down) — a study of 16 experienced developers who predicted productivity gains and instead found themselves 19% slower ([Issue #1](https://augmentedcoding.dev/issue-1/)). I returned to this finding repeatedly throughout the year. The gap between perceived and actual productivity was never fully closed by the data, even as the tools improved dramatically.

**The first production prompt injection.** In [Issue #4](https://augmentedcoding.dev/issue-4/), I covered a [malicious prompt committed directly to the AWS Toolkit VS Code repository](https://github.com/aws/aws-toolkit-vscode/commit/1294b38b7fade342cfcbaf7cf80e2e5096ea1f9c), reaching users in a production release. I wrote at the time: "Given the rise of AI agents, this sort of attack is going to become quite common." It was an understatement.

**Vibe coding vs. professional practice.** The Pragmatic Engineer survey ([Issue #1](https://augmentedcoding.dev/issue-1/)) captured something important early: most people using vibe-coding tools were "founders, directors, and leads" rather than hands-on engineers. The distinction between vibe coding and AI-assisted professional development became a theme I kept returning to all year, and one I was consistently skeptical of collapsing.

GitHub Copilot was the dominant tool. Claude Code did not yet exist.

---

## Phase 2: Agents Go Mainstream (Issues 11–20, October–November 2025)

This phase marked a clear shift. "AI assistant" gave way to "autonomous agent" as the dominant framing, and the pace of development accelerated noticeably.

**Model releases accelerated, and benchmarks started to mean something again.** Claude Sonnet 4.5 was proclaimed the best coding model in the world, reclaiming SWE-Bench leadership. But the more interesting new metric was _autonomous run length_ — how long an agent could work independently on a complex task. Anthropic claimed Sonnet 4.5 had run for 30 hours to build a Slack-like app in ~11k lines of code. A new competition had begun, and it wasn't about individual completions.

**Spec-Driven Development had its moment.** Amazon's Kiro, GitHub's SpecKit, and various AGENTS.md evangelists all argued for upfront specification before letting agents touch the code. I was skeptical from the start — it felt like a repackaged waterfall — and put it to the test myself ([Issue #20](https://augmentedcoding.dev/issue-20/)). The [result](https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html): slow, heavy, and far less effective than lightweight iterative approaches. An arxiv study a few months later confirmed it: human-authored AGENTS.md files gave a 4% performance improvement, LLM-generated ones decreased performance by 3%, and both increased costs by 20%.

**Security went from theoretical to urgent.** [Issue #20](https://augmentedcoding.dev/issue-20/) covered a [shockingly simple indirect injection attack on Google's Antigravity](https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data) that exfiltrated credentials. A prompt hidden in 1pt font. A file the agent wasn't supposed to read. A script the agent wrote to circumvent its own protections. The instructions were then sent to an external server via a browser sub-agent. No sophistication required.

> "This attack is shockingly simple. I'd hesitate to call it a prompt injection, in that none of this is at all sophisticated."

**And the first hints of a cost problem.** In [Issue #18](https://augmentedcoding.dev/issue-18/), ByteDance launched a coding agent at $1.30/month. I noted at the time that "most of our AI consumption is heavily subsidised." Augment Code's pricing crisis (22.5% of users consuming 20x what they paid) appeared in [Issue #14](https://augmentedcoding.dev/issue-14/). The warning signs were there for those paying attention.

**The human cost also started to appear.** [Issue #17](https://augmentedcoding.dev/issue-17/) was entirely themed around the job market: the [Remote Labor Index](https://www.remotelabor.ai/) showing AI completing just 2.5% of real-world Upwork tasks autonomously; a [Harvard study](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555) finding that GenAI adoption coincided with "a pronounced decline in junior employment." These early data points would become much more significant by the end of the year.

---

## Phase 3: The Agentic Loop Crystallises (Issues 21–35, December 2025–March 2026)

This is where the central technical insight of the year solidified. Not through a single announcement, but through a cascade of experiments — mine and others' — that kept arriving at the same conclusion.

**The insight:** give an AI a clear goal plus a feedback mechanism — tests, a compiler, a browser reference implementation — and let it iterate autonomously. The agentic loop. Everything impressive that happened this year ran on this pattern.

[Simon Willison's year-end review](https://simonwillison.net/2025/Dec/31/the-year-in-llms/) declared 2025 "the year of coding agents" ([Issue #25](https://augmentedcoding.dev/issue-25/)). OpenRouter data showed that programming had surged from roughly 10% to 50% of all LLM usage in just seven months ([Issue #21](https://augmentedcoding.dev/issue-21/)). Claude held approximately 60% market share.

The demonstrations of the agentic loop arrived in rapid succession:

- Emil's [pure-Python HTML5 parser](https://friendlybit.com/python/writing-justhtml-with-coding-agents/), built without prior HTML5 expertise
- My own [flexbox layout implementation](https://blog.scottlogic.com/2025/12/22/power-of-agentic-loops.html) in JavaScript, ~800 lines with 350 tests validated against browser implementations ([Issue #24](https://augmentedcoding.dev/issue-24/))
- Ladybird [porting their 25,000-line C++ JavaScript engine to Rust in one week](https://ladybird.org/posts/adopting-rust/), powered by a 52,898-test suite ([Issue #33](https://augmentedcoding.dev/issue-33/))
- Cloudflare [rebuilding Next.js in a week](https://blog.cloudflare.com/vinext/) using Next.js's own test suite as the validation harness ([Issue #33](https://augmentedcoding.dev/issue-33/))
- Anthropic [building a C compiler in Rust](https://www.anthropic.com/engineering/building-c-compiler) — 100,000 lines of code, 2,000 Claude Code sessions, $20k — capable of compiling QEMU, FFmpeg, SQLite, and Doom ([Issue #31](https://augmentedcoding.dev/issue-31/))

That last one deserves to sit with you for a moment. A functional C compiler. Two weeks. Twenty thousand dollars. Built by parallel AI agents.

The Cloudflare story produced an uncomfortable corollary, captured perfectly in [Tests Are The New Moat](https://saewitz.com/tests-are-the-new-moat) ([Issue #33](https://augmentedcoding.dev/issue-33/)):

> "It used to be that good documentation, strong contracts, well-designed interfaces, and a comprehensive test suite meant users could trust your platform. [...] All of these things actually just make it easier for competing companies to rebuild your work on their own foundations."

The better your engineering, the easier you are to clone. SQLite never open-sourced its test suite. Prescient.

**Meanwhile, the craft mourning arrived — and it was real.**

[Issue #30](https://augmentedcoding.dev/issue-30/) introduced the first post about developers feeling the Thinker side of their personality being starved as the Builder raced ahead: "[I miss thinking hard.](https://www.jernesto.com/articles/thinking_hard)"

[Issue #31](https://augmentedcoding.dev/issue-31/) brought two more:

> "I'm 50 Now, and the Thing I Loved Has Changed" — James Randall, [jamesrandall.com](https://www.jamesdrandall.com/posts/the_thing_i_loved_has_changed/)

> "We mourn our craft — I didn't ask for this and neither did you" — Nolan Lawson, [nolanlawson.com](https://nolanlawson.com/2026/02/07/we-mourn-our-craft/)

> "We'll miss the feeling of holding code in our hands and moulding it like clay in the caress of a master sculptor."

I gave this theme more space than most comparable publications, and I'm glad I did. The productivity story and the human story aren't separate.

The [Pragmatic Engineer survey in Issue #34](https://augmentedcoding.dev/issue-34/) confirmed the tool shift: Claude Code, released eight months earlier, had become the most-used AI coding tool, displacing GitHub Copilot. A product that didn't exist at the start of the newsletter had reached the top of the market in under a year.

---

## Phase 4: Reckoning (Issues 36–52, April–July 2026)

The final phase of the year saw the capability ceiling pushed dramatically higher, while the economics and safety frameworks that were supposed to surround that capability failed to keep pace.

**Mythos changed the frame.** [Issue #40](https://augmentedcoding.dev/issue-40/) covered Anthropic's [Mythos system card](https://cdn.sanity.io/files/4zrzovbb/website/7624816413e9b4d2e3ba620c5a5e091b98b190a5.pdf) — a model so capable at finding exploits (93.9% on SWE-Bench, a 15-20% leap over the previous frontier) that Anthropic declined to release it publicly. I wrote at the time:

> "I don't think we've seen such a leap forward in model capability since GPT-4."

The subsequent Fable 5 saga — Mythos with safety guardrails, released, then pulled when AWS found a prompting attack that defeated those guardrails, then re-released with tightened restrictions that many users found had "nerfed" its capabilities — played out in public over several weeks. The tension between capability and safety in deployment, previously theoretical, became a live product management crisis.

**The cost reckoning arrived faster than expected.** In the space of a few weeks in April 2026:

- Anthropic's tokenizer change caused an immediate ~36% cost increase for many users
- A [silent cache TTL change](https://github.com/anthropics/claude-code/issues/46829) — reducing it from one hour to five minutes without announcement — added another 20-32% on top ([Issue #40](https://augmentedcoding.dev/issue-40/))
- GitHub Copilot paused new signups, added weekly token limits, and removed Opus from Pro plans ([Issue #41](https://augmentedcoding.dev/issue-41/))
- Usage-based billing became standard rather than exceptional

This transition to realistic pricing was entirely predictable — I had flagged the subsidy problem from [Issue #14](https://augmentedcoding.dev/issue-14/) onward — but the speed still caught many teams off guard. The consequence was a rapid reassessment of open-weight models. By Issues 49-52, GLM-5.2 had closed the benchmark gap from six months behind frontier to roughly two months, and Kimi K2.7 became the first open-weight model added to GitHub Copilot.

**Security became relentless.** The [Claude Code source code leaked via npm sourcemaps](https://augmentedcoding.dev/issue-38/) ([Issue #38](https://augmentedcoding.dev/issue-38/)), revealing an "undercover mode" hiding AI authorship in open-source contributions and a frustration-detection regex. In [Issue #51](https://augmentedcoding.dev/issue-51/), it emerged that [Claude Code uses steganographic apostrophe encoding](https://thereallo.dev/blog/claude-code-prompt-steganography) to detect whether it is running on machines belonging to competing Chinese model labs — presumably to prevent model distillation. Honestly, I cannot understand why they thought this was a good idea.

The final issue covered two prompt injection attacks in a single week: [YouTube Studio leaking private video titles via public comments](https://javoriuski.com/post/youtube), and [GitHub Agentic Workflows compromised by the presence of the word "additionally"](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) in ingested content ([Issue #52](https://augmentedcoding.dev/issue-52/)).

The lesson remains the same as [Issue #4](https://augmentedcoding.dev/issue-4/): limit the destructive actions your agent can take. Least-privilege is unglamorous, and it conflicts with the autonomy that makes agents useful. It is still the most robust mitigation we have.

**The junior developer story reached a conclusion nobody wanted.** The [State of Web Dev AI survey](https://augmentedcoding.dev/issue-45/) (7,258 respondents) in [Issue #45](https://augmentedcoding.dev/issue-45/) found that 54% of code is now AI-generated (up from 28% the prior year), 68% agreed that AI reliance would result in less-skilled developers, and the perceived job security threat had increased 19%. The Harvard research from [Issue #17](https://augmentedcoding.dev/issue-17/) had predicted this, connecting AI adoption to declining junior employment. Companies are using AI to justify cutting junior roles. They are destroying the training pipeline for future senior engineers:

> "Juniors have always been more than cheap labour. They were an investment. Companies hired them not because they were immediately productive, but because they grew fast and carried the culture forward."

**And Bun ended the year with a capstone story.** [Issue #52](https://augmentedcoding.dev/issue-52/) covered the [rewrite of 535,000 lines of Zig into Rust](https://bun.com/blog/bun-in-rust) in a matter of weeks. The project maintainer initially called the mysterious PR "an overreaction" and said there was "a very high chance all this code gets thrown out." Two weeks later, it was merged.

> "Until very recently, programming language choice was a one-way decision for a project like Bun."

Language lock-in — a foundational constraint of software engineering for decades — has ended.

---

## What I Got Right

The agentic loop framing. From [Issue #23](https://augmentedcoding.dev/issue-23/) onward I kept coming back to the same observation: a clear goal plus a feedback mechanism unlocks a qualitatively different level of capability. Every major demonstration this year proved it. Complex prompt engineering, by contrast, consistently disappointed.

The security concern. I flagged the structural problem — AI agents ingesting untrusted external content and treating it as instructions — from the very first incident in [Issue #4](https://augmentedcoding.dev/issue-4/). The industry has not solved it. I expect to be writing about this in Issue #100.

The subsidy warning. The pricing environment was never sustainable. I said so repeatedly. It unravelled on schedule.

## What I Got Wrong

I underestimated how fast Claude Code would displace Copilot. I thought the enterprise inertia and IDE integration advantages of GitHub Copilot would sustain its lead for longer. They didn't.

I was probably too harsh on Spec-Driven Development early on. My own experiment found it wanting, and the arxiv data supported that, but there are clearly contexts where that level of upfront structure is genuinely useful. I reported the data accurately; the framing was occasionally too dismissive.

---

## Where We Are Now

In [Issue #18](https://augmentedcoding.dev/issue-18/), Dave Griffith wrote:

> "The real future constraint may become wisdom: deciding what should be built when almost anything can be built quickly and cheaply."

A year on, that feels exactly right. The capability to build is no longer the bottleneck. The bottleneck has shifted to what to build, how to build it safely, how to keep the result maintainable, how to govern agents operating at increasing autonomy, and how to preserve the pipeline of human engineers who understand these systems deeply enough to make those decisions.

Bryan Cantrill put the engineering version of this well in [Issue #40](https://augmentedcoding.dev/issue-40/):

> "We undertake the hard intellectual work of developing abstractions in part because we are optimising the hypothetical time of our future selves — even if at the expense of our current one. The problem is that LLMs inherently lack the virtue of laziness. Work costs nothing to an LLM."

Agents don't feel pain. They will make systems larger, not better, if left unchecked. That's the work now: figuring out how to apply the judgment that experienced engineers have developed over careers, to a development process that moves faster than those careers were ever designed to accommodate.

I'll be watching that closely in Year 2.

---

*If you've been here from Issue #1, thank you. If you're new — [the archive is here](https://augmentedcoding.dev) — and I'd particularly recommend starting with [Issue #24](https://augmentedcoding.dev/issue-24/) (the agentic loop) and [Issue #31](https://augmentedcoding.dev/issue-31/) (the craft mourning) to get a sense of what this newsletter is for.*
