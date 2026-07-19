import type { Restaurant } from "../../../shared/types/travel";

interface Props {
    restaurants: Restaurant[];
}

function RestaurantList({ restaurants }: Props) {

    return (

        <div>

            <h2>Recommended Restaurants</h2>

            {
                restaurants.length === 0 ? (

                    <p>No restaurants available.</p>

                ) : (

                    restaurants.map((restaurant, index) => (

                        <div key={index}>

                            <h3>{restaurant.name}</h3>

                            <p>
                                <strong>Rating:</strong> {restaurant.rating ?? "N/A"}
                            </p>

                            <p>
                                <strong>Address:</strong> {restaurant.address}
                            </p>

                        </div>

                    ))

                )
            }

        </div>

    );

}

export default RestaurantList;