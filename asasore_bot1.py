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
st.title("Alphabet Challenge")

# 説明文を表示
st.write("Press the button to generate a random prompt and letter.")

# ボタンが押されたら結果を生成
if st.button("Generate Prompt and Letter"):
    # ランダムにお題を選ぶ
    selected_prompt = random.choice(prompts)

    # ランダムにアルファベットを選ぶ
    selected_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    # 結果を表示
    st.write(f"📋 **Prompt**: {selected_prompt}")
    st.write(f"🔤 **Letter**: {selected_letter}")
