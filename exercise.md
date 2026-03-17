# Exercise: Analyze Volvo's Q4 2025 Report Using Gemini CLI
**Duration:** 10–15 minutes
**Difficulty:** No coding required

---

## The big idea

You are going to direct an AI agent to read a real financial report and produce an executive brief — entirely steered by the instructions *you* write.

You won't touch the PDF. You won't write code. Your only job is to give the agent enough context to do the work well.

This is the core lesson of **Harness Engineering**: the agent's output is only as good as the context you give it. The files in this folder are that context.

---

## What's in this folder

| File | What it is |
|---|---|
| `GEMINI.md` | The agent's project map — already filled in for you. It tells Gemini what this project is, what the source document contains, and the rules for all outputs. **Do not edit this.** |
| `SKILLS.md` | Your personal analytical skill — a template **you fill in**. This is where you tell Gemini *how* to analyze the report for you specifically. |
| `volvo-group-q4-2025-eng.pdf` | The source document. Gemini will read this directly. |

---

## Step 1 — Set up (2 min)

Open your terminal and navigate into this folder:

```bash
cd Harness-Engineering-Exercise
```

Check that the PDF is present:

```bash
ls
```

You should see `GEMINI.md`, `SKILLS.md`, and `volvo-group-q4-2025-eng.pdf`.

Launch Gemini CLI:

```bash
gemini
```

Gemini will automatically read `GEMINI.md` when it starts. It now knows what this project is.

---

## Step 2 — Fill in your SKILLS.md (4 min)

Open `SKILLS.md` in any text editor. Read through it and fill in each section.

There are no wrong answers. Write what is true for you:
- What angle are you coming from?
- What sections do you want in the brief?
- What specific thing are you curious about?

**The more specific you are, the better the output.**

If you're stuck, here are two example approaches:

> *"I care about the big picture — just give me the 5 most important things to know about this quarter, and tell me if Volvo is in a good or bad position heading into 2026."*

> *"I want to understand segment performance. Break down each business unit, compare their margins, and tell me which one is punching above its weight."*

Save the file when you're done.

---

## Step 3 — Run the analysis (3 min)

Back in your Gemini CLI session, type this prompt:

```
Read the SKILLS.md file in this folder. Then read volvo-group-q4-2025-eng.pdf
and produce the executive brief exactly as I have specified in my skill file.
Save the output as executive-brief.md
```

Watch what Gemini does. It will:
1. Read your SKILLS.md
2. Parse the PDF
3. Generate the brief according to your instructions
4. Save it to a file

---

## Step 4 — Review and steer (3 min)

Open `executive-brief.md` and read it.

Something will not be quite right. That's intentional. Now ask yourself:

> *"What is missing or off? Is it a prompt problem — or a context problem?"*

**If it's a context problem** (the agent didn't understand your intent): go back to `SKILLS.md`, add or refine one rule, and re-run.

**If it's a prompt problem** (you didn't ask clearly enough): refine your prompt in Gemini and try again.

This loop — run, review, refine context, re-run — is the harness engineering feedback loop.

---

## Step 5 — Debrief (2 min)

When you're done, reflect on these questions:

1. What did filling in `SKILLS.md` force you to think about that you wouldn't have otherwise?
2. What one line in your skill file had the biggest impact on the output?
3. If you had another 10 minutes, what would you add to `SKILLS.md`?

---

## Bonus challenge

If you finish early, try one of these:

**Challenge A:** Add this line to your SKILLS.md:
> *"End every section with a one-sentence 'so what' that would resonate with a Volvo team member."*
Then re-run and see how the tone changes.

**Challenge B:** Ask Gemini directly in the chat:
> *"Which segment had the most surprising performance this quarter and why?"*
See if the answer matches what's in your brief — or reveals something new.

**Challenge C:** Ask Gemini to turn the brief into a 5-slide structure:
> *"Based on executive-brief.md, suggest a 5-slide deck structure with a title and 3 bullet points per slide."*

---

## What you just demonstrated

By completing this exercise, you experienced three of the core principles from the OpenAI Harness Engineering article:

| Principle | Where you felt it |
|---|---|
| **Context is everything** | GEMINI.md gave Gemini its world. Without it, the output would have been generic. |
| **Humans specify intent, agents execute** | You didn't touch the PDF. You described what you wanted and Gemini did the work. |
| **Fix the context, not just the prompt** | When the output was off, the right move was to improve SKILLS.md — not just rephrase the ask. |

---

*Built for the Harness Engineering session. PDF source: Volvo Group Q4 and Full Year 2025 Report, published January 28, 2026.*
