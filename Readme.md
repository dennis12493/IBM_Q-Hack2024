# IBM_Q-Hack2024

## Frontend

To use the frontend you need to set your OpenAI API key. Do this with the following command.
Replace `###OPENAI_API_KEY###` with your API key.

```bash
echo "VITE_OPENAI_API_KEY=###OPENAI_API_KEY###" > frontend/.env
```

## Backend transcript

```bash
mkdir --parents backend-transcript/resources/deepspeach
curl --location https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm \
    > backend-transcript/resources/deepspeach/models.pbmm
curl --location https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer \
    > backend-transcript/resources/deepspeach/models.scorer
```
