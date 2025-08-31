import streamlit as st
import math

# st.title("calc")
st.markdown("#### 計算機")
# セッションステートの初期化
if 'expression' not in st.session_state:
    st.session_state.expression = ''

# クリアボタンの処理
def clear_input():
    st.session_state.expression = ''
    st.session_state.expression2 = ''
    st.session_state.expression3 = ''

# 入力欄とクリアボタン
st.button("クリア", on_click=clear_input)
expression = st.text_input("数式を入力してEnterを押してください : ", key='expression')


# piをmath.piに置き換える
if expression:
    expression = expression.replace('pi', 'math.pi')
if expression:
    expression = expression.replace('sqrt(', 'math.sqrt(')

if expression:
    try:
        result = eval(expression)
        st.write(f"結果: {result}")
    except Exception as e:
        st.write(f"エラー: {e}")

# 入力欄とクリアボタン
expression2 = st.text_input("2進数を10進数に変換します : ", key='expression2')
if expression2:
    try:
        # 2進数文字列を10進数に変換
        result = int(expression2, 2)
        st.write(f"10進数: {result}")
    except Exception as e:
        st.write(f"エラー: {e}")

expression3 = st.text_input("10進数を2進数に変換します : ", key='expression3')
if expression3:
    try:
        # 10進数を2進数に変換
        result = bin(int(expression3))
        st.write(f"2進数: {result}")
    except Exception as e:
        st.write(f"エラー: {e}")