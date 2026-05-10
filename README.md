# Jewellery Chatbot using Flowise

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) based Jewellery Chatbot using Flowise 3.1.2. The chatbot answers customer questions using information retrieved from the provided jewellery catalogue (`Jewellery Details.pdf`).

The chatbot supports:

* Catalogue-based question answering
* Conversational memory
* Retrieval-based grounded responses
* Out-of-stock alternative recommendations
* Lightweight web chatbot interface
* Flowise API integration

---

# Objectives

The solution was designed to:

* Answer jewellery-related customer questions accurately
* Retrieve responses from uploaded PDF catalogue data
* Maintain short-term conversational memory
* Suggest relevant alternatives for unavailable items
* Provide a lightweight customer-facing chatbot UI

---

# Technology Stack

| Component              | Technology             |
| ---------------------- | ---------------------- |
| Workflow Orchestration | Flowise 3.1.2          |
| LLM Provider           | OpenAI GPT-4o-mini     |
| Embeddings             | OpenAI Embeddings      |
| Vector Database        | In-Memory Vector Store |
| Backend API            | Flask                  |
| Frontend               | HTML, CSS, JavaScript  |
| Communication          | REST API               |

---

# Flowise Architecture

The chatbot uses a Retrieval-Augmented Generation (RAG) architecture.

## Flowise Components Used

| Node                              | Purpose                          |
| --------------------------------- | -------------------------------- |
| Recursive Character Text Splitter | Splits PDF into chunks           |
| PDF File Loader                   | Reads jewellery catalogue        |
| OpenAI Embedding                  | Generates vector embeddings      |
| In-Memory Vector Store            | Stores embeddings for retrieval  |
| Vector Store Retriever            | Retrieves relevant chunks        |
| Conversational Retrieval QA Chain | Handles RAG conversation flow    |
| Buffer Memory                     | Maintains conversational context |
| OpenAI                            | Generates final responses        |

---

# Architecture Diagram

```text
                        User
                          │
                          ▼
               Web Chatbot Interface
               (HTML/CSS/JavaScript)
                          │
                          ▼
                    Flask Backend
                          │
                          ▼
                 Flowise Prediction API
                          │
                          ▼
        ┌─────────────────────────────────┐
        │     Conversational QA Chain     │
        └─────────────────────────────────┘
                    ▲              ▲
                    │              │
             Buffer Memory      OpenAI LLM
                    ▲
                    │
          Vector Store Retriever
                    ▲
                    │
          In-Memory Vector Store
               ▲             ▲
               │             │
     OpenAI Embeddings    PDF Loader
               ▲
               │
   Recursive Character Text Splitter
```

---

# Data Ingestion Workflow

The jewellery catalogue PDF is processed using the following pipeline:

```text
PDF → Text Splitter → Embeddings → Vector Store
```

## Chunking Strategy

| Parameter     | Value |
| ------------- | ----- |
| Chunk Size    | 800   |
| Chunk Overlap | 100   |

### Reasoning

* Smaller chunks improve semantic retrieval
* Overlap preserves neighbouring context
* Better retrieval of:

  * prices
  * product names
  * stock details
  * material information

---

# Prompt Design

The chatbot prompt was customised to create a jewellery assistant tone.

## Prompt Goals

* Be concise and factual
* Avoid hallucinated answers
* Use only catalogue data
* Support conversational continuity
* Recommend alternatives for unavailable items

## Response Prompt

```text
You are Ornativa’s virtual jewellery expert.

Use ONLY the provided catalogue context to answer customer questions.

Rules:
- Be polite, concise, and factual.
- Never invent products or prices.
- If an item is out of stock, suggest a similar available product from the catalogue.
- Use previous conversation context when relevant.
- If information is unavailable, say:
"I could not find that information in the catalogue."
```

---

# Conversational Memory

Conversational memory was implemented using the `Buffer Memory` node.

## Purpose

The memory component enables:

* Follow-up questions
* Context retention
* Multi-turn conversations
* Product reference continuity

## Example

### User

```text
Show me diamond rings.
```

### Bot

```text
Classic Diamond Ring is available.
```

### User

```text
What is the price of the ring?
```

The chatbot correctly understands that “ring” refers to the previously discussed product.

---

# Out-of-Stock Handling

The chatbot dynamically handles unavailable products using retrieval and prompt instructions.

## Behaviour

If a product is out of stock:

1. Inform the customer politely
2. Recommend a similar product from catalogue

## Example

### User

```text
Do you have Ruby Solitaire Ring?
```

### Bot

```text
Ruby Solitaire Ring is currently out of stock.
You may like the Classic Diamond Ring instead.
```

---

# Lightweight Web Chatbot Interface

A lightweight Flask-based chatbot interface was developed to connect users with the deployed Flowise API.

## Features

* Real-time chatbot interaction
* Clean customer-facing UI
* Flowise API integration
* Supports conversational memory
* Displays chatbot responses dynamically

---

# Folder Structure

```text
week20_flowise/
│
├── app.py
├── week 20 Chatflow.json
├── Jewellery_Chatbot_README.md
├── public/
│   └── index.html
└── venv/
```

---

# Flask Integration

The Flask backend acts as a lightweight proxy between frontend and Flowise API.

## API Endpoint

```text
https://cloud.flowiseai.com/api/v1/prediction/0dd4bc76-534b-405a-97fc-41a1ba4
```

---

# Running the Application

## Install Dependencies

```bash
pip install flask requests
```

## Run Flask Application

```bash
python app.py
```

## Open Browser

```text
http://localhost:5000
```

---

# Sample Test Queries

## Retrieval Query

```text
List all available diamond items.
```

## Price Query

```text
What is the price of the Pearl Necklace?
```

## Material Query

```text
Which products are made of 22K gold?
```

## Memory Query

```text
Show me diamond rings.
```

Followed by:

```text
What is the price of the ring?
```

## Out-of-Stock Query

```text
Do you have Ruby Solitaire Ring?
```

---

# Conclusion

The project successfully demonstrates:

* Retrieval-Augmented Generation (RAG)
* PDF document ingestion
* Semantic retrieval using vector embeddings
* Conversational memory
* Prompt engineering
* Flowise orchestration
* Lightweight chatbot integration
* Catalogue-grounded jewellery assistance

The final solution provides an efficient conversational jewellery assistant capable of answering customer questions accurately and professionally using catalogue-driven retrieval.
