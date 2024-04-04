# IBM_Q-Hack2024

## Frontend

To use the frontend you need to set your OpenAI API key. Do this with the following command.
Replace `###OPENAI_API_KEY###` with your API key.

```bash
echo "VITE_OPENAI_API_KEY=###OPENAI_API_KEY###" > frontend/.env
```

Start the frontend development server with the following command:
```bash
cd frontend
npm install
npm run dev
```

## Backend

Start the backend development server with the following command:
```bash
pip3 install fastapi nltk uvicorn youtube_transcript_api
uvicorn backend:app --reload --port 8080
```
