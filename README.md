# dspy-community

The DSPy community meta-package — install [DSPy](https://github.com/stanfordnlp/dspy) and curated community libraries in one go.

## Install

```bash
# Just DSPy
pip install dspy-community

# DSPy + all community libraries
pip install dspy-community[all]

# Pick what you need
pip install dspy-community[session,template-adapter]
```

## Included Libraries

| Extra | Package | Description |
|---|---|---|
| `session` | [dspy-session](https://github.com/MaximeRivest/dspy-session) | Multi-turn session wrapper — turn any module into a stateful conversation with optimizer-ready linearization |
| `template-adapter` | [dspy-template-adapter](https://github.com/MaximeRivest/dspy-template-adapter) | Exact-fidelity prompt templates with full control over messages |
| `profiles` | [dspy-profiles](https://github.com/nielsgl/dspy-profiles) | Configuration profiles via TOML files — switch between models, retrieval settings, and environments |

> **Coming soon:** [dspy-spotlighting](https://github.com/estsauver/dspy-spotlight) — production-ready defense against indirect prompt injection attacks.

## DSPy Ports in Other Languages

DSPy isn't just Python. The community has built ports for other languages:

| Language | Project | Description |
|---|---|---|
| 💎 Ruby | [DSPy.rb](https://github.com/vicentereig/dspy.rb) | Faithful port with Sorbet type-safety. By Vicente Reig Rincon de Arellano. |
| 🦀 Rust | [DSRs](https://dsrs.herumbshandilya.com) | Full rewrite with Rust-native design. COPRO, MIPROv2, GEPA optimizers. |
| 🐹 Go | [dspy-go](https://github.com/XiaoConstantine/dspy-go) | Full port with CLI tool, interceptors, multimodal, A2A protocol. |

## Contributing

We welcome new libraries and projects to the DSPy community! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to submit yours.

## License

MIT
