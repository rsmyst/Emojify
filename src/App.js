import React, { useState } from "react";
import axios from "axios";
import InputField from "./components/InputField";
import VoiceRecognition from "./components/VoiceRecognition";

function App() {
  const [inputText, setInputText] = useState("");
  const [emojifiedText, setEmojifiedText] = useState([]);
  const [selectedEmojis, setSelectedEmojis] = useState({});

  const handleSubmit = async () => {
    const response = await axios.post("/emojify", {
      text: inputText,
    });
    setEmojifiedText(response.data.emojifiedText);
  };

  const handleEmojiChange = (word, emoji) => {
    setSelectedEmojis((prev) => ({
      ...prev,
      [word]: emoji,
    }));
  };

  const getFinalOutput = () => {
    return emojifiedText
      .map(({ word, emoji }) => selectedEmojis[word] || emoji)
      .join(" ");
  };

  return (
    <div className="container">
      <h1>Emojify</h1>
      <InputField
        inputText={inputText}
        setInputText={setInputText}
        handleSubmit={handleSubmit}
      />
      <VoiceRecognition setInputText={setInputText} />
      <div>
        <h3>Emojified Text:</h3>
        <div className="flex">
          {emojifiedText.map(({ word, emoji, alternatives }) => (
            <div key={word} className="word-container">
              {alternatives.length > 0 ? (
                <>
                  <span>{word}: </span>
                  <select
                    value={selectedEmojis[word] || emoji}
                    onChange={(e) => handleEmojiChange(word, e.target.value)}
                  >
                    <option value={emoji}>{emoji}</option>
                    {alternatives.map((alt) => (
                      <option key={alt} value={alt}>
                        {alt}
                      </option>
                    ))}
                  </select>
                </>
              ) : (
                <span>{word} </span>
              )}
            </div>
          ))}
        </div>
      </div>
      <div>
        <h3>Final Output:</h3>
        <p>{getFinalOutput()}</p>
      </div>
    </div>
  );
}

export default App;
