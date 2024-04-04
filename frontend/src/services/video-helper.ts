import { YoutubeTranscript } from "youtube-transcript";
import OpenAI from "openai";
import transcripts from "../lib/assets/transcripts.json";

export type UserMessage = {
        sender: "me" | "other";
        message: string;
    };

const openaiApiKey: string = import.meta.env.VITE_OPENAI_API_KEY;
const openai = new OpenAI({ apiKey: openaiApiKey, dangerouslyAllowBrowser: true });

async function fetchTranscript(videoId: string) {
    return await YoutubeTranscript.fetchTranscript(videoId);
}

async function askOpenAI(question: string, systemPrompt: string,  oldUserMessages: UserMessage[], transcript: string) {
    let oldMessages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [];
    oldMessages.push({ role: "system", content: systemPrompt });
    oldMessages.push({ role: "user", content: "Here is the transcript of the video on which the user refers: " + transcript });
    oldMessages.push({ role: "user", content: "These are old messages with the user:" });
    oldUserMessages.forEach((oldUserMessage) => {
        oldUserMessage.sender === "me" ? oldMessages.push({ role: "user", content: oldUserMessage.message }) : oldMessages.push({ role: "assistant", content: oldUserMessage.message });
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

function getVideoSystemPrompt() {
    let systemPrompt =
        "You are a helpful assistant, which answers the question with information from provided " +
        'transcript. You provide an explanation to the new question and also an single integer timestamp, where the explanation can be found in the video of the transcript. The answer is always in the format "TIMESTAMP:EXPLANATION".';
    return systemPrompt;
}

export async function askAboutVideo(videoId: string, question: string, oldUserMessages: UserMessage[]) {
    let systemPrompt = getVideoSystemPrompt();
    let answer = await askOpenAI(question, systemPrompt, oldUserMessages, JSON.stringify(transcripts[videoId]));
    let message = answer.split(":");
    return { timestamp: parseInt(message[0]), answer: message[1] };
}
