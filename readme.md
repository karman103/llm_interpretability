# Quantifying LLM Beliefs with  Statistics

This notebook demonstrates how **Statistics** can be used to extract **quantitative answers** from the **qualitative outputs** of large language models (LLMs).

I used alpaca api to get historiocal data and bencmarked ARIMA and LLMP for 6 months daily data whole preicting the next 5 days.

Inspired by the NeurIPS 2024 paper [_LLM Processes: Numerical Predictive Distributions Conditioned on Natural Language_](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5ec22711f3a4a2f4a0a8ffd92167190-Paper-Conference.pdf), this project explores how we can formalize and analyze the implicit uncertainty and beliefs encoded in LLM predictions.

By conditioning LLMs on contextual text and using Bayesian inference, we can model a predictive distribution over numeric targets — effectively bridging the gap between free-form natural language and structured statistical modeling.


## Acknowledgments

This work is inspired by:
- [LLM Processes: Numerical Predictive Distributions Conditioned on Natural Language](https://proceedings.neurips.cc/paper_files/paper/2024/file/c5ec22711f3a4a2f4a0a8ffd92167190-Paper-Conference.pdf)  
  _James Requeima, John Bronskill, Dami Choi, Richard E. Turner, David Duvenaud_

## Note

This is simple prelimary work that I spent a single evening on, so it needs some polishing (like accounting for stock splits)

