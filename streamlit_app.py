import streamlit as st

# st.title("Mi primer proyecto")
# st.write("Hola")
# st.markdown(
#     """## Hello""")

# animales = ("dog", "cat", "bird")
# name = st.text_input("Que animal: ")
# if name in animales:
#     st.write(f"Tu animal es {name}")
# else:
#     st.write(f"Tu animal no existe")

# def aplicarEdad(x):
#     return x * 10

# edad: int=st.number_input('Que edad tienes?')

# if st.button("click me"):
#     st.write(f"Tu edad  es {aplicarEdad(edad)}")

left_column, right_column = st.columns(2)
with left_column:
    st.markdown("## CALCULADORA")
    num1 = st.number_input("El primer numero", min_value=0, max_value=100)
    num2 = st.number_input("El segundo numero:", min_value=0, max_value=100)

    oper = st.radio("Seleccionar operación: ", ["Sumar", "Multiplicar"])
    match oper:
        case "Sumar": resultado = num1 + num2
        case "Multiplicar": resultado = num1 * num2

    if st.button("calcular"):
        st.markdown(f"  # {resultado}")


with right_column:
    st.markdown("Tips")
    st.video("https://www.youtube.com/watch?v=29mZql6xb9M")

add_slider = st.sidebar.slider('Select a range', 0.0, 100.0, (25.0, 75.0))

st.write(add_slider)
