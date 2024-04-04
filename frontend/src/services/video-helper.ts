import OpenAI from "openai";
import transcripts from "../lib/assets/transcripts.json";
import axios from "axios";

export type UserMessage = {
        sender: "me" | "other";
        message: string;
    };

const openaiApiKey: string = import.meta.env.VITE_OPENAI_API_KEY;
const openai = new OpenAI({ apiKey: openaiApiKey, dangerouslyAllowBrowser: true });

async function fetchTranscript(videoId: string) {
    let response = await axios.get(
        "/api/transcript/youtube/" + videoId,
        {
            headers: {
                "Content-Type": "application/json",
            }
        }
    );
    return response.data;
}

async function askOpenAI(question: string, systemPrompt: string,  oldUserMessages: UserMessage[]) {
    let oldMessages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [];
    oldMessages.push({ role: "system", content: systemPrompt });
    oldUserMessages.forEach((oldUserMessage) => {
        oldUserMessage.sender === "me"
            ? oldMessages.push({ role: "user", content: oldUserMessage.message })
            : oldMessages.push({ role: "assistant", content: oldUserMessage.message });
    });

    let messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
        { role: "user", content: "Here is the new question the user asked: " + question },
    ];
    messages = oldMessages.concat(messages);
    console.log("Asking OpenAI with following messages:", messages);
    let completion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages,
    });
    console.log("Response from OpenAI:", completion);
    let answerChoice = completion.choices[0];
    if (answerChoice.finish_reason != "stop") {
        console.error("OpenAI did not finish successful generating an answer.");
    }
    return answerChoice.message.content ?? "Sorry, currently I can't help you.";
}

async function getTranscript(videoId: string) {
    let transcriptRaw = transcripts[videoId];
    if (!transcriptRaw) {
        console.log("Transcript for video with id " + videoId + " not found. Asking API.");
        transcriptRaw = await fetchTranscript(videoId);
        transcripts[videoId] = transcriptRaw;
    }
    return JSON.stringify(transcripts[videoId]);
}

async function getVideoSystemPrompt(videoId: string) {
    let transcript = await getTranscript(videoId);
    let systemPrompt =
        transcript +
        "\n" +
        "You are a helpful assistant, which answers the question with information from the upper " +
        'transcript. You provide an explanation to the question and also an beginning timestamp, where the explanation can be found in the video of the transcript. The answer has to be in the format "TIMESTAMP:EXPLANATION".';
    return systemPrompt;
}

export async function askAboutVideo(videoId: string, question: string, oldUserMessages: UserMessage[]) {
    let systemPrompt = await getVideoSystemPrompt(videoId);
    let answer = await askOpenAI(question, systemPrompt, oldUserMessages);
    let message = answer.split(":");
    return { timestamp: parseInt(message[0]), answer: message[1] };
}
