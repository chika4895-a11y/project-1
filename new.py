import matplotlib.pyplot as plt
import streamlit as st
 
# Sample data for two students
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
student_A = [60, 65, 70, 68, 75]
student_B = [55, 60, 65, 67, 73]
 
# Create the plot
fig, ax = plt.subplots()
ax.plot(months, student_A, label="Student A", marker='o')
ax.plot(months, student_B,
         label="Student B", marker='s')
ax.set_title("Performance Comparison")
ax.set_xlabel("Month")
ax.set_ylabel("Test Score")
ax.legend()
ax.grid(True)
 
# Show chart
st.pyplot(fig)