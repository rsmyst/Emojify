# Emojify

Emojify is a web application that converts text into emoji-enhanced text. It also includes voice recognition for input and sentiment analysis.
![image](https://github.com/user-attachments/assets/b3bb0f8f-57de-427c-be2b-bfe6ccee0e02)


https://github.com/user-attachments/assets/53e517c4-637c-44bd-9cdd-b3f8cdf65b4d


## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/rsmyst/Emojify.git
   cd Emojify
   ```

2. Install dependencies:

   ```sh
   npm install
   ```

3. Start the development server:

   ```sh
   npm start
   ```

4. The application will be available at `http://localhost:3000`.

## Usage

1. Enter text into the input field.
2. Click the "Emojify" button to convert the text.
3. Optionally, use the voice recognition feature to input text.
4. View and select alternative emojis for each word.
5. The final emojified text will be displayed below.

## Dependencies

- React
- Axios
- Vader-Sentiment
- Multer
- Http-Proxy-Middleware

## Project Structure

```
emojify/
├── .gitignore
├── build/
├── package.json
├── public/
├── README.md
├── server/
│   ├── emojifier.py
│   ├── sentimentAnalysis.js
│   ├── server.js
│   ├── transcribe.py
│   └── uploads/
├── setupProxy.js
└── src/
    ├── App.js
    ├── components/
    │   ├── InputField.js
    │   └── VoiceRecognition.js
    ├── index.css
    └── index.js
```

This Project was built for GDG WEC Recruitments 2024 by Rahul Saravanan.
Task ID: Emojify
Completion Status: Optional/Bonus tasks done. Medium Level.
