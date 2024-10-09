const vader = require("vader-sentiment");

function analyzeSentiment(text) {
  const intensity = vader.SentimentIntensityAnalyzer.polarity_scores(text);
  return intensity;
}

module.exports = analyzeSentiment;
