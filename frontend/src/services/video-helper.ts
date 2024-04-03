import { YoutubeTranscript } from "youtube-transcript";
import OpenAI from "openai";
import transcripts from "../lib/assets/transcripts.json";

const openaiApiKey: string = import.meta.env.VITE_OPENAI_API_KEY;
const openai = new OpenAI({ apiKey: openaiApiKey, dangerouslyAllowBrowser: true });

async function fetchTranscript(videoId: string) {
    return await YoutubeTranscript.fetchTranscript(videoId);
}

async function askOpenAI(question: string, systemPrompt?: string) {
    let messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
        { role: "system", content: systemPrompt || "You are a helpful assistant." },
        { role: "user", content: question },
    ];
    console.log("Asking OpenAI with following messages:", messages);
    let completion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages,
    });
    let answerChoice = completion.choices[0];
    if (answerChoice.finish_reason != "stop") {
        console.error("OpenAI did not finish successful generating an answer.");
    }
    return answerChoice.message.content;
}

function getVideoSystemPromt(videoId: string) {
    let transcript = JSON.stringify(transcripts[videoId]);
    let systemPrompt =
        transcript +
        "\n" +
        "You are a helpful assistant, which answers the question with information from the upper " +
        'transcript.The Answer is in the format "BEGINNING_TIMESTAMP:ANSWER_TEXT".';
    return systemPrompt;
}

export async function askAboutVideo(videoId: string, question: string) {
    let systemPrompt = getVideoSystemPromt(videoId);
    return await askOpenAI(question, systemPrompt);
}
