import axios from "axios";
import type { TravelResponse } from "../shared/types/travel";

const BASE_URL = "http://127.0.0.1:8000";

export async function planTrip(query: string): Promise<TravelResponse> {

    const response = await axios.post<TravelResponse>(
        `${BASE_URL}/travel/plan`,
        { query }
    );

    return response.data;
}