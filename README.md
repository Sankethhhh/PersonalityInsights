<!DOCTYPE html>
<html>

<body>

  <h1>Psychometric Assessments Project</h1>

  <p>This project focuses on two widely used psychometric assessments - the Big 5 Personality Traits and the Hexaco Personality Inventory. The user interface is built using the Streamlit library, and the assessment results are stored in <code>assessment_database.json</code>.</p>

  <h2>Big 5 Personality Traits</h2>

  <p>The Big Five personality traits, also known as the Five Factor Model (FFM), include:</p>

  <ol>
      <li>Openness</li>
      <li>Conscientiousness</li>
      <li>Extraversion</li>
      <li>Agreeableness</li>
      <li>Neuroticism</li>
  </ol>

  <p>This assessment provides insights into an individual's personality based on these five dimensions.</p>

  <h2>Hexaco Personality Inventory</h2>

  <p>The Hexaco Personality Inventory measures six major personality dimensions:</p>

  <ol>
      <li>Honesty-Humility</li>
      <li>Emotionality</li>
      <li>eXtraversion</li>
      <li>Agreeableness</li>
      <li>Conscientiousness</li>
      <li>Openness to Experience</li>
  </ol>

  <p>It offers a comprehensive view of an individual's personality, including traits not covered by the Big 5.</p>

  <h2>Usage Steps</h2>

  <ol>
      <li><strong>Clone the Repository:</strong></li>
      <pre><code>git clone https://github.com/Sankethhhh/PersonalityInsights.git</code></pre>
      <li><strong>Install Dependencies:</strong></li>
       <pre><code>cd PersonalityInsights
pip install -r requirements.txt</code></pre>
      <li>Run the Streamlit app: 
        <p>For Big 5 assessment: <code>streamlit run big5/big5_app.py</code></p>
        <p>For Hexaco assessment: <code>streamlit run hexaco/hexaco_app.py</code></p></li>
      <li>Access the application in your web browser at <code>http://localhost:8501</code>)</li>
      <li>Complete the assessments and submit your responses</li>
      <li>View the results in the console and find the detailed output in <code>assessment_database.json</code></li>
  </ol>


  <h2>Notes</h2>

  <p>Make sure to customize the project as needed and refer to the Streamlit documentation for further details on customizing the UI and handling assessments.</p>

</body>

</html>
