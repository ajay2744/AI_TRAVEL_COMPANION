import { useState } from "react";
import { planTrip } from "../../../api/travelApi";
import type { TravelResponse } from "../../../shared/types/travel";
import Itinerary from "./Itinerary";
// import PlannerResult from "./PlannerSummary";

import PlannerSummary from "./PlannerSummary";

import RestaurantList from "../../recommendation/components/RestaurantList";
import NearbyPlaces from "../../recommendation/components/NearbyPlaces";

import GuideForm from "../../guide/components/GuideForm";
import GuideResponse from "../../guide/components/GuideResponse";
import { askGuide } from "../../../api/guideApi";

function PlannerForm() {
    const [query, setQuery] = useState("");
    const [trip, setTrip] = useState<TravelResponse | null>(null);
    const [guideResponse, setGuideResponse] = useState("");
    const [guideSources, setGuideSources] = useState<string[]>([]);
    const handleGuideQuestion = async (query: string) => {

    try {

        const result = await askGuide(query);

        setGuideResponse(result.answer);

        setGuideSources(result.sources);

    }

    catch (error) {

        console.error(error);

        setGuideResponse("Unable to fetch guide information.");

        setGuideSources([]);

    }

};
    const handlePlanTrip = async () => {

        const result = await planTrip(query);

        setTrip(result);
//         const mockTrip: TravelResponse = {

//     city: "Mysore",

//     days: 3,

//     budget: 15000,

//     itinerary: [

//         "Visit Mysore Palace and St. Philomena's Church",

//         "Chamundi Hills and Mysore Zoo",

//         "Srirangapatna and Brindavan Gardens",

//     ],

//     restaurants: [

//         {

//             name: "Mylari",

//             rating: 4.8,

//             address: "Nazarbad Main Road",

//         },

//         {

//             name: "Hotel RRR",

//             rating: 4.7,

//             address: "Gandhi Square",

//         },

//     ],

//     nearby_places: [

//         {

//             name: "Mysore Palace",

//             description: "Historic Palace",

//             address: "Mysore",

//             latitude: 12.3052,

//             longitude: 76.6552,

//             rating: 4.8,

//             place_id: "abc123",

//         },

//         {

//             name: "Chamundi Hills",

//             description: "Tourist Attraction",

//             address: "Mysore",

//             latitude: 12.272,

//             longitude: 76.67,

//             rating: 4.7,

//             place_id: "xyz456",

//         },

//     ],

// };

// setTrip(mockTrip);

    };
    return (
        <div>

            <h2>Plan Your Trip</h2>

            <input
                type="text"
                placeholder="Enter your travel plan..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />

            <button onClick={handlePlanTrip}>
                Plan Trip
            </button>
            {
                trip && (

                    <>

                        <PlannerSummary
                            trip={trip}
                        />

                        <Itinerary
                            itinerary={trip.itinerary}
                        />

                        <RestaurantList
                            restaurants={trip.restaurants}
                        />

                        <NearbyPlaces
                            places={trip.nearby_places}
                        />

                    </>

                )
            }

<hr />

<GuideForm
    onAsk={handleGuideQuestion}
/>

<GuideResponse

    response={guideResponse}

    sources={guideSources}

/>

</div>

)

}
export default PlannerForm;