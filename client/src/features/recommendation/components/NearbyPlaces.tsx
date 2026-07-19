import type { Place } from "../../../shared/types/travel";

interface Props {
    places: Place[];
}

function NearbyPlaces({ places }: Props) {

    return (

        <div>

            <h2>Nearby Attractions</h2>

            {
                places.length === 0 ? (

                    <p>No nearby places found.</p>

                ) : (

                    places.map((place, index) => (

                        <div key={index}>

                            <h3>{place.name}</h3>

                            <p>
                                <strong>Description:</strong> {place.description}
                            </p>

                            <p>
                                <strong>Rating:</strong> {place.rating ?? "N/A"}
                            </p>

                            <p>
                                <strong>Address:</strong> {place.address}
                            </p>

                        </div>

                    ))

                )
            }

        </div>

    );

}

export default NearbyPlaces;