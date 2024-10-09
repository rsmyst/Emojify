import React from "react";

function InputField({ inputText, setInputText, handleSubmit }) {
  return (
    <div>
      <input
        type="text"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        className="inputField"
      />
      <button className="emojiBtn" onClick={handleSubmit}>
        Emojify
      </button>
    </div>
  );
}

export default InputField;
