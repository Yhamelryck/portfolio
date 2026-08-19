# Yannick Hamelryck Portfolio

## Project purpose

This repository contains the production source code for:
https://yannickhamelryck.be

It is Yannick Hamelryck's personal cybersecurity and cloud security portfolio.

## Architecture

- Static website
- HTML
- CSS
- Minimal JavaScript where required
- Hosted on GitHub Pages
- DNS managed through Cloudflare
- Custom domain: yannickhamelryck.be
- Source controlled with Git and GitHub

Do not introduce React, Next.js, Vue, Angular, a database, or a backend unless explicitly requested.

## Design

The website may be redesigned substantially when this improves the overall quality.

The target style is a modern, polished technology and cybersecurity portfolio.

Design principles:

- modern and minimal
- professional rather than "hacker themed"
- strong visual hierarchy
- dark or dark-neutral base
- subtle blue, cyan, purple or gradient accents
- clean typography
- generous whitespace
- modern card and section layouts
- subtle shadows, borders and glass effects where appropriate
- smooth but restrained animations and hover interactions
- responsive mobile-first design
- accessible contrast and readable typography

The website should feel like a modern 2026 technology portfolio rather than a traditional static HTML website.

Avoid:

- excessive neon effects
- Matrix/hacker clichés
- excessive animations
- cluttered layouts
- large amounts of text without visual hierarchy
- unnecessary UI frameworks
- redesigning functionality purely for visual novelty

Prefer:

- modern hero sections
- bento/grid layouts where appropriate
- visually distinct project cards
- clear career timeline
- clean navigation
- subtle background effects
- strong typography
- consistent spacing and border radius
- tasteful micro-interactions

The website must remain lightweight and fast.

The design may change significantly, but the website should still clearly represent a Cloud Security / Cybersecurity professional.

## Code

- Keep HTML semantic.
- Keep CSS maintainable.
- Avoid unnecessary dependencies.
- Avoid duplicated CSS.
- Prefer reusable CSS classes.
- Keep the website lightweight.
- Maintain responsive behavior.
- Maintain accessibility.

## Content

The website represents Yannick professionally.

Do not invent:
- work experience
- certifications
- education
- skills
- projects
- employers
- dates

If information appears outdated or contradictory, flag it instead of guessing.

## Security

- Never commit secrets.
- Never add credentials or API keys to the repository.
- Avoid unnecessary third-party JavaScript.
- Flag external dependencies that introduce security or privacy concerns.
- Keep dependencies to a minimum.

## Workflow

Before changing code:
1. Inspect the relevant existing files.
2. Understand the current implementation.
3. Preserve existing behavior unless requested otherwise.

After changing code:
1. Review the diff.
2. Check for broken internal links.
3. Check navigation consistency.
4. Check responsive behavior.
5. Check accessibility.
6. Check for duplicated or unused CSS.

For major changes, create a plan before implementation.

## Multi-agent orchestration

The main Codex agent is the lead and orchestrator. It returns one consolidated final report; the user should not need to inspect individual subagent threads.

For meaningful website changes:

1. The main agent first understands the request and inspects the relevant repository context.
2. It spawns the relevant read-only reviewer subagents in parallel when their work is independent.
3. Normally use:
   - `content_reviewer` for professional or content changes.
   - `design_reviewer` for visual, layout, responsive, UX, or accessibility changes.
   - `security_reviewer` when HTML, JavaScript, forms, external resources, privacy, or security-relevant behavior changes.
4. Wait for the reviewers' findings before implementation.
5. The main agent resolves conflicts between recommendations and defines the approved implementation scope.
6. Delegate implementation to `site_worker`.
7. After implementation, delegate final verification to `qa_reviewer`.
8. If QA finds an actual defect, send that specific defect back to `site_worker`.
9. Run `qa_reviewer` again after fixes.
10. Finish only when QA reports no blocking findings.

Review agents should return concise findings to the main agent and must not edit website source. Only `site_worker` should normally modify website source files. `qa_reviewer` should operate read-only except for temporary local validation artifacts, which it must remove before finishing.

For tiny changes, such as correcting one typo, use judgment and do not unnecessarily spawn every reviewer. For large tasks, reviewers may work in parallel. Never allow multiple implementation agents to edit the same website files concurrently.

Do not automatically commit or push changes.
