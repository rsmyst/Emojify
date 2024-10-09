const express = require("express");
const bodyParser = require("body-parser");
const { exec } = require("child_process");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const analyzeSentiment = require("./sentimentAnalysis");
const app = express();
const port = 5000;

const upload = multer({ dest: "uploads/" });

app.use(bodyParser.json());

app.post("/emojify", (req, res) => {
  const { text } = req.body;
  const sentiment = analyzeSentiment(text);

  const sentimentString = JSON.stringify(sentiment).replace(/"/g, '\\"');

  exec(
    `python emojifier.py "${text}" "${sentimentString}"`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return res.status(500).send("Error processing text");
      }
      const emojifiedText = JSON.parse(stdout);
      res.json({ emojifiedText, sentiment });
    }
  );
});

app.post("/transcribe", upload.single("audio"), (req, res) => {
  const audioPath = req.file.path;
  const wavPath = path.join("uploads", `${path.parse(audioPath).name}.wav`);

  // Convert the audio file to WAV format using ffmpeg
  exec(`ffmpeg -i ${audioPath} ${wavPath}`, (error) => {
    if (error) {
      console.error(`ffmpeg error: ${error}`);
      return res.status(500).send("Error converting audio file");
    }

    exec(`python transcribe.py "${wavPath}"`, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return res.status(500).send("Error transcribing audio");
      }
      const transcript = stdout.trim();
      res.json({ transcript });

      // Clean up the uploaded and converted files
      fs.unlink(audioPath, (err) => {
        if (err) console.error(`Error deleting original audio file: ${err}`);
      });
      fs.unlink(wavPath, (err) => {
        if (err) console.error(`Error deleting converted audio file: ${err}`);
      });
    });
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
