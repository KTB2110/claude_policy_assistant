# Anthropic Applied AI Study Tracker

## Goal
Be ready for an Anthropic Applied AI Associate interview around March 2027 by building and explaining a functioning Claude application and evaluating it rigorously.

## Operating rules
1. Study for understanding before asking an AI to implement a feature.
2. Write the initial solution personally. Ask AI for hints and conceptual explanations first.
3. Use Codex to review, test, challenge and debug code. Ask for full implementations only after making an independent attempt or when studying a reference implementation.
4. Every study session must produce evidence: a commit, test, experiment, note, or a clearly documented blocker.
5. Record actual performance measurements. Never invent accuracy, latency or cost numbers.
6. Keep customer data, employer data and API keys out of public repositories.

## Ten week roadmap
| Week | Focus | Status | Evidence |
| :--- | :--- | :--- | :--- |
| 1 | Claude API and SDK fundamentals | In progress: Day 1 completed, automated tests pending | Reusable Claude Python client; successful API calls; error and input validation exercises; GitHub push reported (URL and commit hash not verified) |
| 2 | Tool calling and structured outputs | Not started | |
| 3 | Context engineering and caching | Not started | |
| 4 | Hybrid retrieval and RAG evaluation | Not started | |
| 5 | Agent design and Claude Agent SDK | Not started | |
| 6 | MCP and Claude Skills | Not started | |
| 7 | Systematic agent evaluations | Not started | |
| 8 | Reliability, security and approvals | Not started | |
| 9 | Production optimization and deployment | Not started | |
| 10 | Capstone demonstration and interview simulation | Not started | |

## Day 1: October 29, 2026
Status: Completed as a guided learning session; formal automated test coverage remains pending.
Goal: Understand the basic Claude Messages API and send a first request yourself.

1. Set up a new Git repository for the Claude enterprise policy assistant.
2. Review the introduction to Claude Academy and the relevant sections of Claude Platform 101.
3. Create a Python environment and install the Anthropic SDK following the current official docs.
4. Read an API key from an environment variable. Do not commit the key.
5. Write a short Python program that sends a user message to Claude and prints the response.
6. Display input and output token usage and capture elapsed time.
7. Write three small tests: ordinary answer, unknown fact requiring abstention, and an API failure case.
8. Commit the code and record one thing learned and one open question.

Definition of done: I can explain the request parameters, response structure and token usage without consulting the tutorial.

## Day 1 completed study log: October 29, 2026

| Field | Entry |
| :--- | :--- |
| Date | October 29, 2026 |
| Topic | Week 1: Claude Messages API and Python SDK foundations |
| Minutes studied | Not recorded; do not infer from chat timestamps |
| Concepts explained in my own words | Stateless Messages API and explicit conversation history; environment variable authentication; virtual environment isolation; token ceilings versus actual usage; exception propagation and `finally`; retrieval versus generation failure; deterministic eligibility rules |
| Code or experiment completed | Created `first_message.py` and reusable `policy_assistant.py` with `ask_claude(question: str) -> dict`; configured `.env` with `load_dotenv()` and reusable `Anthropic()` client; added plain text extraction, response metadata, latency measurement, empty input validation, and Anthropic API exception handlers |
| Git commit or artifact | User reported creating a GitHub repository and completing the Git commit/push steps. Repository URL, commit hash, and remote contents not independently verified. |
| Tests passed / failed | Successful live Claude API call and text response observed; empty whitespace input raised `ValueError`; invalid model raised HTTP 404 `NotFoundError` in earlier exercise. No automated pytest suite demonstrated; no unknown fact/abstention test demonstrated. Isolated empty input run not independently verified because pasted output included a preceding latency line. |
| Measured API run | Model `claude-haiku-4-5-20251001`; input 40 tokens; output 145 tokens; `stop_reason=end_turn`; request latency approximately 2.468641 seconds. Earlier run: 40 input, 128 output, approximately 2.016 seconds. |
| What surprised me | `finally` executes before a return or exception propagates, but only for code that enters its corresponding `try`; `max_tokens` is a ceiling, not an output target; `msg.content` is a list of content blocks |
| What remains confusing / needs practice | Reliable retry policies for 429/5xx; model evaluation against verified expected answers; exact boundaries of retrieval and deterministic rules; test isolation and pytest mocks; policy versioning and authorization |
| Next concrete action | Create a pytest suite with mocked success, empty input, and Anthropic API failure scenarios; verify no real API calls occur in tests. Run tests, capture results, and commit test additions. |
| Mastery assessment | Level 3 of 5 overall for Messages API and Python SDK (implements with guidance); Level 2 for production retries and evaluation design |

**Day 1 interview check:** Completed five conceptual questions. Needed correction on rate limit retries and evaluation methodology. Demonstrated good reasoning about RAG retrieval failures, deterministic scholarship eligibility, policy effective dates, and manual approval for conflicting rules. This is not evidence of production implementation of those ideas.

**Week 1 remaining:** Build policy document input, structured answer, FastAPI endpoint, reproducible automated tests, and initial evaluation dataset as the syllabus progresses. Confirm GitHub repository URL/commit when available.

## Daily study log template
Date:
Topic:
Minutes studied:
Concept explained in my own words:
Code or experiment completed:
Git commit or artifact:
Tests passed / failed:
What surprised me:
What I still cannot explain:
Next concrete action:

## Weekly review template
Week:
Study hours completed / planned:
Learning objectives completed:
Evidence links:
Benchmark results:
Largest failure or misconception:
One concept I can teach clearly:
One concept I still cannot teach:
Next week's priority:
Self assessment from 1 to 5:

## Project scorecard
Track retrieval correctness, answer correctness, tool selection and arguments, task completion, grounding and citations, unauthorized actions blocked, latency, cost per task and repeatability when applicable.

## Official starting points
Claude Academy: https://academy.claude.com/collections/build-with-claude
Claude Platform 101: https://academy.claude.com/courses/claude-platform-101
Building with the Claude API: https://academy.claude.com/courses/building-with-the-claude-api
Claude API docs: https://platform.claude.com/docs/en/home
Claude Agent SDK: https://code.claude.com/docs/en/agent-sdk/overview
Effective context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Evaluating agents: https://www.anthropic.com/research/demystifying-evals-for-ai-agents
