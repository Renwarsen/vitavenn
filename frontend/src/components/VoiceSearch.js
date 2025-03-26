
import React, { useState } from "react";

const VoiceSearch = () => {
  const [transcript, setTranscript] = useState("");

  const startListening = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "no-NO";
    recognition.interimResults = false;
    recognition.onresult = (event) => {
      const text = event.results[0][0].transcript;
      setTranscript(text);
    };
    recognition.start();
  };

  return (
    <div>
      <button onClick={startListening}>🎙 Snakk med Vitavenn</button>
      <p>Du sa: {transcript}</p>
    </div>
  );
};

export default VoiceSearch;
