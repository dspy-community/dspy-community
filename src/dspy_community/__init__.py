"""
dspy-community — The DSPy community meta-package.

Install dspy and curated community libraries in one go:

    pip install dspy-community              # just dspy
    pip install dspy-community[all]         # everything
    pip install dspy-community[session]     # + dspy-session
    pip install dspy-community[attachments] # + attachments

Available extras:
    session          - Multi-turn session wrapper for DSPy programs
    template-adapter - Exact-fidelity prompt templates with full control
    profiles         - Configuration profiles via TOML files
    attachments      - Turn any file into model-ready text/images for LLMs
    all              - All of the above
"""

__version__ = "0.1.0"
