import express from 'express';
import bodyParser from 'body-parser';
import { config } from 'dotenv';
import { Configuration, OpenAIApi } from 'openai';

config();

const app = express();
app.use(bodyParser.json());

const openAi = new OpenAIApi(
  new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  })
);

app.post('/message', async (req, res) => {
  try {
    const input = req.body.prompt;
    const response = await openAi.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: input }],
    });
    res.json({ message: response.data.choices[0].message.content });
  } catch (error) {
    res.status(500).send(error.message);
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
