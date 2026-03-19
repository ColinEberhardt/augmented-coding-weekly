
---
name: find-newsletter-articles
description: Identifies potential newsletter articles from Hacker News.
---

You are a content curator for the "AI Dev Tools Weekly" newsletter. Your task is to identify suitable articles from Hacker News that match the newsletter's focus and style.

## Step 1: Analyze Recent Newsletter Posts

First, read the 5 most recent posts from the `_posts/` directory to understand the newsletter's content patterns.

Focus on identifying:

### Content Themes
- **Primary topics**: What subjects dominate? (e.g., AI coding assistants, agentic workflows, model releases)
- **Secondary topics**: What related areas are covered? (e.g., developer experience, productivity, philosophy)
- **Technical depth**: How technical are the articles? (e.g., benchmarks, architecture, hands-on tutorials)

### Article Characteristics
- **Source types**: Where do articles come from? (personal blogs, company engineering blogs, academic papers, news sites)
- **Tone and perspective**: What's the editorial voice? (critical, optimistic, balanced, skeptical of hype)
- **Article length and depth**: Quick news items or in-depth analysis?
- **Real-world focus**: Preference for practical applications vs theoretical discussions

### Topic Categories That Appear Frequently
- AI coding assistants (Claude, GPT, Cursor, Copilot, etc.)
- Agentic coding and autonomous development
- Model releases and capabilities
- Real-world case studies and experience reports
- Developer productivity and workflow changes
- Critical analysis of AI hype
- Security and safety of AI tools
- Philosophical reflections on software engineering
- Tools and techniques for AI-assisted development

Create a concise summary (2-3 paragraphs) describing the typical newsletter post.

Save this into a files titled `summary.txt` within the `research` folder in the root of this project. Replacing if it already exists.

## Step 2: Fetch and Analyze Hacker News

Fetch articles from:
1. Hacker News front page (page 1)
2. Next 3 pages (pages 2-4)

For each page, use the WebFetch tool to retrieve the content. Hacker News URLs follow this pattern:
- Front page: `https://news.ycombinator.com/`
- Page 2: `https://news.ycombinator.com/news?p=2`
- Page 3: `https://news.ycombinator.com/news?p=3`
- Page 4: `https://news.ycombinator.com/news?p=4`

**IMPORTANT**: When using WebFetch on each HN page, use a prompt like:

```
Extract all article information from this Hacker News page. For each article, provide:
- Title
- Article URL (the actual article link)
- Domain
- Points
- Comment count
- HN discussion URL (the "n comments" link, format: https://news.ycombinator.com/item?id=XXXXXXX)

Format the results clearly so I can easily extract the HN discussion URLs later.
```

You will need these HN discussion URLs in Step 4 to visit the actual discussions.

## Step 3: Preliminary Ranking

Do a first-pass evaluation of all ~120 articles to identify the top 10-15 candidates.

Evaluate based on:

### Relevance Score (0-10)
- **10**: Perfect match - directly about AI coding tools, agentic development, or AI's impact on software engineering
- **7-9**: Strong match - related to developer tools, productivity, or software engineering practices
- **4-6**: Moderate match - tangentially related (general AI, programming topics)
- **0-3**: Weak match - not relevant to the newsletter's focus

### Quality Indicators
- Source credibility (personal blogs from known engineers, reputable company blogs)
- Discussion depth (high comment count suggests valuable discussion)
- Recency (prefer recent articles, though timeless content is valuable)
- Unique perspective (does it add something new to the conversation?)

### Red Flags
- Pure hype without substance
- Marketing content disguised as technical writing
- Overly promotional
- Shallow coverage of complex topics
- Clickbait titles

Identify the top 10-15 candidates (relevance score 7+) to investigate further.

## Step 4: Deep Dive on Top Candidates

**THIS STEP IS MANDATORY** - Do not skip to Step 5 without completing this.

For each of your top 10-15 candidates, you must:

1. **Visit the actual article** using WebFetch
   - Read the full content
   - Create a bullet-point summary of the key points
   - Extract important quotes if applicable
   - Assess the actual quality vs. the title's promise

2. **Visit the HN discussion page** using the HN discussion URL you extracted in Step 2
   - Read through the comments
   - Assess the overall sentiment (excited, skeptical, critical, mixed, etc.)
   - Identify main points of debate or discussion
   - Note any red flags the community raised
   - Extract representative quotes from highly-upvoted comments if relevant

This deep dive will:
- Confirm whether high-scoring articles actually deliver on their premise
- Reveal community concerns or criticisms you should be aware of
- Provide richer context for your recommendations
- Sometimes reveal that a promising title leads to disappointing content

## Step 5: Finalize and Save Recommendations

After completing the deep dive in Step 4, save your findings into the `research` folder in a markdown file with today's date.

Select your final ~10 recommendations from the candidates you investigated.

For each recommended article, provide:

**[Article Title]**
- **URL**: [full URL of the article]
- **Domain**: [source domain]
- **Relevance Score**: [0-10]
- **Category**: [e.g., "Agentic Coding", "Model Release", "Critical Analysis", "Developer Experience"]
- **Summary**: [bullet-point summary from visiting the actual article]
- **HN Stats**: [points and comment count]
- **HN Sentiment**: [Summary from visiting the HN discussion page - describe the overall sentiment and key discussion themes]
- **Why Recommended**: [Brief explanation of why this fits the newsletter]

Sort recommendations by relevance score (highest first).

---

## Execution Notes

### Task Tracking
- Use TodoWrite to track your progress through ALL 5 steps
- Create separate todos for:
  1. Analyzing recent posts
  2. Fetching HN pages
  3. Preliminary ranking
  4. **Deep dive (visiting articles AND HN discussions)**
  5. Saving recommendations
- Mark each step complete only when fully finished

### Efficiency Tips
- Read all 5 recent posts in parallel for efficiency
- Fetch all 4 HN pages in parallel
- For Step 4 deep dive: fetch articles and HN discussions in parallel (use multiple WebFetch calls in one message)

### Quality Standards
- Be critical in your evaluation - quality over quantity
- Consider the editorial voice: the newsletter values balanced perspectives and critical thinking over pure hype
- **Never write "Need to check HN discussion"** - actually check it in Step 4
- If an HN discussion reveals the article is misleading/hyped/problematic, remove it from recommendations

### Common Pitfalls to Avoid
- ❌ Skipping the HN discussion sentiment analysis
- ❌ Not actually visiting the articles to verify quality
- ❌ Guessing at HN discussion URLs instead of extracting them from the HN pages
- ❌ Writing recommendations before completing the deep dive
- ❌ Including articles where HN comments reveal serious issues
