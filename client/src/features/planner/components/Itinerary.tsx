interface Props {
    itinerary: string[];
}

function Itinerary({ itinerary }: Props) {

    return (

        <div>

            <h2>Itinerary</h2>

            {
                itinerary.map((day, index) => (

                    <div key={index}>

                        <h3>Day {index + 1}</h3>

                        <p>{day}</p>

                    </div>

                ))
            }

        </div>

    );

}

export default Itinerary;