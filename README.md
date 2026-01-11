# Complete AI & LLM Engineering Bootcamp

Welcome to the **Complete AI & LLM Engineering Bootcamp** – your one-stop course to learn Python, Git, Docker, Pydantic, LLMs, Agents, RAG, LangChain, LangGraph, and Multi-Modal AI from the ground up.

This is not just another theory course. By the end, you will be able to code, deploy, and scale real-world AI applications that use the same techniques powering ChatGPT, Gemini, and Claude.

---

## 🎯 What You'll Learn

### 📚 Foundations

- **Python programming** from scratch — syntax, data types, OOP, and advanced features
- **Git & GitHub** essentials — branching, merging, collaboration, and professional workflows
- **Docker** — containerization, images, volumes, and deploying applications like a pro
- **Pydantic** — type-safe, structured data handling for modern Python apps

### 🤖 AI Fundamentals

- What are LLMs and how GPT works under the hood
- Tokenization, embeddings, attention, and transformers explained simply
- Understanding multi-head attention, positional encodings, and the "Attention is All You Need" paper

### 💡 Prompt Engineering

- Master prompting strategies: zero-shot, one-shot, few-shot, chain-of-thought, persona-based prompts
- Using Alpaca, ChatML, and LLaMA-2 formats
- Designing prompts for structured outputs with Pydantic

### 🚀 Running & Using LLMs

- Setting up OpenAI & Gemini APIs with Python
- Running models locally with Ollama + Docker
- Using Hugging Face models and INSTRUCT-tuned models
- Connecting LLMs to FastAPI endpoints

### 🤖 Agents & RAG Systems

- Build your first AI Agent from scratch
- CLI-based coding agents with Claude
- The complete RAG pipeline — indexing, retrieval, and answering
- LangChain: document loaders, splitters, retrievers, and vector stores
- Advanced RAG with Redis/Valkey Queues for async processing
- Scaling RAG with workers and FastAPI

### 🧠 LangGraph & Memory

- Introduction to LangGraph — state, nodes, edges, and graph-based AI
- Adding checkpointing with MongoDB
- Memory systems: short-term, long-term, episodic, semantic memory
- Implementing memory layers with Mem0 and Vector DB
- Graph memory with Neo4j and Cypher queries

### 🎙️ Conversational & Multi-Modal AI

- Build voice-based conversational agents
- Integrate speech-to-text (STT) and text-to-speech (TTS)
- Code your own AI voice assistant for coding (Cursor IDE clone)
- Multi-modal LLMs: process images and text together

### 🔌 Model Context Protocol (MCP)

- What is MCP and why it matters for AI apps
- MCP transports: STDIO and SSE
- Coding an MCP server with Python

---

## 🛠️ Real-World Projects You'll Build

1. **Tokenizer from scratch**
2. **Local Ollama + FastAPI AI app**
3. **Python CLI-based coding assistant**
4. **Document RAG pipeline with LangChain & Vector DB**
5. **Queue-based scalable RAG system with Redis & FastAPI**
6. **AI conversational voice agent (STT + GPT + TTS)**
7. **Graph memory agent with Neo4j**
8. **MCP-powered AI server**

---

## 📂 Repository Structure

```
fullstack-generative-and-agentic-ai/
├── 02_datatypes/           # Python data types and fundamentals
│   ├── chapter_1.py        # Objects, mutability, and immutability
│   ├── chapter_2.py        # Mutable data types (sets)
│   ├── chapter_3.py        # Integers and arithmetic operations
│   ├── chapter_4.py        # Booleans and logical operations
│   ├── chapter_5.py        # Real numbers and floating point
│   ├── chapter_6.py        # Strings - indexing, slicing, encoding
│   ├── chapter_7.py        # Tuples - immutable collections
│   └── theory_notes.md     # Complete theory notes for interviews
├── python/                 # Python programming exercises
└── README.md              # This file
```

---

## 📝 Quick Interview Notes - Python Tuples

### 🔒 **TUPLES** (Immutable Collections)

**Key Concepts:**
- **Immutable** ordered collection (cannot be changed)
- Defined with **parentheses**: `(item1, item2, item3)`
- Faster and more memory-efficient than lists
- Can be used as dictionary keys (hashable)

**Creating Tuples:**
```python
# With parentheses
spices = ("cardamom", "clove", "cinnamon")

# Without parentheses (tuple packing)
spices = "cardamom", "clove", "cinnamon"

# Single element - need comma!
single = ("item",)  # ✅ Tuple
not_tuple = ("item")  # ❌ String!
```

**Tuple Unpacking:**
```python
spices = ("cardamom", "clove", "cinnamon")
spice1, spice2, spice3 = spices

# Advanced unpacking
first, *rest = spices
first, *middle, last = spices
```

**Variable Swapping (Python Magic!):**
```python
a, b = 5, 10
a, b = b, a  # Swap! Now a=10, b=5
# Works because: (a, b) = (b, a)
```

**Membership Testing:**
```python
spices = ("cardamom", "clove", "cinnamon")
"clove" in spices     # True
"pepper" in spices    # False
"Clove" in spices     # False (case-sensitive!)
```

**Tuple Methods (Only 2!):**
```python
numbers = (1, 2, 3, 2, 4, 2)
numbers.count(2)    # 3
numbers.index(2)    # 1 (first occurrence)
```

**Tuple vs List:**
| Feature | Tuple | List |
|---------|-------|------|
| Mutable | ❌ No | ✅ Yes |
| Speed | ⚡ Faster | 🐌 Slower |
| Memory | 💾 Less | 💾 More |
| Syntax | `()` | `[]` |
| Dict Key | ✅ Yes | ❌ No |

**When to Use Tuples:**
1. Data shouldn't change (coordinates, RGB colors, config)
2. Need better performance
3. Using as dictionary keys
4. Returning multiple values from functions

**Interview Q&A:**
- Q: Difference between tuple and list?
- A: Tuples are immutable, faster, use less memory. Lists are mutable, flexible.

- Q: How to swap variables in Python?
- A: `a, b = b, a` (uses tuple unpacking behind the scenes)

- Q: Can tuples be dictionary keys?
- A: Yes! Tuples are hashable (immutable). Lists cannot be keys.

---

## 📝 Quick Interview Notes - Python Strings

### 📝 **STRINGS** (Immutable Text)

**Key Concepts:**
- **Immutable** - Cannot be changed in place (creates new object)
- Defined with quotes: `"text"` or `'text'`
- Each character has an index (starts at 0)

**Indexing (Single Character):**
```python
text = "Python"
# Positive: 0  1  2  3  4  5
# Negative:-6 -5 -4 -3 -2 -1

text[0]    # 'P' (first)
text[-1]   # 'n' (last)
text[5]    # 'n'
```

**Slicing Syntax: `string[start:end:step]`**
- `start` - Starting position (inclusive)
- `end` - Ending position (EXCLUSIVE - not included!)
- `step` - How many to skip (default: 1)

**Common Slicing Patterns:**
```python
text = "Aromatic and bold"

text[:8]       # "Aromatic" (start to position 7)
text[12:]      # "bold" (position 12 to end)
text[0:8:2]    # "Aoai" (every 2nd character)
text[::-1]     # "dlob dna citamorA" (reverse!)
text[-4:]      # "bold" (last 4 characters)
```

**Encoding/Decoding (Special Characters):**
```python
text = "Café"
encoded = text.encode('utf-8')    # Convert to bytes
decoded = encoded.decode('utf-8')  # Back to string
```

**Interview Q&A:**
- Q: How to reverse a string?
- A: `text[::-1]` (step of -1 reverses)

- Q: Are strings mutable?
- A: No, they're immutable. Modifications create new objects.

- Q: What does `text[2:5]` return?
- A: Characters at positions 2, 3, 4 (position 5 NOT included)

---

## 📝 Quick Interview Notes - Python Numbers

### 1️⃣ **INTEGERS** (Whole Numbers)

**Key Operations:**
- `+` Addition, `-` Subtraction, `*` Multiplication
- `/` True Division (always returns float: `7/4 = 1.75`)
- `//` Floor Division (removes decimal: `7//4 = 1`)
- `%` Modulo (remainder: `10%3 = 1`)
- `**` Exponentiation (power: `2**3 = 8`)
- Use `_` for readability: `1_000_000` (Python ignores it)

**Interview Q&A:**
- Q: What's difference between `/` and `//`?
- A: `/` gives decimal result, `//` gives whole number (floor division)

---

### 2️⃣ **BOOLEANS** (True/False)

**Key Concepts:**
- Only two values: `True` and `False` (capital first letter)
- `True = 1`, `False = 0` (upcasting)
- **Falsy values:** `0`, `None`, `""`, `[]`, `{}`, `False`
- Everything else is **Truthy**

**Logical Operators:**
- `and` - Both must be True
- `or` - At least one must be True  
- `not` - Reverses the value

**Interview Examples:**
```python
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("Hi")     # True
bool(None)     # False

# Logical operations
True and False  # False
True or False   # True
not True        # False
```

---

### 3️⃣ **FLOATS** (Decimal Numbers)

**Key Concepts:**
- Real numbers with decimal precision
- Precision issues due to binary representation
- Use `Decimal` for financial calculations
- Use `Fraction` for exact rational numbers

**Interview Q&A:**
- Q: Why `0.1 + 0.2 != 0.3` in Python?
- A: Binary representation of decimals isn't exact. Use `Decimal` for precision.

**Best Practices:**
```python
# For money/finance
from decimal import Decimal
price = Decimal("19.99")

# For exact fractions
from fractions import Fraction
half = Fraction(1, 2)

# Check system limits
import sys
sys.float_info  # Max/min float values
```

---

### 4️⃣ **COMPLEX NUMBERS** (Rarely Used)

- Format: `2 + 3j` (where j = √-1)
- Used in scientific computing
- Python has built-in support

---

## 🎯 Common Interview Questions

**Q1: What are all numeric types in Python?**  
A: `int`, `float`, `complex`, `bool` (technically numeric)

**Q2: What's the difference between `is` and `==`?**  
A: `==` checks value equality, `is` checks identity (same object in memory)

**Q3: What's upcasting in Python?**  
A: Automatic type conversion (e.g., `True` → `1` when used in arithmetic)

**Q4: How to check if a variable is a number?**  
A: `isinstance(x, (int, float))` or `type(x) in (int, float)`

**Q5: What's the difference between `/` and `//`?**  
A: `/` is true division (returns float), `//` is floor division (returns int)

---

## 💡 Pro Tips for Interviews

1. **Integers are immutable** - operations create new objects
2. **Use `_` for readability** in large numbers: `1_000_000`
3. **Floor division `//`** is faster than `int(a/b)`
4. **Modulo `%`** is perfect for checking even/odd: `n % 2 == 0`
5. **Boolean short-circuit evaluation** - `and`/`or` stop early

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Git
- Docker (optional but recommended)
- VS Code or any code editor

### Installation

```bash
# Clone the repository
git clone https://github.com/raavikant27/Full-stack-Generative-And-AgenticAI-With-Python.git

# Navigate to the project directory
cd Full-stack-Generative-And-AgenticAI-With-Python

# Install dependencies (when available)
pip install -r requirements.txt
```

---

## 📖 Course Progress

- [x] Python Fundamentals
- [x] Data Types & Objects
- [ ] Git & GitHub
- [ ] Docker Fundamentals
- [ ] Pydantic
- [ ] LLMs & GPT Basics
- [ ] Prompt Engineering
- [ ] AI Agents
- [ ] RAG Systems
- [ ] LangChain
- [ ] LangGraph
- [ ] Multi-Modal AI
- [ ] Model Context Protocol

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/raavikant27/Full-stack-Generative-And-AgenticAI-With-Python/issues).

---

## 📝 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Raavikant**
- GitHub: [@raavikant27](https://github.com/raavikant27)

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

*Last Updated: January 2026*
