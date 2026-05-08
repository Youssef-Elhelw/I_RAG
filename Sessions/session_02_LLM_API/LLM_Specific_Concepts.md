# **LLM-Specific Concepts**

## Outline:
### 1. [What is a `token`?](#1-what-is-a-token-1)
### 2. [What is the difference between `system`, `user`, and `assistant` roles?](#2-what-is-the-difference-between-system-user-and-assistant-roles-1)
### 3. [What does `temperature` do? What about `top_p`?](#3-what-does-temperature-do-what-about-top_p-1)
### __3.1 [Temperature](#31-temperature-controls-randomness)
### __3.2 [Top-p](#32-top-p-nucleus-sampling)
### 4. [What is `max_tokens` and how does it affect cost?](#4-what-is-max_tokens-and-how-does-it-affect-cost-1)
### 5. [What is `context window`?](#5-what-is-context-window-1)
### 6.[ What is `stop_reason` and what values can it have?](#6-what-is-stop_reason-and-what-values-can-it-have-1)

---

## 1. What is a `token`?

- LLMs don't read text word by word, they break it into smaller pieces called tokens.

- token is roughly:

    - ~1 short word → "cat" = 1 token
    - ~¾ of a long word → "unhappy" = 2 tokens ("un" + "happy")
    - A punctuation mark → "!" = 1 token
    - A space + word → " hello" = 1 token

- Example: 
    - "Hello, world!"        → 4 tokens
    - "I love programming."  → 4 tokens

- Why Does It Matter?
    - Because you pay per token — both what you send (input) and what you receive (output).

## 2. What is the difference between `system`, `user`, and `assistant` roles?

- In AI chat systems (like chatbots and APIs), messages are usually separated into roles.
- The three main roles are:
    - System Role
        - The system role gives the AI its global instructions and behavior.
        - It tells the model things like:
            - how to behave
            - what tone to use
            - rules to follow
            - limitations
            - personality
        - Example: 
            ```json
            {
            "role": "system",
            "content": "You are a rude assistant who gets irritated by dumb questions and conveys your frustration to the user."
            }

    <p style="text-align:center;">────────────</p>

    - User Role 
        - represents the human interacting with the AI model. 
        - When sending a message with the “user” role, we’re essentially simulating a user’s input in the conversation.
        - The AI model will interpret this message as coming from the user and generate a response accordingly.
        - Example:
            ```json
                {
                "role": "user",
                "content": "What is the capital of Spain?"
                }

    <p style="text-align:center;">────────────</p>
                
    - Assistant Role
        - The assistant role represents the AI model itself. 
        - When the API returns a response, it will include a message with the “assistant” role. 
        - This message contains AI-generated content that serves as the response to the user’s input.
        - Example:
            ```json
                {
                "role": "assistant",
                "content": "The capital of Spain is Madrid."
                }

---

## 3. What does `temperature` do? What about `top_p`?
- Both `temperature` and `top_p` control how “random” or “creative” an AI model’s responses are. 
- They shape how the model chooses the next word.

### 3.1 Temperature (controls randomness)

- Temperature adjusts how confident vs creative the model is.

- How it works

    - The model assigns probabilities to possible next words.

        - Low temperature (0.0 – 0.3)
            - more deterministic, focused, repetitive
            - picks the most likely words
        - Medium (0.5 – 0.8)
            - balanced creativity and accuracy
        - High (0.9 – 1.5+)
            - more random, creative, sometimes unpredictable
- Example

    - Prompt: “The sky is…”

        - Temp = 0.1:
            - “blue.”
        - Temp = 0.7:
            - “blue and calm today.”
        - Temp = 1.2:
            - “a shifting ocean of light and wandering clouds.”

<div align="center">
<img src="Screenshots\Temperature.jpg" width=800>
</div>

<p style="text-align:center;">────────────</p>

### 3.2 Top-p (nucleus sampling)
- Top-p controls the pool of words the model is allowed to choose from.
- Instead of taking all possible words, it takes the smallest group whose total probability >= p.

- How it works
    - Sort words by probability
    - Add them until cumulative probability reaches p
    - Sample only from that set

<div align="center">
<img src="Screenshots\top p.png" width=800>
</div>

---

## 4. What is `max_tokens` and how does it affect cost?

- `max_tokens` is a setting that controls the maximum number of tokens the model is allowed to generate in its response.


    |max_tokens |	Output behavior |
    |-----------|---------------------|
    |50	| short explanation, maybe incomplete|
    |200	| decent full explanation|
    |1000	| very detailed explanation|

---

## 5. What is `context window`?

- The context window is the maximum amount of text (in tokens) that a model can “see” and use at one time.
- It includes:

    - your system message
    - your user messages
    - the assistant’s previous replies
    - and sometimes tool outputs or retrieved documents

for example:
- If a model has a context window of 8,000 tokens, it means:
    - It can only consider the most recent ~8,000 tokens of the conversation at once.
    - Anything beyond that gets truncated or dropped.

<p style="text-align:center;">────────────</p>

- Different models have different windows:

    |Model type	|Context window|
    -----------|---------------|
    |Small models	|2K–8K tokens|
    |Standard LLMs	|16K–32K|
    |Advanced models	|100K+ tokens|

---

## 6. What is `stop_reason` and what values can it have?

- `stop_reason` is a field in an AI model response that tells you why the model stopped generating text.
- Instead of just giving output, the API also tells you what caused the end of the response.

<p style="text-align:center;">────────────</p>

- Common stop_reason values


    |stop_reason	|Meaning|
    --------------|----------
    |`stop`	|Finished normally|
    |`length`	|Hit max token limit|
    |`stop_sequence`	|Triggered custom stop rule|
    |`content_filter`	|Blocked by safety system|
    |`tool_calls`	|Model requested tool execution|

---
