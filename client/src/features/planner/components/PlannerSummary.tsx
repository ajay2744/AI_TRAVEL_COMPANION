import type { TravelResponse } from "../../../shared/types/travel";

interface Props {
    trip: TravelResponse;
}

function PlannerSummary({ trip }: Props) {

    return (

        <div>

            <h2>Trip Summary</h2>

            <p>
                <strong>Destination:</strong> {trip.city}
            </p>

            <p>
                <strong>Days:</strong> {trip.days}
            </p>

            <p>
                <strong>Budget:</strong> ₹{trip.budget}
            </p>

        </div>

    );

}

export default PlannerSummary;