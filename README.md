<h2>🤖 DigiMitra: LLM-Based Q&A Bot for Computer Education</h2>

<p>DigiMitra is an AI-powered Question & Answer bot designed to assist users with queries strictly related to computer fundamentals and digital tools. The system ensures focused, accurate, and structured responses by limiting its domain to computer-related topics only.

The project leverages Large Language Models (LLMs) along with structured data to provide reliable and consistent answers aligned with predefined learning content.</p>

<h4>🚀 Features</h4>
<ul>
  <li>💡 Domain-specific Q&A (Computer-related topics only)</li>
  <li>🤖 Powered by OpenAI LLM</li>
  <li>🔗 Built using LangChain framework</li>
  <li>📚 Uses structured JSON datasets for guided responses</li>
  <li>⚡ Fast and context-aware answers</li>
  <li>🎯 Controlled output to avoid irrelevant responses</li>
</ul>

<h4>🛠️ Tech Stack</h4>
<ul>
  <li>Language: Python</li>
  <li>Framework: LangChain</li>
  <li>LLM: OpenAI</li>
  <li>Data Format: JSON (raw_data & processed_data)</li>
</ul>

<h4>📂 Project Structure</h4>
DigiMitra/ <br>
│── llm_helper.py # Handles LLM interaction and response generation <br>
│── content_gen.py # Generates structured content for responses <br>
│── preprocess.py # Processes raw data into structured format <br>
│── main.py # Entry point of the application <br>
│── raw_data/ # Original dataset (JSON files) <br>
│── processed_data/ # Cleaned and structured dataset <br>

<h4>⚙️ How It Works</h4>
<ol>
  <li>Data Preparation</li>
  <ul>
    <li>Raw data is stored in JSON format.</li>
    <li>preprocess.py cleans and structures the data.</li>
  </ul>
</ol>  

<ol>
  <li>Content Structuring</li>
  <ul>
    <li>content_gen.py formats the processed data for better understanding.</li>
  </ul>
</ol>  

<ol>
  <li>LLM Integration</li>
  <ul>
    <li>llm_helper.py interacts with the OpenAI model using LangChain.</li>
  </ul>
</ol>  

<ol>
  <li>Execution</li>
  <ul>
    <li>main.py runs the application and handles user queries.</li>
  </ul>
</ol> 

<h4>🧠 Key Concept</h4>
DigiMitra follows a controlled-response approach, where:
<ul>
  <li>The bot only answers computer-related questions</li>
  <li>Uses predefined structured knowledge</li>
  <li>Avoids hallucination by grounding responses in dataset</li>
</ul>

<h4>▶️ Setup Instructions</h4>

<ol>
  <li>Clone the Repository</li>
  <p>git clone https://github.com/your-username/DigiMitra.git cd DigiMitra</p>

  <li>Install Dependencies</li>
  <p>pip install -r requirements.txt</p>

  <li>Set Environment Variables</li>
  <p>Create a .env file and add: <br>
    OPENAI_API_KEY=your_api_key_here
  </p>

  <li>Run the Application</li>
  <p>python main.py</p>
</ol>

<h4>Use Cases</h4>

<ul>
  <li>Digital literacy education for beginners</li>
  <li>Computer fundamentals learning</li>
  <li>Guided AI chatbot for students</li>
  <li>Academic assistance in basic computing</li>
</ul>

<h4>🔒 Limitations</h4>

<ul>
  <li>Only answers computer-related queries</li>
  <li>Depends on the quality of provided dataset</li>
  <li>Not designed for general-purpose conversation</li>
</ul>

<h4>🌱 Future Enhancements</h4>
<ol>
  <li>UI/UX improvements (ChatGPT-like interface)</li>
  <li>Multi-language support</li>
  <li>Voice-based interaction</li>
  <li>Expansion of dataset for advanced topics</li>
</ol>

<h4>🤝 Contributing</h4>
Contributions are welcome! Feel free to fork the repository and submit a pull request.

<h4>Author</h4>
Developed by Sakshi Dethe 👩🏻‍💻

<h4>⭐ Support</h4>

If you find this project helpful, consider giving it a ⭐ on GitHub!
