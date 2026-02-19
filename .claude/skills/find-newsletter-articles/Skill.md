
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

Save this into a files titled `summary.txt` within the `research` folder. Replacing if it already exists.

## Step 2: Fetch and Analyze Hacker News

Fetch articles from:
1. Hacker News front page (page 1)
2. Next 3 pages (pages 2-4)

For each page, use the WebFetch tool to retrieve the content. Hacker News URLs follow this pattern:
- Front page: `https://news.ycombinator.com/`
- Page 2: `https://news.ycombinator.com/news?p=2`
- Page 3: `https://news.ycombinator.com/news?p=3`
- Page 4: `https://news.ycombinator.com/news?p=4`

Extract article titles, URLs, and any available metadata (points, comments, domains).

## Step 3: Match and Rank Articles

For each article, evaluate its fit based on:

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

## Step 4: Save Recommendations

Save your findings into the `research` folder, in a markdown file with todays date.

### Recommended Articles

For each recommended article (aim for 10 recommendations), provide:

**[Article Title]**
- URL: [full URL]
- Domain: [source domain]
- Relevance Score: [0-10]
- Category: [e.g., "Agentic Coding", "Model Release", "Critical Analysis", "Developer Experience"]
- summary: a brief bullet point summary of the article itself (visit the article to produce this)
- HN Stats: [points and comment count if available]
- HN Sentiment: View the HN comments page and summarise the sentiment towards this post.

Sort recommendations by relevance score (highest first).

---

## Execution Notes

- Use TodoWrite to track your progress through the steps
- Read all 5 recent posts in parallel for efficiency
- Fetch all 4 HN pages in parallel
- Be critical in your evaluation - quality over quantity
- Consider the editorial voice: the newsletter values balanced perspectives and critical thinking over pure hype
