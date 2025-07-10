import streamlit as st
import pandas as pd

st.title('Personal Expense Tracker')

if 'expenses' not in st.session_state:
    st.session_state.expenses=pd.DataFrame(columns=['Date', 'Category', 'Amount'])

with st.form('Expense form'):
    date=st.text_input('Date: year-month-day')
    category=st.selectbox('Category',['Food','Transport','Tution fees','Shopping'])
    amount=st.number_input('Amount:', min_value=0.0) #amount less than zero not possible
    submit=st.form_submit_button('Add expense')

if submit:
    row={'Date':date, 'Category':category, 'Amount': amount}
    # adding this row in above columns
    st.session_state.expenses=pd.concat([st.session_state.expenses,pd.DataFrame([row])])

    st.success('Expense added successfully')


st.subheader('Your Expenses')
st.write(st.session_state.expenses)

total=st.session_state.expenses['Amount'].sum()
st.info(f"Total spent: RS,{total}")

csv = st.session_state.expenses.to_csv(index=False).encode('utf-8') # convert string in to bytes
st.download_button(label='Download',data=csv, file_name='expenses.csv', mime='text/csv')