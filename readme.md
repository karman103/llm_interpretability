# Quantifying LLM Beliefs with Bayesian Statistics

This notebook demonstrates how **Bayesian statistics** can be used to extract **quantitative answers** from the **qualitative outputs** of large language models (LLMs).

I used alpaca api to get historiocal data and bencmarked ARIMA and LLMP for 6 months daily data whole preicting the next 5 days

Inspired by the NeurIPS 2024 paper [_LLM Processes: Numerical Predictive Distributions Conditioned on Natural Language_](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5ec22711f3a4a2f4a0a8ffd92167190-Paper-Conference.pdf), this project explores how we can formalize and analyze the implicit uncertainty and beliefs encoded in LLM predictions.

By conditioning LLMs on contextual text and using Bayesian inference, we can model a predictive distribution over numeric targets — effectively bridging the gap between free-form natural language and structured statistical modeling.

---

> 💬 _If you're an interviewer from **PSP Investments**, please ask me about this repo — I'd be excited to walk through the ideas and code!_

---

## Acknowledgments

This work is inspired by:
- [LLM Processes: Numerical Predictive Distributions Conditioned on Natural Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5ec22711f3a4a2f4a0a8ffd92167190-Paper-Conference.pdf)  
  _James Requeima, John Bronskill, Dami Choi, Richard E. Turner, David Duvenaud_

