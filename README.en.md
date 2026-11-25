<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
    <img src="assets/banner-light.svg" alt="ViWrite — AI viết. Con người hiểu." width="840">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/tronghongnguyen1012/vietnamese-human-readable-writing/releases/tag/v4.1.0-beta"><img src="https://img.shields.io/badge/release-v4.1.0--beta-0F766E?style=flat-square" alt="Release v4.1.0-beta"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/spec-agentskills.io-1E293B?style=flat-square" alt="Agent Skills Spec"></a>
  <a href="https://skills.sh"><img src="https://img.shields.io/badge/CLI-skills.sh-0D9488?style=flat-square" alt="skills.sh"></a>
  <img src="https://img.shields.io/badge/SKILL.md-82%20lines-334155?style=flat-square" alt="82 lines">
  <a href="./docs/compatibility-and-smoke-test.md#4-%C4%91%E1%BB%81-xu%E1%BA%A5t-gi%E1%BA%A5y-ph%C3%A9p-m%C3%A3-ngu%E1%BB%93n-m%E1%BB%9F-license-proposal"><img src="https://img.shields.io/badge/license-pending%20selection-64748B?style=flat-square" alt="License Pending"></a>
</p>

<p align="center">
  <a href="./README.md">Tiếng Việt</a> · <strong>English</strong> · <a href="./INSTALL.md">Installation Guide</a> · <a href="./examples/README.md">Real Examples</a>
</p>

---

**ViWrite** *(proposed brand display name for package `vietnamese-human-readable-writing`)* is an [`agentskills.io`](https://agentskills.io) skill that helps AI coding agents communicate in **clear, structured, natural Vietnamese** without distorting logic or inventing missing facts.

## Quick Start

Install in one command via [Skills CLI (`skills.sh`)](https://skills.sh) (requires Node.js ≥ 22.20):

```bash
npx skills add tronghongnguyen1012/vietnamese-human-readable-writing
```

On **Windows PowerShell**, if `npx.ps1` is blocked by execution policy, use `npx.cmd` with `--copy`:

```powershell
npx.cmd --yes skills add tronghongnguyen1012/vietnamese-human-readable-writing -g --copy
```

See **[INSTALL.md](./INSTALL.md)** for per-agent targeting (`-a antigravity`, `claude-code`, `codex`, `cursor`), updates, removal, and manual copy instructions without Node.js.

---

## Why This Skill Exists

Standard LLMs write grammatically valid Vietnamese that engineers and PMs still struggle to act on because of:
1. **Translationese & Nominalization:** Heavy English syntax (*"cung cấp năng lực xử lý việc..."*, unnatural passive voice), burying who does what to whom.
2. **Compressing Technical Depth:** Summarizing multi-axis architecture comparisons in ways that break storage or ordering guarantees.
3. **False Clarity on Incomplete Sources:** When specs omit actors, protocols, or thresholds, default LLMs and simple prompts invent plausible-sounding systems or payloads as if settled.

### How It Differs from a Standard Vietnamese Humanizer
Instead of rewriting prose just to sound smooth or bypass AI detectors, **ViWrite** separates **Case A** (unclear prose with complete facts → clarify cleanly without adding facts) from **Case B** (incomplete or contradictory source → preserve uncertainty, surface exact open questions, and maintain confirmation status consistently across prose, tables, Mermaid diagrams, Business Rules, and API contracts).

---

## Real Output Highlights & Examples

<p align="center">
  <img src="assets/before-after.svg" alt="Before and After — Real Case H2-07" width="840">
</p>

Browse verbatim saved benchmark examples in **[examples/](./examples/README.md)**:
- [Natural Conversation](./examples/01-natural-conversation.md) (`H2-14`: 56-word witty reply, `refs = []`, zero lecturing)
- [Workplace Communication](./examples/02-workplace-communication.md) (`TEST-10`: BLUF Teams scope change, 152w → 100w)
- [Ambiguous Business Rules](./examples/03-business-rule-and-prd.md) (`H2-12`: scoped conditional options without guessing)
- [Technical RFC & Hybrid SAD](./examples/04-technical-and-sad.md) (`H2-06` verified PostgreSQL lock modes, `H2-19` Mermaid `[Chưa chốt]` parity)
- [Ambiguous Source / Anti-False-Clarity](./examples/05-ambiguous-source-case-b.md) (`H2-07`)

---

## Supported Agents & Compatibility Status

> Full 4-tier breakdown (*Spec Compliance → Install Tested → Discovery Verified → Activation Verified*) and live Windows CLI logs are in **[docs/compatibility-and-smoke-test.md](./docs/compatibility-and-smoke-test.md)**. This skill is **not yet listed** on any official curated marketplace.

- **Antigravity IDE / CLI:** Spec compliant (`.antigravity-plugin/plugin.json`), Windows CLI install + discovery verified, runtime generation evaluated on `flash` / `pro`.
- **Claude Code / Desktop, OpenAI Codex (CLI / App / IDE), Cursor:** Format-compliant plugin & repository manifests included (`.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/marketplace.json`, `.cursor-plugin/`) without hooks or MCP servers; file placement tested on Windows via `skills.sh --copy`; live activation inside those runtimes/models is **not yet tested**.

---

## Evaluation Highlights & Honest Limitations

<p align="center">
  <img src="assets/benchmark-chart.svg" alt="Verified Benchmark Highlights" width="840">
</p>

- On `held-out-v2.jsonl` (`n = 24`, LLM Blind Judge `pro` with 2 swapped passes, generator `flash`), `Skill v4` won **`20/24 (83.3%)`** vs a Neutral baseline (`0/24` vs `8/24` Hard Fails) and **`17/24 (70.8%)`** vs a 6-rule Simple Prompt (`1/24` vs `8/24` Hard Fails).
- On a focused **9-case targeted regression** (`v4.1 vs v4`, known cases), **`v4.1.0-beta` achieved `0/9` Hard Fails** in both standalone Gate 0 audits and blind A/B comparisons, resolving `H2-06` (PostgreSQL lock mode) and `H2-19` (confirmation-status mismatch).
- **Not Yet Proven:** Real Vietnamese human reader **Time to Correct Understanding (TtCU)** has not been executed yet ([human-eval-protocol.md](./evaluation/human-eval-protocol.md)); multi-section long docs in `held-out-v2.jsonl` are simulated cases; cross-model performance outside Antigravity `flash`/`pro` is untested.
- **License Status:** No `LICENSE` file is currently committed. See the MIT vs Apache-2.0 recommendation in [docs/compatibility-and-smoke-test.md](./docs/compatibility-and-smoke-test.md).
