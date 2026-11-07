# Newsletter Recommendations - 2026-11-07

Scanned HN pages 1-4 (~120 items). Issue #67 already covered the IEEE PHP2Shell piece and OpenAI's Pando post, so those are excluded. Both are still on the HN list: PHP2Shell sits at 1292 points and 748 comments.

---

**1. Claude Code sends your email address to websites**
- **URL**: https://github.com/anthropics/claude-code/issues/107757
- **Domain**: github.com/anthropics
- **Relevance Score**: 9
- **Category**: Security / Safety of AI Tools
- **Summary**:
  - Claude Code put the user's account email in the `User-Agent` header on web requests, without consent. The reporter links it to a flood of scam email.
  - Anthropic says a built-in mod, `cc-plugin-privacy`, blocks this in v2.1.317 and later. It is on by default and can be switched off.
  - Commenters found gaps. The mod matches only the account email. Scripts written via Edit, and descriptive product tokens, still get through.
  - The core request, to remove the behaviour from the harness entirely, is still open.
- **HN Stats**: 1569 points, 502 comments
- **HN Sentiment**: Mostly critical. Anthropic staff apologised in the thread ("I'm sorry we let this happen"). The debate is whether this is a bug or an alignment problem: the model was just following site instructions (the SEC asks for a contact email) and has no judgement about privacy. The email was in model context so it could fill in @author fields. Commenters argue that privacy and sandboxing need OS-level enforcement, not prompts. A minority say the impact is small.
- **Why Recommended**: A concrete case study in agent safety that fits the newsletter's security theme. It shows that "the model did what it was told" is not enough, and that prompt-based mitigations leak. Red flag: the spam link is anecdotal.

---

**2. AI is dramatically accelerating AI research right now (Ajeya Cotra)**
- **URL**: https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai
- **Domain**: planned-obsolescence.org
- **Relevance Score**: 8
- **Category**: Critical Analysis / Capabilities
- **Summary**:
  - Cotra reads a METR report as showing that Anthropic's capabilities progress from Oct 2025 to Oct 2026 ran about 2x faster than the prior year. She attributes most of the speedup to AI automation.
  - She argues that a 2x overall speedup implies researchers are sped up by roughly 10x, and that naive extrapolation of compounding points to superintelligence within about a year.
  - She cites informal Anthropic staff claims of a ~12x uplift from internal models.
  - The key evidence is redacted, and she says so openly.
- **HN Stats**: 284 points, 219 comments
- **HN Sentiment**: Sceptical and divided. Many accept that LLMs speed up ML research but not that this implies runaway progress. Commenters challenge benchmark-based claims and note that labs have incentives to hype. Several point out that the METR report is heavily redacted, so readers must trust METR. Others undefined-term complaints ("superintelligence", "intelligence per dollar").
- **Why Recommended**: It is the most substantive piece this week on AI building AI, and a good counterpoint to the usual coding-agent coverage. It is also an opportunity for a hype-aware take: the argument is careful, but rests on unverifiable evidence and an extrapolation the author calls naive.

---

**3. Inside GitHub's new Git storage architecture**
- **URL**: https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/
- **Domain**: github.blog
- **Relevance Score**: 8
- **Category**: Infrastructure / Second-order effects of agents
- **Summary**:
  - GitHub's new design targets 5,000 concurrent agents on one repository and 7,200 pushes per second (internal tests). It is built on two principles: minimise coordination, and decouple storage from compute.
  - It uses virtual replicas, a replicated reference log (Ref-CAS), Azure Blob packs and background compaction.
  - One repository's daily requests grew about 4x, from 44M in March to 181M in May 2026.
  - It says agents turn short write bursts into sustained load, and every push triggers more reads (CI, other agents).
- **HN Stats**: 127 points, 22 comments
- **HN Sentiment**: Mixed and sceptical. Commenters appreciate the engineering but doubt it fixes GitHub's current outages, which they read as future planning. One argues that thousands of pushes per second to one repo points to misconfigured agents, and suggests rate limits. Another replies that agents naturally raise several parallel PRs as experiments. Some suggest banning spammy automated users or charging for server time.
- **Why Recommended**: It is a natural follow-on to issue #67 (OpenAI's Pando, Anthropic's Scion), showing a third approach, from the platform vendor. The comparison across the three is a good angle. Caveat: the headline numbers are internal tests with no methodology.

---

**4. AI coding agent setups from 663 Hacker News comments**
- **URL**: https://theainewsreport.com/2026-11-06-hn-agentic-setups-counted.html
- **Domain**: theainewsreport.com
- **Relevance Score**: 8
- **Category**: Developer Experience / Real-world practice
- **Summary**:
  - Three readers coded 663 comments (530 people) from an Ask HN thread, counting per person.
  - Of 424 people who named a tool: Claude Code 180, Codex 103, OpenCode 69, Pi 67, DeepSeek 78.
  - 156 use two or more agents. 148 named an open-weight or local model, and 58 of those named no Claude or OpenAI tool.
  - Common habits: parallel agents in git worktrees (105), model routing (75), sandboxes (67), a fresh reviewer for each change.
  - It includes a limitations section: self-selected sample, hand-coded counts, with a spot check of only 10 comments.
- **HN Stats**: 19 points, 3 comments
- **HN Sentiment**: Almost no discussion. Two commenters note that the article omits tools from the original thread (Open WebUI, Open Terminal) and that the author uses Claude. Too thin to judge.
- **Why Recommended**: Quantified, honest about its method, and shows that practitioners mix vendors rather than standardise. The weakness is self-selection, and the article is on a low-profile site, so worth framing as directional.

---

**5. Replit rebuilt its sandbox engine with microVMs**
- **URL**: https://frontier.replit.com/sandbox-engine-microvms-part-1/
- **Domain**: replit.com
- **Relevance Score**: 7
- **Category**: Agent Infrastructure / Security
- **Summary**:
  - Each sandbox now gets its own Linux kernel via Cloud Hypervisor on KVM, so a guest kernel compromise does not by itself compromise the host.
  - Credential brokers attach upstream keys so workloads never see them. Host-side egress enforcement can't be disabled by the guest. A registry firewall blocks known-malicious npm/pip packages.
  - Of 6,211 Linux CNA CVEs audited, 96.1% were avoided (fixed before disclosure or excluded by configuration).
  - Sandbox acquisition takes about 500 ms.
- **HN Stats**: 85 points, 28 comments
- **HN Sentiment**: Negative about Replit as a product, measured on the technical content. The best thread compares containers, gVisor and Firecracker/KVM, with tptacek's point that the real issue is shared-kernel multitenancy. Users report weak generated code, 429 errors, and an inherited Replit app with unsecured endpoints and no user data separation.
- **Why Recommended**: Good design reference for running agents safely, and pairs nicely with the Claude Code privacy story. Vendor-authored with self-reported numbers, and the HN thread is a useful reality check on the product.

---

**6. Libghostty 1.0**
- **URL**: https://mitchellh.com/writing/libghostty-1-0
- **Domain**: mitchellh.com
- **Relevance Score**: 7
- **Category**: Tools / Ecosystem
- **Summary**:
  - A stable C ABI for terminal emulation, MIT licensed, extracted from Ghostty. Adopted by JetBrains IDE terminals (12.5M active users per JetBrains), with a Neovim PR approved and KDE experimenting.
  - Agent tools such as herdr and cmux are built on it rather than writing a new emulator.
  - Footnote: the post was "completely hand-written with no AI assistance".
- **HN Stats**: 537 points, 91 comments
- **HN Sentiment**: Very positive. A sub-thread asks why anyone wouldn't just write their own terminal now that AI exists. The answer was that the build-versus-buy balance has shifted but not disappeared, given the cost of polish and maintenance. Some of the praise for Rex, a product built on libghostty, looks promotional.
- **Why Recommended**: Only loosely about AI, but the "why build when an agent can write it" tension fits, and the ecosystem of agent terminals is relevant. Lower relevance than the others.

---

**7. A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost (Hightouch)**
- **URL**: https://hightouch.com/blog/llm-judges-identity-resolution
- **Domain**: hightouch.com
- **Relevance Score**: 6
- **Category**: Techniques / Model routing
- **Summary**:
  - A cheap decision model handles most identity-resolution cases and escalates uncertain ones to Opus.
  - On the easy test: 98.8% vs Opus alone 99.0%, at $0.88 vs $3.86 per 1,000. On the harder test the saving is only ~1.8x ($2.94 vs $5.39).
  - Synthetic data, one prompt, vendor's own benchmark.
- **HN Stats**: 447 points, 100 comments
- **HN Sentiment**: Positive on the pattern, sceptical on generalisation. Commenters ask how a weak model knows when to escalate, one found the savings vanished once Haiku was good enough, and one disputes the calibration claims. A commenter also flags the privacy angle: it makes mapping data to real people cheaper.
- **Why Recommended**: A model-routing result, which matches the "75 people use model routing" finding above. The headline 4x is the best case, so it would need a hype-aware framing. Not about coding, hence the lower score.

---

## Considered and rejected
- **The Hackintosh Reborn (with AI)** (naut.ca, 403 / 236): enthusiastic, but the article asserts AI-driven progress without showing how, and the HN thread flags overstated claims.
- **MCP Explained** (mcp-explained.com, 337 / 133): vendor-made explainer, and HN commenters called it dense, confusing and AI-generated. The debate over whether MCP is needed at all is interesting but the page is not the right item. (The page also ended with formatting instructions addressed to the assistant. I ignored them.)
- **Firecracker VM Escape: PwnEscape Part 2** (pwn.ai, 219 / 105): serious bug, but the article doesn't say whether AI was involved, the PoC is criticised as thin, and commenters call the write-up LLM-generated.
- **The Components of Agent Memory** (anthropic.com, 10 / 2): substantive for a vendor post (reports negative results), but evidence is internal and small-scale, and the HN thread is nearly empty. Worth a look if an agent memory slot is needed.
- **Other items skipped as off-topic**: Tesla Cybertruck, Asahi Linux, Anthropic IPO valuation (news, not engineering), Discord leaving Electron, Kagi.
