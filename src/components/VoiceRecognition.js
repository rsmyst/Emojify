import React from "react";
import axios from "axios";

function VoiceRecognition({ setInputText }) {
  const handleVoiceInput = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      const audioChunks = [];

      mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
      };

      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
        const formData = new FormData();
        formData.append("audio", audioBlob, "voiceInput.webm");

        const response = await axios.post("/transcribe", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        const { transcript } = response.data;
        setInputText(transcript);
      };

      mediaRecorder.start();
      setTimeout(() => {
        mediaRecorder.stop();
      }, 5000); // Record for 5 seconds
    } catch (error) {
      console.error("Error recording audio:", error);
    }
  };

  return (
    <div>
      <button className="speakBtn" onClick={handleVoiceInput}>
        Speak
      </button>
    </div>
  );
}

export default VoiceRecognition;
