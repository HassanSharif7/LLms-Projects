import streamlit as st
import google.generativeai as genai

# Configure API key for Google Gemini
Google_API_KEY = "Hassan API"
genai.configure(api_key=Google_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def generate_sql_query(prompt_text):
    # Generate SQL query using the model
    response = model.generate_content(prompt_text)
    return response.text


def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon=":robot:")
    st.markdown(
        """
        <style>
            body {
                background-color: #000000;
                color: #FFFFFF;
            }
            .header {
                text-align: center;
                color: #E0E0E0;
            }
            .header h1 {
                font-family: 'Courier New', Courier, monospace;
                font-size: 3rem;
                color: #4CAF50;
                text-shadow: 2px 2px 4px #000000;
            }
            .header h3 {
                font-family: 'Arial', sans-serif;
                font-size: 2rem;
                color: #FFC107;
                text-shadow: 1px 1px 2px #000000;
            }
            .header p {
                font-family: 'Verdana', sans-serif;
                font-size: 1.2rem;
                color: #FF5722;
                text-shadow: 1px 1px 2px #000000;
            }
            .button {
                background-color: #1f77b4;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
            }
            .button:hover {
                background-color: #00509e;
            }
        </style>
        <div class="header">
            <h1>🚀 Dynamic SQL Query Generator</h1>
            <h3>Transform Your Text into Powerful SQL Queries!</h3>
            <p>Effortlessly create SQL queries from your natural language descriptions.</p>
        </div>      
        """,
        unsafe_allow_html=True,
    )

    text_input = st.text_area("Enter your text here", key="text_input")

    if st.button("Generate SQL Query", key="generate_button"):
        with st.spinner("Generating SQL Query"):
            template = """
            Create a SQL query snippet using the below text:

            ''' 
                {text_input}
            '''

            I just want a SQL query.
            """
            formatted_template = template.format(text_input=text_input)

            # Call the model to generate the SQL query
            sql_query = generate_sql_query(formatted_template)

            st.subheader("📜 Generated SQL Query:")
            st.write(sql_query, unsafe_allow_html=True)

            expected_output = f"""
                📈 What would be the expected response of this SQL query snippet:
                '''
                {sql_query}
                '''
                Provide a sample tabular response with no explanation.
            """
            expected_output_format = expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_format)
            eoutput = eoutput.text
            st.write(eoutput, unsafe_allow_html=True)

            explanation = f"""
                📚 Explain this SQL Query:
                '''
                {sql_query}
                '''
                Provide the simplest information and in 3 to 4 lines.
            """
            explanation_format = explanation.format(sql_query=sql_query)
            explanation = model.generate_content(explanation_format)
            explanation = explanation.text
            st.write(explanation, unsafe_allow_html=True)


main()
