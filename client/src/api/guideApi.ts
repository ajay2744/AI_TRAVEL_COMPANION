import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export interface GuideResponse {

    answer: string;

    sources: string[];

}

export async function askGuide(
    query: string
): Promise<GuideResponse> {

    const response = await axios.post<GuideResponse>(
        `${BASE_URL}/guide/ask`,
        {
            query,
        }
    );

    return response.data;

}