export interface Restaurant {

    name: string;

    rating: number | null;

    address: string;

}

export interface Place {

    name: string;

    description: string;

    address: string;

    latitude: number;

    longitude: number;

    place_id: string;

    rating: number | null;

}

export interface TravelResponse {

    city: string;

    days: number;

    budget: number | null;

    itinerary: string[];

    restaurants: Restaurant[];

    nearby_places: Place[];

}