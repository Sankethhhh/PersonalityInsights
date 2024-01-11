import streamlit as st
from hexaco_data import questions120, reversal, facets_questions
import json
import hashlib
from datetime import datetime
# new chart
import plotly.graph_objects as go
import random

def reverse(reversal:list, answers: dict, shift: int):
    for i in reversal:
        answers[i] = shift-answers[i]
    return answers

def domains_scores(facets_quetions: dict, answers: dict):
    scores = {}
    for domain in facets_quetions.keys():
        for facet in facets_quetions[domain].keys():
            single_facet_scores = [answers[i] for i in facets_quetions[domain][facet]]
            scores.setdefault(domain, {})[facet] = sum(single_facet_scores)/len(single_facet_scores)
    return scores

def domain_plot(domain, facets):
    """Create individual plots for each domain."""

    # colors = ['blue', 'green', 'orange', 'red', 'purple', 'brown']
    palettes = [
    '#FFB6C1', '#FFD700', '#98FB98', '#ADD8E6', '#FF6347', '#D3D3D3',  # Soft Pastels
    '#8B4513', '#CD853F', '#8FBC8F', '#D2B48C', '#DEB887', '#A52A2A',  # Earth Tones
    '#87CEEB', '#6A5ACD', '#4682B4', '#87CEFA', '#B0E0E6', '#ADD8E6',  # Tranquil Blues
    '#556B2F', '#8FBC8F', '#2E8B57', '#BDB76B', '#CD853F', '#8B4513',  # Nature Inspired
    '#D3D3D3', '#C0C0C0', '#A9A9A9', '#808080', '#696969', '#778899',  # Muted Neutrals
    '#AEEEEE', '#98FB98', '#87CEFA', '#5F9EA0', '#B0C4DE', '#AFEEEE'   # Soft Greens and Blues
    ]
    # colors = ['#%06x' % random.randint(0, 0xFFFFFF) for _ in facets]
    colors = random.sample(palettes, len(facets))
    
    # Create a horizontal bar chart using Plotly
    fig = go.Figure(go.Bar(
        x=list(facets.values()),
        y=list(facets.keys()),
        orientation='h',
        marker=dict(color=colors)
    ))

    # Update layout for better visualization
    fig.update_layout(
        title=domain,
        xaxis_title="Scores",
        yaxis=dict(autorange="reversed")  # To display bars in descending order of letters
    )
    
    # Set x-axis range from 0 to 5
    fig.update_xaxes(range=[0, 5])

    return fig

def save_to_json(data):
    # Read existing data from the file, or initialize an empty list
    try:
        with open("hexaco_database.json", "r") as file:
            existing_data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        existing_data = []

    # Append the new data to the list
    existing_data.append(data)

    # Write the updated data back to the file
    with open("hexaco_database.json", "w") as file:
        json.dump(existing_data, file, indent=4)

def main():
    st.set_page_config(page_title="Elevated Leaders - HEXACO", layout="centered")

    #  -----HEADER SECTION-----
    st.subheader("Elevated Leaders")
    st.title("HEXACO")
    st.write("The HEXACO model of personality is a comprehensive framework that identifies six major dimensions of human personality: Honesty-Humility, Emotionality, eXtraversion, Agreeableness, Conscientiousness, and Openness to Experience. Unlike some other models, HEXACO includes the dimension of Honesty-Humility, emphasizing sincerity, fairness, and modesty as essential components of individual differences in personality.")
    st.write("It is valuable for its nuanced exploration of personality traits, providing a more detailed understanding of individual differences and emphasizing ethical aspects, making it particularly useful in fields like psychology, organizational behavior, and interpersonal relationships.")  
    st.write("---")

    # Get the questions
    questions = questions120
    
    labels_map = {
        "Strongly disagree": 1,
        "Disagree": 2,
        "Neutral": 3,
        "Agree": 4,
        "Strongly agree": 5,
    }

    answers = {}
    button_key = "submit_button"  # Key for the Submit button
    
    # Display questions and collect answers
    container = st.container()
    with container:
        for q_id, question in questions.items():
            answer = st.radio(f"Q{q_id}. {question}", options=["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"], key=q_id, index=None, horizontal=True)
            
            # Store the answer in the dictionary
            answers[q_id] = str(labels_map[answer]) if answer is not None else None
        
    # Submit button
    flag = 0
    if st.button("Submit", key=button_key):
        # Check if any answer is None
        if None in answers.values():
            unanswered = [f"Q{key}" for key, value in answers.items() if value is None]
            st.warning(f"Please select answer for these questions before submitting: {', '.join(unanswered)}")
        elif flag == 1:
            st.error(f"Please refresh page and answer again")
        else:
            # Display collected answers
            st.success("Answers submitted successfully!")
            flag = 1
            
            # Convert key value to int
            answers = {int(k): int(v) for k, v in answers.items()} 
            # Get reverse answers for negative questions
            ranswers = reverse(reversal, answers, 6) 

            # Get the domain scores by taking average of each domain
            scores = domains_scores(facets_questions, ranswers)
            
            # Calculate hash value for the current set of answers
            hash_object = hashlib.sha256(json.dumps(scores, sort_keys=True).encode())
            hash_value = hash_object.hexdigest()
            
            # Get the current UTC time
            utc_now = datetime.utcnow()

            # Format the UTC time as a string
            formatted_utc_time = utc_now.strftime("%Y-%m-%dT%H:%M:%S")
            
            data = {
                "userHash": hash_value,
                "timestamp": formatted_utc_time,
                "scores": scores,
                "answers": answers
            }
            
            # Save the data to the JSON file
            save_to_json(data)
            
            for domain in scores.keys():
                # Create and display the plot
                fig = domain_plot(domain, scores[domain])
                st.plotly_chart(fig, use_container_width=True, theme="streamlit")           

if __name__ == "__main__":
    main()