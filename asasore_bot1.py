import random
import streamlit as st

# お題リスト
prompts = [
    "Architects and/or architecture firm",
    "Building material",
    "Construction methods",
    "Something sustainable in architecture",
    "Famous architecture",
    "Architectural styles",
    "Structural components of a building",
    "Dream travel destinations",
    "'high' in any sense (height, price, or value)"
]

# タイトルを表示
st.title("Agree to Win! the alphabet game")

# 説明文を表示
st.write("Press the button to generate a random prompt and letter.")

# ルール説明を表示
st.markdown("""
### How to Play:
1. Press the **Generate Prompt and Letter** button to receive a random letter and a prompt.
2. Think of a word that starts with the given letter and matches the prompt.
3. The word can be serious or humorous. Discuss with your friends and decide which answer fits the best!
""")

# ボタンが押されたら結果を生成
if st.button("Generate Prompt and Letter"):
    # ランダムにお題を選ぶ
    selected_prompt = random.choice(prompts)

    # ランダムにアルファベットを選ぶ
    selected_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # 結果を表示
    st.write(f"📋 **Prompt**: {selected_prompt}")
    st.write(f"🔤 **Letter**: {selected_letter}")
