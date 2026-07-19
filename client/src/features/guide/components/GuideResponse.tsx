interface Props {

    response: string;

    sources: string[];

}

function GuideResponse({

    response,

    sources,

}: Props) {

    return (

        <div>

            <h2>Guide Response</h2>

            <p>{response}</p>

            {
                sources.length > 0 && (

                    <>

                        <h3>Sources</h3>

                        <ul>

                            {
                                sources.map((source, index) => (

                                    <li key={index}>
                                        {source}
                                    </li>

                                ))
                            }

                        </ul>

                    </>

                )
            }

        </div>

    );

}

export default GuideResponse;