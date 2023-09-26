import streamlit as st
import pandas as pd


st.title("GTD App")


if "todos" not in st.session_state:
    st.session_state["todos"] = []

def refresh():
    st.session_state['todos'] = edited_df


if todo := st.chat_input("오늘의 할일"):
    st.session_state["todos"].append({"할일": todo, "상태": '😶‍🌫️'})


df = pd.DataFrame(st.session_state["todos"])

def submit():
    st.session_state.todo135 = st.session_state.widget
    st.session_state.widget = ''

st.text_input('text something', key='widget', on_change=submit)



edited_df = st.data_editor(
    st.session_state['todos'], 
    column_config={
        "할일": st.column_config.TextColumn(
            "할일설명",
            help="GTD 중 수집단계입니다.",
            width="large",
            required=False
        ),
        "상태": st.column_config.SelectboxColumn(
            "할일 상태",
            help='GTD 중 명료화 단계입니다.',
            width='large',
            options=[
                "버림",
                "언젠가",
                "참고자료",
                "2분내",
                "위임하기",
                "캘린더",
                "프로젝트",
            ],
            required=True
        )
    },
    hide_index=True,
)

st.session_state['todos'] = edited_df


st.session_state

# for i, todo in enumerate(st.session_state['todos']):
#     st.write(todo['할일'])


