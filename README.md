# 🧠 Mini GPT-2 Transformer from Scratch

This repository contains a PyTorch implementation of a GPT-2-style Transformer model, built from scratch by following the core ideas from the "Attention is All You Need" paper. The model supports training on custom datasets with adjustable configurations for both CPU and GPU environments.

---

## 🚀 Features

- Transformer architecture based on GPT-2
- Causal (autoregressive) self-attention
- Configurable number of layers, heads, embedding size
- Token and positional embeddings
- Supports CPU and GPU training
- Gradient accumulation (for memory efficiency on GPUs)
- Easy to extend for fine-tuning or custom datasets

---

## 🧪 CPU Training Configuration

| Hyperparameter       | Value    |
|----------------------|----------|
| `batch_size`         | 12       |
| `block_size`         | 64       |
| `n_embd`             | 128      |
| `n_head`             | 4        |
| `n_layer`            | 4        |
| `dropout`            | 0.0      |
| `learning_rate`      | 3e-4     |
| `max_iterations`     | 4000     |
| **Total Parameters** | ~0.8M    |
| **Runtime**          | ~14 min on CPU |

---

## ⚡ GPU Training Configuration (e.g. A100, RTX 3090)

| Hyperparameter       | Value    |
|----------------------|----------|
| `batch_size`         | 12       |
| `block_size`         | 1024     |
| `n_embd`             | 768      |
| `n_head`             | 12       |
| `n_layer`            | 12       |
| `learning_rate`      | 6e-4     |
| `max_iterations`     | 600000   |
| **Total Parameters** | ~124M    |
| **Expected Quality** | GPT-2 Small level |

---

## 🏗️ Model Architecture

- **Embedding Layer**: Token + Positional embeddings
- **Stacked Transformer Blocks** (n_layer):
  - LayerNorm
  - Multi-Head Self Attention
  - FeedForward MLP
  - Residual Connections
- **Final LayerNorm**
- **Output Projection**: tied with token embedding (optional)

---

## 📂 Project Structure

```plaintext
📦gpt2-transformer
 ┣ 📜model.py         # GPT-2 model definition
 ┣ 📜train.py         # Training script
 ┣ 📜config.py        # Hyperparameters and configuration
 ┣ 📜utils.py         # Tokenization and helper utilities
 ┣ 📜README.md        # Project documentation
 ┣ 📜requirements.txt # Dependencies
 ┗ 📂data             # Training text files go here
    ┗ 📄input.txt     # Example dataset
```

