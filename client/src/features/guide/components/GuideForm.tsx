import { useState } from "react";

interface Props {

    onAsk: (query: string) => void;

}

function GuideForm({ onAsk }: Props) {

    const [query, setQuery] = useState("");

    const handleAsk = () => {

        if (!query.trim()) return;

        onAsk(query);

    };

    return (

        <div>

            <h2>AI Travel Guide</h2>

            <input

                type="text"

                placeholder="Ask about a place..."

                value={query}

                onChange={(e) => setQuery(e.target.value)}

            />

            <button onClick={handleAsk}>

                Ask Guide

            </button>

        </div>

    );

}

export default GuideForm;