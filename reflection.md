# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The submit button did not work no matter how many times i pressed it. The game would not refresh after winning. The hints were totally wrong, when the guess was lower the hint said to go higher.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used VS Code Copilot to debug glitches in the code. When playing, i found a bug where hints displayed were wrong. It was due to reverse logic in the code. I asked Copilot and it was able to fix the mistake by switching certain lines.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To see if the bug was really fixed, I actually went to the app GUI to test the fix. It indeed worked, so I confirmed Copilot's changes. I tried doing a pytest, but I ran into error where my terminal couldn't process the command, so Copilot helped me add more needed imports and install .venv to run the pytest. It showed lots of errors that were needed to be fixed, then it showed multiple failed test that Copilot successfully fixed. Yes, AI helped me understand multiple errors in the code.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing because it wasn't stored in Streamlit's session state. It caused the number to regenerate every time. Reruns are caused by every interaction with the app, so whenever you press something, the script would run again and again. This is the script AI fixed `if "secret" not in st.session_state:
st.session_state.secret = random.randint(low, high)`
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think that some strategy I should use for the next labs/projects is constantly checking the app. Whenever AI does not understand/fix the issue, you try to explain it like you're explaining it to a 5 year old. It really helped me solve some issues.
Next time I will try to dive deeper into the code instead of jumping straight to AI. Yes, it can generate and write the code for us, but in the end we humans should be able to understand the code itself.
This project helped me understand that AI is still underdeveloped and makes some logic mistakes that even a human would not make. This is why humans and AI need each other.
---
